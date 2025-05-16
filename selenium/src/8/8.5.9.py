#
# https://stepik.org/lesson/732079/step/9?unit=733612
#
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
    browser.get("https://parsinger.ru/selenium/5.8/5/index.html")

    inp = browser.find_element(By.ID, 'guessInput')
    chk = browser.find_element(By.ID, 'checkBtn')

    for frame in browser.find_elements(By.TAG_NAME, 'iframe'):
        browser.switch_to.frame(frame)
        browser.find_element(By.TAG_NAME, 'button').click()
        id = browser.find_element(By.ID, 'numberDisplay').text
        browser.switch_to.default_content()
        inp.clear()
        inp.send_keys(id)
        chk.click()
        try:
            ans = browser.switch_to.alert.text
            print(ans)
            break
        except Exception:
            pass
