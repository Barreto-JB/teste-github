"""Viseu em Agenda: append-only, optimistic Git coordination for scheduled roles.
Run from an isolated clone; never write the coordination ref with force.
"""
import argparse, datetime as dt, json, os, re, subprocess, sys, tempfile, uuid
from pathlib import Path
REF='refs/heads/coord/pipeline'
ROLES=('research','development','audit')
FILES=('state.json',)+tuple(x+'.json' for x in ROLES)
ORIGINS={'https://github.com/Barreto-JB/teste-github','https://github.com/Barreto-JB/teste-github.git','git@github.com:Barreto-JB/teste-github.git'}
class Busy(Exception): pass
class Pipeline:
    def __init__(self,repo,check_origin=True):
        self.repo=Path(repo)
        if check_origin and self.git('remote','get-url','origin').strip().lower() not in {x.lower() for x in ORIGINS}:
            raise RuntimeError('Unexpected origin; refusing to write')
    def git(self,*args,stdin=None,check=True):
        p=subprocess.run(['git','-C',str(self.repo),*args],input=stdin.encode('utf-8') if stdin is not None else None,capture_output=True,timeout=60,check=False)
        if check and p.returncode: raise RuntimeError(p.stderr.decode('utf-8',errors='replace').strip() or 'Git failed: '+str(args[0]))
        return p.stdout.decode('utf-8') if check else p
    def read(self):
        p=self.git('ls-remote','--heads','origin',REF,check=False)
        if p.returncode:raise RuntimeError('Cannot read remote coordination ref')
        if not p.stdout.strip():return None,{}
        self.git('fetch','--no-tags','origin',REF)
        sha=self.git('rev-parse','FETCH_HEAD').strip()
        files={f:json.loads(self.git('show',sha+':'+f)) for f in FILES}
        return sha,files
    def write(self,parent,files,message):
        rows=[]
        for name in FILES:
            value=json.dumps(files[name],ensure_ascii=False,indent=2,sort_keys=True)+'\n'
            blob=self.git('hash-object','-w','--stdin',stdin=value).strip()
            rows.append('100644 blob '+blob+'\t'+name+'\n')
        tree=self.git('mktree',stdin=''.join(rows)).strip()
        cmd=['commit-tree',tree]
        if parent:cmd+=['-p',parent]
        sha=self.git(*cmd,'-m',message).strip()
        p=self.git('push','origin',sha+':'+REF,check=False)
        if p.returncode:
            # Unknown response: accept only if exact commit is still remote; otherwise fail closed.
            actual,_=self.read()
            if actual!=sha: raise Busy('Concurrent update or failed push; no ownership acquired')
        return sha
    def init(self):
        old,files=self.read()
        if old:return old
        files={f:{} for f in FILES};files['state.json']={'status':'idle','updated':now()}
        return self.write(None,files,'coord: initialise pipeline')
    def acquire(self,role):
        old,files=self.read()
        if not old:raise RuntimeError('Coordination branch not initialised')
        if files['state.json'].get('status')!='idle':raise Busy('Pipeline busy; skip this run')
        token=uuid.uuid4().hex
        files['state.json']={'status':'running','role':role,'token':token,'updated':now()}
        sha=self.write(old,files,'coord: acquire '+role)
        actual,current=self.read()
        if actual!=sha or current['state.json'].get('token')!=token:raise Busy('Ownership not confirmed; stop')
        return token
    def release(self,role,token,handoff=None):
        old,files=self.read();state=files.get('state.json',{})
        if state.get('status')!='running' or state.get('role')!=role or state.get('token')!=token:raise Busy('Not owner; cannot release')
        if handoff is not None:
            if not isinstance(handoff,dict):raise ValueError('Handoff must be a JSON object')
            handoff=dict(handoff);handoff['role']=role;handoff['updated']=now()
            files[role+'.json']=handoff
        files['state.json']={'status':'idle','updated':now(),'last_role':role}
        return self.write(old,files,'coord: release '+role)
def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',default='.')
    sub=p.add_subparsers(dest='cmd',required=True)
    sub.add_parser('init');sub.add_parser('status')
    a=sub.add_parser('acquire');a.add_argument('role',choices=ROLES)
    a=sub.add_parser('release');a.add_argument('role',choices=ROLES);a.add_argument('token');a.add_argument('--handoff',type=Path)
    args=p.parse_args()
    try:
        g=Pipeline(args.repo)
        if args.cmd=='init':print(g.init())
        elif args.cmd=='status':
            sha,files=g.read();print(json.dumps({'commit':sha,**files},ensure_ascii=True,indent=2))
        elif args.cmd=='acquire':print(g.acquire(args.role))
        elif args.cmd=='release':print(g.release(args.role,args.token,json.loads(args.handoff.read_text(encoding='utf-8-sig')) if args.handoff else None))
    except Busy as e:print(str(e),file=sys.stderr);sys.exit(2)
    except Exception as e:print(str(e),file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()
