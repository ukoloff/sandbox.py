#
# https://stepik.org/lesson/1617754/step/7?unit=1639632
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/3/3.2.3/index.html")


    btn = browser.find_element(By.ID, "showTextBtn")
    btn.click()

    out = browser.find_element(By.ID, "text1")
    psw = out.text

    inp = browser.find_element(By.ID, "userInput")
    inp.clear()
    inp.send_keys(psw)

    btn = browser.find_element(By.ID, "checkBtn")
    btn.click()

    out = browser.find_element(By.ID, "text2")
    txt = out.text
    print(txt)
    print(
        f"""
    Введите_ключ = "{txt}"
    """.strip()
    )
