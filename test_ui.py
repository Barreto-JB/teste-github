"""Offline rendering and interaction test; no external requests required."""
from pathlib import Path
import sys
from playwright.sync_api import sync_playwright
root=Path(__file__).parent
html=(root/'index.html').read_text().replace('<link rel="stylesheet" href="styles.css">','<style>'+ (root/'styles.css').read_text()+'</style>').replace('<script defer src="app.js"></script>','<script>'+ (root/'app.js').read_text()+'</script>')
errors=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1440,'height':1000});page.on('pageerror',lambda e: errors.append(str(e)));page.set_content(html)
 assert 'Viseu,' in page.locator('h1').inner_text();page.locator('nav a[href="#explorar"]').click();page.wait_for_selector('#results .tile');assert page.locator('#results .tile').count()==25
 page.locator('#filter').fill('ranhados');assert page.locator('#results .tile').count()==1
 page.locator('nav a[href="#poupar"]').click();page.wait_for_selector('#item');page.locator('#item').fill('Leite 1 L');page.locator('#qty').fill('2');page.locator('#add button').click();page.locator('#item').fill('Arroz 1 kg');page.locator('#add button').click()
 for a,v in [('0:0','1'),('0:1','1.2'),('1:0','2'),('1:1','1')]:
  i,j=a.split(':');page.locator(f'[data-item="{i}"][data-store="{j}"]').fill(v)
 assert '3,00' in page.locator('#compare').inner_text();page.locator('#trip').fill('2');assert '3,40' in page.locator('#compare').inner_text()
 if len(sys.argv)>1:
  page.locator('nav a[href="#mobilidade"]').click();page.wait_for_selector('#fuel-file');page.locator('#fuel-file').set_input_files(sys.argv[1]);page.wait_for_selector('#fuel-type');assert page.locator('#fuel-rows tbody tr').count()==145;page.locator('#fuel-type').select_option('gasoline_95');assert page.locator('#fuel-rows tbody tr').count()==38
 page.locator('#q').fill('Cine Clube');page.locator('#search button').click();page.wait_for_selector('#app .tile');assert page.locator('#app .tile').count()==1
 page.locator('nav a[href="#inicio"]').click();page.wait_for_selector('.hero');page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth');assert not errors,errors
 b.close()
print('PASS: navigation, search, 25 parishes, basket UI, mobile layout, optional fuel import; no JS exceptions.')
