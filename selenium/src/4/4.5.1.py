#
# https://stepik.org/lesson/731861/step/1?unit=733396
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/selenium/1/1.html")

    iz = browser.find_elements(By.CSS_SELECTOR, "input[type=text]")
    for z in iz:
        z.clear()
        z.send_keys('Текст')

    btn = browser.find_element(By.CSS_SELECTOR, "input[type=button]")
    btn.click()

    out = browser.find_element(By.ID, "result")
    txt = out.text

    print(txt)
