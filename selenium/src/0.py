from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://nc.ekb.ru")

time.sleep(5)
browser.quit()