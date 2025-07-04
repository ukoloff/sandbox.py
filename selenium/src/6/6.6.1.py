#
# https://stepik.org/lesson/732063/step/1?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/methods/1/index.html")

    while True:
      i = browser.find_element(By.ID, "result").text
      if i.isnumeric():
         print(i)
         break
      browser.refresh()
