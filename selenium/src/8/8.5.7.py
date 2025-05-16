#
# https://stepik.org/lesson/732079/step/7?unit=733612
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("http://parsinger.ru/blank/3/index.html")
    for b in browser.find_elements(By.CLASS_NAME, 'buttons'):
        b.click()

    summa = 0
    for w in browser.window_handles[1:]:
        browser.switch_to.window(w)
        summa += int(browser.title)

    print(summa)
