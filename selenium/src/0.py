from selenium import webdriver
import time


with webdriver.Chrome() as browser:
  browser.get("https://nc.ekb.ru")

  time.sleep(5)
