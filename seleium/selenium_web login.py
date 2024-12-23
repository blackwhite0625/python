from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = Options()
edge_options.add_argument('--disable-gpu')
edge_options.add_argument('--no-sandbox')
edge_options.page_load_strategy = 'eager'

service = Service()
driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window()

try:
    driver.set_page_load_timeout(10)
    driver.get("https://portal.aeust.edu.tw/")
    
    wait = WebDriverWait(driver, 10)
    
    id_input = wait.until(EC.presence_of_element_located((By.ID, "LoginAccount")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "LoginPassword")))
    
    id_input.send_keys('學號')
    password_input.send_keys('密碼')
    
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div[3]')))
    button.click()

    input("按Enter鍵結束程式...")

except Exception as e:
    print(f"發生錯誤: {e}")
    input("按Enter鍵結束程式...")