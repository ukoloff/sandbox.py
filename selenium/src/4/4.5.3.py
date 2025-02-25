#
# https://stepik.org/lesson/731861/step/3?unit=733396
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/selenium/3/3.html")

    sum = 0

    pz = browser.find_elements(By.TAG_NAME, "p")
    for p in pz:
        sum += int(p.text)

    print(sum)
