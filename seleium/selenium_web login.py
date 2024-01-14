from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

service = Service()

driver = webdriver.Chrome(service = service)
#全螢幕
driver.maximize_window()
driver.get("https://portal.aeust.edu.tw/")

#刷新頁面
#driver.refresh()

print(driver.name) #瀏覽器名稱
print(driver.title) #網站標題
print(driver.current_url) #網站網址
print(driver.page_source) #網站屬性
print(driver.current_window_handle) #網站句柄
#取得網站元素(定位)
#填入文字 .send_keys()
idproject = driver.find_element(by=By.ID,value="LoginAccount").send_keys('112109229')
passproject = driver.find_element(by=By.ID,value="LoginPassword").send_keys('!yahoo2209')
#xpath定位div class
buttomproject = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div[3]').click()
buttomproject
#print(idproject)

sleep(5000)
driver.quit()