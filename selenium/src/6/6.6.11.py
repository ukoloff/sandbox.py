#
# https://stepik.org/lesson/732063/step/11?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/methods/3/index.html")

    summa = 0
    for c in browser.get_cookies():
        if not c['name'].startswith('secret_cookie_'):
            continue
        summa += int(c['value'])
    print(summa)
