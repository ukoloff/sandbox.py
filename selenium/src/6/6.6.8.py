#
# https://stepik.org/lesson/732063/step/8?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/5.5/3/1.html")

    summa = 0

    for d in browser.find_elements(By.CLASS_NAME, "parent"):
        cb = d.find_element(By.TAG_NAME, "input")
        if cb.is_selected():
            summa += int(d.find_element(By.TAG_NAME, "textarea").text)
    print(summa)
