"""Refresh only the openly licensed Lagenda Viseu event snapshot.
Run from the repository root with Python 3.12+; review diff and test before publishing.
"""
import json, re, urllib.request, datetime
from pathlib import Path
URL='https://lagenda.pt/dados-abertos/concelho/viseu.json'
TARGET=Path(__file__).resolve().parents[1]/'data'/'events-viseu.json'
with urllib.request.urlopen(urllib.request.Request(URL,headers={'User-Agent':'ViseuAgenda/1.0 (public open data; attribution provided)'}),timeout=30) as r:
    raw=json.loads(r.read())
if 'CC BY 4.0' not in raw.get('licenca',''):
    raise ValueError('License not confirmed; keep previous snapshot')
generated=datetime.date.fromisoformat(raw['gerado'])
previous=json.loads(TARGET.read_text(encoding='utf-8'))
if generated < datetime.date.fromisoformat(previous['generated']):
    raise ValueError('Source snapshot older than current snapshot')
events={}
for item in raw['eventos']:
    if item.get('concelho')!='Viseu' or not item.get('id') or not item.get('nome'):
        continue
    dates=[]
    for date in item.get('datas',[]):
        if isinstance(date,str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}',date):
            try:
                datetime.date.fromisoformat(date)
            except ValueError:
                continue
            dates.append(date)
    if not dates: continue
    events[item['id']]={k:item.get(k) for k in ['id','nome','hora','preco','entrada_livre','tipo','sala','pagina','ligacao_oficial']}
    events[item['id']]['datas']=sorted(set(dates))
if not events: raise ValueError('Empty feed; review manually before replacing')
if len(events)<len(previous['events'])/2: raise ValueError('Large drop in event count; review manually')
result={'source':'Lagenda (lagenda.pt)','license':'CC BY 4.0','source_url':URL,'generated':raw['gerado'],'events':list(events.values())}
tmp=TARGET.with_suffix('.tmp')
tmp.write_text(json.dumps(result,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
tmp.replace(TARGET)
print('Events:',len(events),'snapshot:',raw['gerado'])

