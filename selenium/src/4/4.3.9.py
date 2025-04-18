#
# https://stepik.org/lesson/1617754/step/9?unit=1639632
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/3/3.2.4/index.html")

    btn = browser.find_element(By.ID, "secret-key-button")
    btn.click()
    txt = btn.get_attribute("data")

    print(txt)
    print(
        f"""
    Введите_ключ = "{txt}"
    """.strip()
    )
