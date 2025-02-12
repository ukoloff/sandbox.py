from selenium import webdriver
from selenium.webdriver.common.by import By
import time

opts = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
opts.add_argument("--ignore-certificate-errors")


with webdriver.Chrome(options=opts) as browser:
  browser.get("https://10.33.102.80/")

  user = browser.find_element(By.ID, 'idUsername')
  pasw = browser.find_element(By.ID, 'idPassword')
  post = browser.find_element(By.ID, 'idConfirm')

  user.send_keys('admin')
  pasw.send_keys('qwerty')
  post.click()

  time.sleep(5)
