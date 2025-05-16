#
# https://stepik.org/lesson/732083/step/3?unit=733616
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/expectations/6/index.html")

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
    el = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))

    print(el.text)
