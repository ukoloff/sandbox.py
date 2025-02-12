#
# https://stepik.org/lesson/1617754/step/3?unit=1639632
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/3/3.2.1/index.html")

    btn = browser.find_element(By.ID, "clickButton")
    btn.click()

    out = browser.find_element(By.ID, "codeOutput")
    txt = out.text
    print(txt)
    print(
        f"""
    Введите_ключ = "{txt}"
    """.strip()
    )
