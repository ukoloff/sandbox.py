#
# https://stepik.org/lesson/732063/step/10?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/5.5/5/1.html")

    for d in browser.find_elements(By.CSS_SELECTOR, "#main-container>div"):
        color = d.find_element(By.CSS_SELECTOR, ':scope > span').text
        sel = Select(d.find_element(By.TAG_NAME, 'select'))
        sel.select_by_value(color)
        d.find_element(By.CSS_SELECTOR, f"button[data-hex=\\{color}]").click()
        d.find_element(By.CSS_SELECTOR, 'input[type=checkbox]').click()
        inp = d.find_element(By.CSS_SELECTOR, 'input[type=text]')
        inp.clear()
        inp.send_keys(color)
        d.find_element(By.CSS_SELECTOR, ':scope > button').click()

    browser.find_element(By.CSS_SELECTOR, 'body > button').click()
    ans = browser.switch_to.alert.text
    print(ans)
