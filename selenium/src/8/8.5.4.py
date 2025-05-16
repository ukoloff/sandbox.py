#
# https://stepik.org/lesson/732079/step/4?unit=733612
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

with webdriver.Chrome(options=options) as browser:
    browser.get("http://parsinger.ru/window_size/1/")

    wh = browser.execute_script("return [innerWidth, innerHeight]")
    sz = browser.get_window_size()
    browser.set_window_size(sz["width"] - wh[0] + 555, sz["height"] - wh[1] + 555)

    # inp = browser.find_element(By.ID, 'input')
    ans = browser.find_element(By.ID, "result")
    print(ans.text)
