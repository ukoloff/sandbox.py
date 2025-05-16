#
# https://stepik.org/lesson/732079/step/3?unit=733612
#
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("https://parsinger.ru/selenium/5.8/3/index.html")

    res = browser.find_element(By.ID, 'result')
    # inp = browser.find_element(By.ID, 'input')
    chk = browser.find_element(By.ID, 'check')

    for pin in browser.find_elements(By.CLASS_NAME, 'pin'):
        id = pin.text
        chk.click()
        browser.switch_to.alert.send_keys(id)
        browser.switch_to.alert.accept()
        if re.search(r'[0-9a-zA-Z]', res.text):
          print(res.text)
          break
