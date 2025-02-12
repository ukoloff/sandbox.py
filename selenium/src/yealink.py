from selenium import webdriver
import time

opts = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
opts.add_argument("--ignore-certificate-errors")


with webdriver.Chrome(options=opts) as browser:
  browser.get("https://10.33.102.80/")

  time.sleep(5)
