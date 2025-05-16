#
# https://stepik.org/lesson/732079/step/8?unit=733612
#
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

sites = [
    "http://parsinger.ru/blank/1/1.html",
    "http://parsinger.ru/blank/1/2.html",
    "http://parsinger.ru/blank/1/3.html",
    "http://parsinger.ru/blank/1/4.html",
    "http://parsinger.ru/blank/1/5.html",
    "http://parsinger.ru/blank/1/6.html",
]

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)

    summa = 0
    for url in sites:
        browser.switch_to.new_window('tab')
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, 'input[type=checkbox]').click()
        res = browser.find_element(By.ID, 'result')
        summa +=  math.sqrt(int(res.text))

    print(f"{round(summa, 9)}")
