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

    pairs = [[cb, btn] for cb, btn in zip(cbs, btns)]

    def tester(x):
        n = 0
        for pair in pairs:
            if len(pair) < 2:
                continue
            n += 1
            if not pair[0].get_attribute("checked"):
                continue
            pair[1].click()
            pair.pop()
        return not n

    x = WebDriverWait(browser, 10).until(tester)

    print(res.text)
