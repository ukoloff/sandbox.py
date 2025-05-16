#
# https://stepik.org/lesson/1121307/step/4?unit=1132795
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/8/8.4.1/")

    i = browser.find_element(By.TAG_NAME, "iframe")
    browser.switch_to.frame(i)
    txt = browser.page_source
    ans = ''.join(txt.split('*')[1::2])

    print(ans)
