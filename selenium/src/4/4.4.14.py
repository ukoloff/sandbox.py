#
# https://stepik.org/lesson/1617768/step/14?unit=1639646
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/3/3.3.3/index.html")

    count = 0

    az = browser.find_elements(By.TAG_NAME, "a")
    for z in az:
        n = z.get_attribute('stormtrooper')
        if n.isnumeric():
            count += int(n)
    ino = browser.find_element(By.TAG_NAME, 'input')
    ino.clear()
    ino.send_keys(str(count))

    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()

    out = browser.find_element(By.ID, "feedbackMessage")
    txt = out.text

    print(txt)
    print(
        f"""
    пароль = "{txt}"
    """.strip()
    )
