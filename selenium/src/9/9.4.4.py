#
# https://stepik.org/lesson/1121330/step/4?unit=1132818
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
    browser.get("https://parsinger.ru/selenium/9/9.4.3/index.html")

    browser.find_elements(By.CSS_SELECTOR, 'a.btn')[-1].click()

    WebDriverWait(browser, 10).until(EC.url_contains('key=secure'))

      # browser.find_element(By.ID, 'dynamicButton').click()

    ans = browser.find_element(By.ID, "password")
    print(ans.text)
