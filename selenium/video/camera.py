import os
import time
import traceback
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

def camera(browser, ip):
    browser.get(f"http://{ip}")

    u = browser.find_elements(By.ID, "login_user")
    if not len(u):
       print("Неподдерживаемая форма авторизации")
       return
    u = u[0]
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
    h264 = 'H.264'
    if not len([1 for o in s.options if o.text == h264]):
       print(f"Вариант {h264} недоступен")
       return
    s.select_by_visible_text(h264)

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

with webdriver.Firefox(options=options) as browser:
    browser.implicitly_wait(5)

    try:
      camera(browser, "192.168.0.19")
    except Exception as e:
      pos = [z for z in traceback.extract_tb(e.__traceback__) if z.filename == __file__][-1]
      print(f"Ошибка в строке {pos.lineno}: {pos._lines.strip()}")

    print("That's all folks!")
