from selenium import webdriver

options = webdriver.FirefoxOptions()
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', 'localhost')
options.set_preference('network.proxy.socks_port', 1080)
options.set_preference('network.proxy.socks_remote_dns', True)

with webdriver.Firefox(options=options) as browser:
  browser.implicitly_wait(5)

  browser.get("http://192.168.0.21")

  print(browser)
