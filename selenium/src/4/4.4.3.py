#
# https://stepik.org/lesson/1617754/step/9?unit=1639632
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/3/3.3.1/index.html")

    div = browser.find_element(By.ID, "parent_id")
    div = div.find_element(By.CLASS_NAME, 'child_class')
    div.click()

    txt = div.get_attribute("password")

    print(txt)
    print(
        f"""
    Введите_пароль = "{txt}"
    """.strip()
    )
