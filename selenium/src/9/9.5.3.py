#
# https://stepik.org/lesson/1121331/step/3?unit=1132819
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.5.1/index.html")

    id = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "order-number")))
    print(id.text)
