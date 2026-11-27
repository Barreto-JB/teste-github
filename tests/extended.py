from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from playwright.sync_api import sync_playwright
import json, os
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[1]
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(root)))
Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/'
with sync_playwright() as p:
 browser=p.chromium.launch(channel=os.environ.get('VISEU_BROWSER','chrome'),headless=True)
 for w,h in [(1440,1000),(390,844)]:
  page=browser.new_page(viewport={'width':w,'height':h})
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(url+'#inicio');page.locator('#development-ack').click();page.locator('.hero-photo').wait_for()
  assert page.locator('.hero-credit a').count()==2
  assert page.locator('.features a').count()==4
  assert page.evaluate("document.querySelector('.site-scroll').getBoundingClientRect().bottom<=document.querySelector('.support-dock').getBoundingClientRect().top+1")
  page.locator('#site-menu summary').click()
  page.locator('.menu-panel a[href="#agenda"]').click()
  page.locator('#event-query').wait_for()
  assert page.locator('#site-menu').get_attribute('open') is None
  count=page.locator('#event-results .event-card').count()
  opts=page.locator('#event-category option').all_text_contents()
  if len(opts)>1:
   page.locator('#event-category').select_option(label=opts[1]);assert 0<page.locator('#event-results .event-card').count()<=count
   page.locator('#event-category').select_option('')
  page.locator('#event-when').select_option('today');assert page.locator('#event-results .event-card').count()<=count
  page.locator('#event-when').select_option('week');assert page.locator('#event-results .event-card').count()<=count
  page.locator('#event-when').select_option('all');assert page.locator('#event-results .event-card').count()==count
  page.goto(url+'#mobilidade');page.locator('#stop-query').wait_for()
  payload={'records':[{'name':'Teste local QA A','fuel':'gasolina','price':1.65,'updated':datetime.now(timezone.utc).isoformat()},{'name':'Teste local QA B','fuel':'gasoleo','price':1.55,'updated':datetime.now(timezone.utc).isoformat()}]}
  page.locator('#fuel-file').set_input_files({'name':'test.json','mimeType':'application/json','buffer':json.dumps(payload).encode()})
  page.locator('#fuel-type').wait_for();assert page.locator('#fuel-rows tbody tr').count()==2
  page.locator('#fuel-type').select_option('gasoleo');assert page.locator('#fuel-rows tbody tr').count()==1
  page.locator('#fresh').check();assert page.locator('#fuel-rows tbody tr').count()==1
  page.goto(url+'#poupar');page.locator('#item').fill('Produto QA');page.locator('#add button').click()
  page.locator('[data-item="0"][data-store="0"]').fill('10')
  page.locator('#store').select_option(index=0);page.locator('#discount').fill('10')
  assert '9,00' in page.locator('#compare').inner_text()
  page.locator('#trip').fill('2')
  page.goto(url+'#privacidade');page.locator('#clear').click()
  page.goto(url+'#poupar');assert page.locator('#basket .empty').count()==1
  assert not errors,errors
  print(f'PASS extended {w}: menu links, credits, event category/date, local fuel import/filter, basket discount and privacy reset, no support overlap, zero JS errors',flush=True)
  page.close()
 browser.close()
server.shutdown()
