#
# https://stepik.org/lesson/732077/step/4?unit=733610
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/8/8.2.1/index.html")

    browser.set_window_size(1200, 720)

    browser.find_element(By.TAG_NAME, 'button').click()

    ans = browser.find_element(By.ID, 'secret').text
    print(ans)
