#
# https://stepik.org/lesson/732083/step/7?unit=733616
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.9/5/index.html")

    res = []
    for b in browser.find_elements(By.CLASS_NAME, 'box_button'):
        b.click()
        browser.find_element(By.ID, 'close_ad').click()
        WebDriverWait(browser, 10).until(lambda x: b.text)
        res.append(b.text)
    print('-'.join(res))
