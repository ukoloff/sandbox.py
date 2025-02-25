#
# https://stepik.org/lesson/731861/step/8?unit=733396
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/selenium/6/6.html")

    div = browser.find_element(By.ID, "text_box")
    res = eval(div.text)

    opz = browser.find_elements(By.TAG_NAME, "option")
    for z in opz:
        if z.text == str(res):
            z.click()

    btn = browser.find_element(By.ID, "sendbutton")
    btn.click()

    out = browser.find_element(By.ID, "result")
    txt = out.text

    print(txt)
