from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType



#definimos el proxy
PROXY = "http://103.129.119.229:21273"

prox = Proxy()

prox.proxy_type = ProxyType.MANUAL
#we set the flag autodetect to false so that we don't declare the world that we are using a manual proxy
prox.autodetect = False
capabilities = webdriver.DesiredCapabilities.CHROME
prox.http_proxy = PROXY
prox.ssl_proxy = PROXY
prox.add_to_capabilities(capabilities)


browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get('http://lumtest.com/myip.json')



