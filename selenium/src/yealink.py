from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from configparser import ConfigParser, UNNAMED_SECTION
from pathlib import Path
import time

f = Path(__file__).parent / '.env'
ini = ConfigParser(allow_unnamed_section=True)
ini.read([f])

opts = webdriver.ChromeOptions()
opts.add_argument("--ignore-certificate-errors")
with webdriver.Chrome(options=opts) as browser:
  browser.implicitly_wait(5)

  browser.get("https://10.33.102.80/servlet?m=mod_data&p=network-adv&q=load")

  user = browser.find_element(By.ID, 'idUsername')
  pasw = browser.find_element(By.ID, 'idPassword')
  post = browser.find_element(By.ID, 'idConfirm')

  user.send_keys(ini.get(UNNAMED_SECTION, 'USER'))
  pasw.send_keys(ini.get(UNNAMED_SECTION, 'PASS'))
  post.click()

  vlan = browser.find_element(By.NAME, 'VlanWanSwitch')
  Select(vlan).select_by_index(0)
  post = browser.find_element(By.ID, 'btn_confirm1')
  post.click()

  post = browser.find_element(By.ID, 'btn-apply-cache-config')
  post.click()

  time.sleep(5)
