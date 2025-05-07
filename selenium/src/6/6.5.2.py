#
# https://stepik.org/lesson/732071/step/2?unit=733604
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/6/6.5/index.html")

    el = browser.find_element(By.ID, "target")
    browser.execute_script('arguments[0].scrollIntoView(true)', el)
    el.click()

    out = browser.find_element(By.ID, "secret-key")
    print(out.text)
