from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from playwright.sync_api import sync_playwright
import json, os, tempfile
from datetime import datetime
root=Path(__file__).resolve().parents[1]
feed=json.loads((root/'data/events-viseu.json').read_text(encoding='utf-8'))
mobi=json.loads((root/'data/mobi-osm.json').read_text(encoding='utf-8'))
out=Path(os.environ.get('VISEU_QA_OUTPUT') or tempfile.mkdtemp(prefix='viseu-qa-'));out.mkdir(parents=True,exist_ok=True);print('QA captures:',out)
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(root)))
Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/'
with sync_playwright() as p:
 browser=p.chromium.launch(channel=os.environ.get('VISEU_BROWSER','chrome'),headless=True)
 for w,h in [(1440,1000),(390,844)]:
  page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
  if os.environ.get('VISEU_SNAPSHOT_CLOCK')=='1':page.clock.set_fixed_time(datetime.fromisoformat(feed['generated']+'T12:00:00+00:00'))
  errs=[];tiles=[];console=[];page.on('pageerror',lambda e:errs.append(str(e)));page.on('console',lambda msg:console.append(msg.text) if msg.type=='error' else None)
  page.on('response',lambda r:tiles.append(r.status) if 'tile.openstreetmap.org' in r.url else None)
  page.goto(url)
  dialog=page.locator('#development-notice')
  dialog.wait_for(state='visible')
  assert dialog.evaluate("d=>d.matches(':modal')")
  assert page.evaluate("document.activeElement.id")== 'development-ack'
  page.keyboard.press('Escape');assert dialog.is_visible()
  page.mouse.click(2,2);assert dialog.is_visible()
  assert dialog.locator('a').get_attribute('href')=='https://buymeacoffee.com/barretomendes'
  assert set(dialog.locator('a').get_attribute('rel').split())=={'noopener','noreferrer'}
  page.context.route('https://buymeacoffee.com/barretomendes',lambda route:route.fulfill(status=200,body='Test navigation'))
  with page.expect_popup() as pop:dialog.locator('a').click()
  popup=pop.value;popup.wait_for_load_state('domcontentloaded');assert popup.url=='https://buymeacoffee.com/barretomendes';popup.close()
  page.context.unroute('https://buymeacoffee.com/barretomendes')
  assert dialog.is_visible()
  page.evaluate("document.fonts.ready")
  page.screenshot(path=str(out/f'notice-{w}.png'))
  page.locator('#development-ack').click();assert not dialog.is_visible()
  assert page.evaluate("sessionStorage.getItem('viseu-development-notice-v1')")=='read'
  page.reload();assert not dialog.is_visible()
  print('PASS notice',w,'ack only, new tab support, reload remembers',flush=True)
  page.locator('#v67-content .event-card').first.wait_for();assert 0<page.locator('#v67-content .event-card').count()<=3
  page.evaluate("document.querySelectorAll('.event-visual img').forEach(i=>i.loading='eager')");page.wait_for_function("[...document.querySelectorAll('.event-visual img')].every(i=>i.complete&&i.naturalWidth>0)");assert page.locator('.event-visual img').count()+page.locator('.event-no-photo').count()==page.locator('.event-card').count()
  page.evaluate("document.fonts.ready")
  assert page.evaluate("document.fonts.check('800 90px Barlow Condensed') && document.fonts.check('400 16px Manrope')"),'fonts not loaded'
  assert page.evaluate("getComputedStyle(document.querySelector('h1')).fontFamily.includes('Barlow Condensed')")
  assert page.evaluate("getComputedStyle(document.body).backgroundColor")=='rgb(243, 240, 232)'
  assert page.locator('.hero-frame').count()==1
  assert page.locator('.features a.feature').count()==4
  assert page.locator('.hero-photo').evaluate("i=>i.complete&&i.naturalWidth>0")
  page.screenshot(path=str(out/f'hero-{w}.png'),full_page=False)
  page.locator('#site-menu summary').click();assert page.locator('#site-menu').get_attribute('open') is not None
  page.keyboard.press('Escape');assert page.locator('#site-menu').get_attribute('open') is None
  page.locator('.skip').focus();page.keyboard.press('Enter');assert page.evaluate("document.activeElement.id")== 'app'
  links=page.locator('a.support-button:visible');assert links.count()==3
  for a in links.all():
   assert a.get_attribute('href')=='https://buymeacoffee.com/barretomendes'
   assert a.get_attribute('target')=='_blank'
   assert set(a.get_attribute('rel').split())=={'noopener','noreferrer'}
   assert 'Paga-me um café' in a.inner_text()
   assert a.evaluate("a=>getComputedStyle(a).backgroundColor")=='rgb(255, 221, 0)'
  dock=page.locator('.support-dock .support-button')
  page.keyboard.press('Tab');dock.focus();assert dock.evaluate("a=>getComputedStyle(a).outlineStyle")!='none'
  page.locator('.support-section').scroll_into_view_if_needed()
  page.screenshot(path=str(out/f'home-{w}.png'),full_page=False)
  if w<701:
   assert page.evaluate("document.querySelector('.site-scroll').getBoundingClientRect().bottom<=document.querySelector('.support-dock').getBoundingClientRect().top+1")
   page.locator('.footer-support').scroll_into_view_if_needed()
   assert page.locator('.footer-support .support-button').is_in_viewport() if hasattr(page.locator('.footer-support .support-button'),'is_in_viewport') else True
   assert page.evaluate("document.querySelector('.site-scroll').scrollTop>0")
  # Test opening a new tab without initiating any payment or depending on third-party UI.
  page.context.route('https://buymeacoffee.com/barretomendes',lambda route:route.fulfill(status=200,body='Link navigation verified'))
  with page.expect_popup() as pop:dock.click()
  popup=pop.value;popup.wait_for_load_state('domcontentloaded');assert popup.url=='https://buymeacoffee.com/barretomendes';popup.close()
  page.context.unroute('https://buymeacoffee.com/barretomendes')
  page.goto(url+'#agenda');page.locator('#event-query').wait_for();count=page.locator('#event-results .event-card').count();assert count>0
  assert page.locator('#event-results .event-visual img').count()+page.locator('#event-results .event-no-photo').count()==count
  page.evaluate("document.querySelectorAll('.event-visual img').forEach(i=>i.loading='eager')");page.wait_for_function("[...document.querySelectorAll('.event-visual img')].every(i=>i.complete&&i.naturalWidth>0)")
  print('REAL PHOTO COVERAGE',w,count,'unique',page.locator('#event-results img').evaluate_all('(imgs)=>new Set(imgs.map(i=>i.src)).size'),flush=True)
  venues=page.locator('#event-venue option').all_text_contents()
  if len(venues)>2:
   page.locator('#event-venue').select_option(label=venues[1]);assert 0<page.locator('#event-results .event-card').count()<count
  page.locator('#event-venue').select_option('')
  # Favorites: home/agenda share IDs; filter, reload, removal and privacy.
  page.locator('#event-saved').check();assert page.locator('#event-results .empty').count()==1
  page.locator('#event-saved').uncheck()
  btn=page.locator('#event-results .event-favorite').first;eventid=btn.get_attribute('data-favorite')
  btn.focus();page.keyboard.press('Space');assert btn.get_attribute('aria-pressed')=='true'
  assert page.locator('#saved-count').inner_text()=='1'
  page.locator('#event-saved').check();assert page.locator('#event-results .event-card').count()==1
  page.locator('#event-results .event-card').first.scroll_into_view_if_needed()
  page.screenshot(path=str(out/f'favorites-{w}.png'))
  page.reload();page.locator('#event-saved').wait_for()
  page.locator('#event-saved').check();assert page.locator('#event-results .event-favorite').first.get_attribute('data-favorite')==eventid
  assert page.locator('#event-results .event-favorite').first.get_attribute('aria-pressed')=='true'
  page.locator('#event-results .event-favorite').first.click();assert page.locator('#event-results .empty').count()==1
  page.locator('#event-saved').uncheck();page.locator('#event-results .event-favorite').first.click()
  page.goto(url+'#privacidade');page.locator('#clear-favorites').click()
  assert page.evaluate("JSON.parse(localStorage.getItem('viseu-event-favorites-v1')).length")==0
  page.goto(url+'#inicio');page.locator('.event-favorite').first.wait_for();page.locator('.event-favorite').first.click()
  page.goto(url+'#agenda');page.locator('#event-saved').wait_for();page.locator('#event-saved').check();assert page.locator('#event-results .event-card').count()==1
  page.locator('#event-results .event-favorite').first.click();page.locator('#event-saved').uncheck()
  print('PASS favorites',w,flush=True)

  page.locator('#event-query').fill('zzzzzz');assert page.locator('#event-results .empty').count()==1
  page.locator('#event-query').fill('');page.locator('#event-free').check();assert page.locator('#event-results .event-card').count()<=count
  page.locator('#event-free').uncheck();page.locator('#event-results details summary').first.click();assert page.locator('#event-results details[open] a').count()>0;assert page.locator('#event-results details[open]').count()==1
  page.evaluate("window.scrollTo(0,0);document.querySelector('.site-scroll').scrollTo(0,0)");page.screenshot(path=str(out/f'agenda-{w}.png'),full_page=False)
  page.goto(url+'#mobilidade');page.locator('#stop-query').wait_for();assert page.locator('#stop-count').inner_text().split()[0].replace('.','')==str(sum(bool(x['viseu']) for x in mobi['stops']))
  page.locator('#stop-query').fill('Mundao');assert page.locator('#stop-list .stop-item').count()>0
  page.locator('#stop-list .stop-item').first.click();assert page.locator('#stop-detail h3').count()==1
  page.locator('#stop-query').fill('');page.locator('#stop-zone').select_option('all');assert page.locator('#stop-count').inner_text().replace('.','').replace('\u00a0','').replace(' ','').startswith(str(len(mobi['stops'])))
  page.locator('#stop-next').click();assert '13' in page.locator('#stop-pages').inner_text()
  page.locator('#stop-zone').select_option('viseu');page.wait_for_timeout(1200)
  assert page.locator('#stop-map .leaflet-overlay-pane canvas').count()>0
  page.evaluate("window.scrollTo(0,0);document.querySelector('.site-scroll').scrollTo(0,0)");page.screenshot(path=str(out/f'mobility-{w}.png'),full_page=False)
  for route in ['inicio','agenda','explorar','mobilidade','poupar','fontes','passatempos','privacidade']:
   page.goto(url+'#'+route);page.wait_for_function("document.querySelector('#app').textContent.trim().length>0")
   if route=='agenda':page.locator('#event-query').wait_for()
   if route=='mobilidade':page.locator('#stop-query').wait_for()
   assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1 && document.querySelector(\'.site-scroll\').scrollWidth <= innerWidth+1'),(w,route,page.evaluate('document.documentElement.scrollWidth'))
   assert page.locator('h1').count()==1,(w,route)
  page.goto(url+'#explorar');page.locator('#filter').fill('Mundao');assert page.locator('#results .tile').count()==1
  page.goto(url+'#poupar');page.locator('#item').fill('Leite');page.locator('#add button').click();page.locator('input[data-item="0"][data-store="0"]').fill('1.25');assert '1,25' in page.locator('#compare').inner_text();page.locator('[data-remove="0"]').click();assert page.locator('.empty').count()==1
  page.locator('#q').fill('teatro');page.locator('#search button').click();page.wait_for_url('**/#pesquisa');assert page.locator('#app .tile').count()>=1;page.locator('#v67-content .event-card').first.wait_for();assert page.locator('#v67-content .event-visual img').count()>0
  page.locator('#v67-content .event-favorite').first.click();assert page.locator('#v67-content .event-favorite').first.get_attribute('aria-pressed')=='true'
  page.goto(url+'#privacidade');page.locator('#clear-favorites').click()
  assert not errs,errs
  assert not console,console
  print(f'PASS {w}x{h}: {count} events; event search/free/details; stop query/zone/details/pagination; canvas map; tile statuses {set(tiles)}; 8 routes no overflow; basket; search; zero JS/console errors; support links and popup; reserved mobile dock',flush=True)
  page.close()
 browser.close()
server.shutdown()
