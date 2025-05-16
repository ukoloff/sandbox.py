#
# https://stepik.org/lesson/732083/step/9?unit=733616
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.9/7/index.html")

    res = browser.find_element(By.ID, 'result')
    cbs = browser.find_elements(By.CSS_SELECTOR, 'input[type=checkbox]')
    btns = browser.find_elements(By.TAG_NAME, 'button')

    for cb, btn in zip(cbs, btns):
        WebDriverWait(browser, 10).until(EC.element_to_be_selected(cb))
        btn.click()

    # selector = (By.CSS_SELECTOR, 'input[type=checkbox]')
    # n = len(browser.find_elements(*selector))
    # found = 0

    # while found < n:
    #   cb = WebDriverWait(browser, 10).until(EC.element_located_to_be_selected(selector))
    #   pass
    print(res.text)
