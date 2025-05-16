#
# https://stepik.org/lesson/732083/step/5?unit=733616
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

IDs = [
    "xhkVEkgm",
    "QCg2vOX7",
    "8KvuO5ja",
    "CFoCZ3Ze",
    "8CiPCnNB",
    "XuEMunrz",
    "vmlzQ3gH",
    "axhUiw2I",
    "jolHZqD1",
    "ZM6Ms3tw",
    "25a2X14r",
    "aOSMX9tb",
    "YySk7Ze3",
    "QQK13iyY",
    "j7kD7uIR",
]

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.9/3/index.html")

    for id in IDs:
        WebDriverWait(browser, 100).until(
            EC.visibility_of_element_located((By.ID, id))
        ).click()
    ans = browser.switch_to.alert.text
    print(ans)
