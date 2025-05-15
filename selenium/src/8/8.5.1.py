#
# https://stepik.org/lesson/732079/step/1?unit=733612
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.get("https://parsinger.ru/selenium/5.8/1/index.html")

    res = browser.find_element(By.ID, 'result')

    for b in browser.find_elements(By.TAG_NAME, 'input'):
        b.click()
        browser.switch_to.alert.accept()
        if res.text:
            print(res.text)
            break
