''' ESTE ESTÁ JALANDO BIEN PARA HACER UN REQUEST USANDO EL PROXY '''

import requests
from selenium import webdriver

proxies = {"http":"http://adrianguti37850:2mxt3n5spx@103.129.119.229:21273"}
#browser = webdriver.Chrome("/usr/local/bin/chromedriver")
r = requests.get("http://lumtest.com/myip.json", proxies=proxies)

#p = browser.get('http://lumtest.com/myip.json')


print(r.content)