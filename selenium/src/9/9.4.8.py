#
# https://stepik.org/lesson/1121330/step/8?unit=1132818
#
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.4.2/index.html")

    browser.find_element(By.TAG_NAME, "button").click()

    summa = 0
    while "index_2" not in browser.current_url:
        if re.search(r"[/]ok[/]ok_\d+[.]html$", browser.current_url):
            summa += int(browser.find_element(By.CLASS_NAME, "number").text)
        WebDriverWait(browser, 10).until(EC.url_changes(browser.current_url))

    ans = browser.find_element(By.ID, "sumInput")
    ans.clear()
    ans.send_keys(summa)
    browser.find_element(By.TAG_NAME, "button").click()

    ans = browser.find_element(By.CSS_SELECTOR, ".success>p")
    print(ans.text)
