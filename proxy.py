''' ESTE NO ESTÁ JALANDO

BIEN

'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

from time import sleep


class Request:

    selenium_retries = 0
    def __init__(self, url):
        self.url = url

    def get_selenium_res(self, class_name):
        try:
            software_names = [SoftwareName.CHROME.value]
            operating_systems = [OperatingSystem.WINDOWS.value,
                                 OperatingSystem.LINUX.value]
            user_agent_rotator = UserAgent(software_names = software_names,
                                           operating_systems = operating_systems,
                                           limit = 100)

            user_agent = user_agent_rotator.get_random_user_agent()
            
            chrome_options = Options()
            chrome_options.add.argument("--headless")
            chrome_options.add.argument("--no-sandbox")
            chrome_options.add.argument("--window-size=1420,1080")
            chrome_options.add.argument("--disable-gpu")
            chrome_options.add.argument(f'user-agent={user_agent}')

            PROXY = "http://gate.smartproxy.com:7000"

            if not IS_GAE_PRODUCTION_ENV:
                chrome_options.binary_location = 'Applications/Google Chrome.app/Contents/MacOs/Google Chrome'

            prox = Proxy()
            prox.proxy_type = ProxyType.MANUAL
            prox.autodetect = False
            capabilities = webdriver.DesiredCapabilities.CHROME
            prox.http_proxy = PROXY
            prox.ssl_proxy = PROXY
            prox.add_to_capabilities(capabilities)

            # browser = webdriver.Chrome(chrome_options = chrome_options,
            #                            desired_capabilities=capabilities)
            browser = webdriver.Chrome(chrome_options=chrome_options)
        
            #when testing proxies
            browser.get('http://lumtest.com/myip.json')
            browser.get(self.url)
        except:
            print('fallido')

pedo = Request('www.facebook.com')
pedo.get_selenium_res('name_of_class')