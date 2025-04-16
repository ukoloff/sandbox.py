import os
import time
import traceback
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

logfile = os.path.join(
    __file__, "../logs", f"camera-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
)
logfile = open(logfile, "w", encoding="utf-8")

env = dict(
    line.strip().split("=", 2) for line in open(os.path.join(__file__, "../.env"))
)

options = webdriver.FirefoxOptions()
options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.socks", "localhost")
options.set_preference("network.proxy.socks_port", 1080)
options.set_preference("network.proxy.socks_remote_dns", True)


def camera(browser, ip):
    def log(str):
        msg = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]<{ip}>\t{str}"
        print(msg)
        print(msg, file=logfile)

    log("Подключаемся...")
    try:
        try:
            browser.get(f"http://{ip}")
        except Exception:
            log("ERROR: Ошибка соединения")
            return

        log("Подключились")

        u = browser.find_elements(By.ID, "login_user")
        if not len(u):
            log("ERROR: Неподдерживаемая форма авторизации")
            return
        u = u[0]
        u.clear()
        u.send_keys(env["USER"])
        p = browser.find_element(By.ID, "login_psw")
        p.clear()
        p.send_keys(env["PASS"])
        b = browser.find_element(By.LINK_TEXT, "Вход")
        b.click()

        log("Открываю Настройки")

        m = browser.find_element(By.CSS_SELECTOR, "span[title=Настройки]")
        time.sleep(1)
        m.click()
        # browser.execute_script("arguments[0].click();", m)

        m = browser.find_element(By.CSS_SELECTOR, "span[title=Видео]")
        time.sleep(1)
        m.click()
        # browser.execute_script("arguments[0].click();", m)

        log("Меняю настройки")

        s = browser.find_element(By.ID, "video_compression0")
        s = Select(s)
        h264 = "H.264"
        if not len([1 for o in s.options if o.text == h264]):
            log(f"ERROR: Вариант {h264} недоступен")
            return
        s.select_by_visible_text(h264)

        s = browser.find_element(By.ID, "video_sencode0")
        s = Select(s)
        s.select_by_visible_text("Выкл.")

        i = browser.find_element(By.ID, "video_gop0")
        i.clear()
        # i.send_keys('12')

        s = browser.find_element(By.ID, "video_compression1")
        s = Select(s)
        s.select_by_visible_text("H.264")

        i = browser.find_element(By.ID, "video_gop1")
        i.clear()
        # i.send_keys('12')

        log("Сохраняю изменения")

        b = browser.find_element(By.LINK_TEXT, "Сохранить")
        b.click()

        bs = browser.find_elements(By.LINK_TEXT, "OK")
        if len(bs):
            log("Перезагрузка...")
            bs[0].click()
            time.sleep(1)

    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        pos = [z for z in tb if z.filename == __file__][-1]
        log(f"ERROR: Ошибка в строке {pos.lineno}: {pos._lines.strip()}")
    finally:
        log("Отключение")


with webdriver.Firefox(options=options) as browser:
    browser.maximize_window()
    browser.set_page_load_timeout(5)
    browser.implicitly_wait(5)

    camera(browser, "192.168.0.23")

    print("That's all folks!")
