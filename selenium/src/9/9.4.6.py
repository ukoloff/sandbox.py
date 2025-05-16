#
# https://stepik.org/lesson/1121330/step/6?unit=1132818
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(1)
    browser.get("http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html")

    while 'qLChv49' not in browser.current_url:
      browser.find_element(By.CSS_SELECTOR, 'a').click()
      sleep(0.3)

    browser.find_element(By.TAG_NAME, "button").click()

    ans = browser.find_element(By.ID, "result")
    print(ans.text)
