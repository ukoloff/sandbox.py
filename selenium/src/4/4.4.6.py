#
# https://stepik.org/lesson/1617754/step/9?unit=1639632
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/3/3.3.2/index.html")

    blocks = browser.find_elements(By.CLASS_NAME, "block")
    for z in blocks:
        btn = z.find_element(By.TAG_NAME, 'button')
        btn.click()
    psw = browser.find_element(By.TAG_NAME, 'password')

    txt = psw.text

    print(txt)
    print(
        f"""
    Введите_пароль = "{txt}"
    """.strip()
    )
