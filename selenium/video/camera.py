import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

env = dict(
    line.strip().split("=", 2) for line in open(os.path.join(__file__, "../.env"))
)

options = webdriver.FirefoxOptions()
options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.socks", "localhost")
options.set_preference("network.proxy.socks_port", 1080)
options.set_preference("network.proxy.socks_remote_dns", True)

with webdriver.Firefox(options=options) as browser:
    browser.implicitly_wait(5)

    browser.get("http://192.168.0.23")

    u = browser.find_element(By.ID, "login_user")
    u.clear()
    u.send_keys(env['USER'])
    p = browser.find_element(By.ID, "login_psw")
    p.clear()
    p.send_keys(env['PASS'])
    b = browser.find_element(By.LINK_TEXT, 'Вход')
    b.click()

    m = browser.find_element(By.CSS_SELECTOR, 'span[title=Настройки]')
    time.sleep(0.5)
    m.click()
    m = browser.find_element(By.CSS_SELECTOR, 'span[title=Видео]')
    time.sleep(0.5)
    m.click()

    s = browser.find_element(By.ID, "video_compression0")
    s = Select(s)
    s.select_by_visible_text('H.264')

    s = browser.find_element(By.ID, "video_sencode0")
    s = Select(s)
    s.select_by_visible_text('Выкл.')

    i = browser.find_element(By.ID, "video_gop0")
    i.clear()
    # i.send_keys('12')

    s = browser.find_element(By.ID, "video_compression1")
    s = Select(s)
    s.select_by_visible_text('H.264')

    i = browser.find_element(By.ID, "video_gop1")
    i.clear()
    # i.send_keys('12')

    b = browser.find_element(By.LINK_TEXT, 'Сохранить')
    b.click()

    bs = browser.find_elements(By.LINK_TEXT, 'OK')
    if len(bs):
        bs[0].click()

    print(browser)
