#
# https://stepik.org/lesson/732079/step/2?unit=733612
#
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.get("https://parsinger.ru/selenium/5.8/2/index.html")

    res = browser.find_element(By.ID, 'result')
    inp = browser.find_element(By.ID, 'input')
    chk = browser.find_element(By.ID, 'check')

    for b in browser.find_elements(By.CLASS_NAME, 'buttons'):
        b.click()
        pin = browser.switch_to.alert.text
        browser.switch_to.alert.accept()
        inp.clear()
        inp.send_keys(pin)
        chk.click()
        if re.search(r'[0-9a-zA-Z]', res.text):
          print(res.text)
          break
