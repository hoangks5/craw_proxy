from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType

chrome_path = r'.\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.set_window_size(width=1920,height=1080)
driver.get('https://free-proxy-list.net/#')
time.sleep(5)
a = ''
f = open('ip.txt','w')
try:
    for i in range(200):
        addres = '/html/body/section[1]/div/div[2]/div/table/tbody/tr['+str(i+1)+']/td[1]'
        addre = driver.find_element_by_xpath(addres).text
        ips = '/html/body/section[1]/div/div[2]/div/table/tbody/tr['+str(i+1)+']/td[2]'
        ip = driver.find_element_by_xpath(ips).text
        b = addre+':'+ip
        a = a +','+ b
except:
    pass
a = a[1:]
f.write(a)
f.close()