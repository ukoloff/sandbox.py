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
    browser.get("https://parsinger.ru/selenium/5.5/4/1.html")

    for d in browser.find_elements(By.CLASS_NAME, "parent"):
        tas = d.find_elements(By.TAG_NAME, "textarea")
        tas[1].clear()
        tas[1].send_keys(tas[0].text)
        tas[0].clear()
        d.find_element(By.TAG_NAME, 'button').click()
    browser.find_element(By.ID, 'checkAll').click()
    ans = browser.find_element(By.ID, 'congrats').text
    print(ans)
