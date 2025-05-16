#
# https://stepik.org/lesson/732083/step/8?unit=733616
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.9/6/index.html")

    cb = browser.find_element(By.ID, 'myCheckbox')
    btn = browser.find_element(By.TAG_NAME, 'button')

    WebDriverWait(browser, 10).until(EC.element_to_be_selected(cb))
    btn.click()
    res = browser.find_element(By.ID, 'result')
    print(res.text)
