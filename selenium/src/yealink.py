from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
from pathlib import Path
import time

f = Path(__file__).parent / '.env'
ini = configparser.ConfigParser(allow_unnamed_section=True)
ini.read([f])

opts = webdriver.ChromeOptions()
opts.add_argument("--ignore-certificate-errors")
with webdriver.Chrome(options=opts) as browser:
  browser.get("https://10.33.102.80/")

  user = browser.find_element(By.ID, 'idUsername')
  pasw = browser.find_element(By.ID, 'idPassword')
  post = browser.find_element(By.ID, 'idConfirm')

  user.send_keys(ini.get(configparser.UNNAMED_SECTION, 'USER'))
  pasw.send_keys(ini.get(configparser.UNNAMED_SECTION, 'PASS'))
  post.click()

  time.sleep(5)
