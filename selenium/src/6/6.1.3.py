#
# https://stepik.org/lesson/732059/step/3?unit=733592
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/6/6.2/index.html")
    link = browser.find_element(By.TAG_NAME, 'a')
    link.click()
    link = browser.find_element(By.TAG_NAME, 'a')
    link.click()
    a = 1
