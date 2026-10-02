"""Optional actual screenshot capture. Requires `pip install selenium` and Chromium/chromedriver."""
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import subprocess,time
server=subprocess.Popen(['python3','-m','http.server','8000'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
try:
 o=Options();o.add_argument('--headless');o.add_argument('--no-sandbox');o.add_argument('--window-size=1440,1000')
 d=webdriver.Chrome(options=o);base='http://127.0.0.1:8000/';out=Path('screenshots');out.mkdir(exist_ok=True)
 d.get(base+'index.html');d.save_screenshot(str(out/'anti-home.png'));d.find_element(By.ID,'startBtn').click();d.find_element(By.CSS_SELECTOR,'.catalog-banner button').click();d.save_screenshot(str(out/'cart-before.png'));d.find_element(By.CSS_SELECTOR,'[data-id="bumblebee"]').click();d.save_screenshot(str(out/'cart-after.png'));d.quit()
finally: server.terminate()
