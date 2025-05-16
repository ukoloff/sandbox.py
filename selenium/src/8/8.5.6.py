#
# https://stepik.org/lesson/732079/step/6?unit=733612
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

options = Options()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get("http://parsinger.ru/window_size/2/index.html")
    browser.set_window_size(window_size_x[0], window_size_y[0])
    sleep(0.1)

    ans = browser.find_element(By.ID, "result")

    for w in window_size_x:
        for h in window_size_y:
            wh = browser.execute_script("return [innerWidth, innerHeight]")
            sz = browser.get_window_size()
            browser.set_window_size(sz["width"] - wh[0] + w, sz["height"] - wh[1] + h)
            sleep(0.1)
            wh = {
                "width": browser.execute_script("return innerWidth"),
                "height": browser.execute_script("return innerHeight"),
            }
            sz = browser.get_window_size()
            if ans.text.isnumeric():
                print(ans.text, wh, sz, sep="\t")
