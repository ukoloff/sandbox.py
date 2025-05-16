#
# https://stepik.org/lesson/732077/step/6?unit=733610
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/8/8.2.2/index.html")

    sz = browser.get_window_size()

    inp = browser.find_element(By.ID, 'answer')
    inp.clear()
    inp.send_keys(sz['width'] + sz['height'])

    browser.find_element(By.TAG_NAME, 'button').click()

    ans = browser.find_element(By.ID, 'resultMessage').text
    print(ans)
