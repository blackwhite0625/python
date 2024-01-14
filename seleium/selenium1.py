from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service()
#抓取driver
driver = webdriver.Chrome(service=service)
#視窗最大化
driver.maximize_window()
#開啟網站 
#driver.get("https://www.aeust.edu.tw/")
#leep(1)
driver.get("https://portal.aeust.edu.tw/")
#返回
driver.back()
sleep(1)
#前進
driver.forward()
sleep(1)
#刷新
driver.refresh()
#關閉
driver.quit()