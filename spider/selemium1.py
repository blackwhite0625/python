from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# 開啟 Edge 視窗 open edge
driver = webdriver.Edge()

driver.implicitly_wait(0.5)

# 抓取網站 get web
driver.get("https://www.dcard.tw/f/")
title = driver.title
print(title)

#搜尋欄 search
# search = driver.find_element(By.NAME,"query")
# search.send_keys("亞東科技大學")
# search.send_keys(Keys.RETURN)

#搜尋欄按鈕 search buttom
# buttom = driver.find_element(By.CLASS_NAME,"atm_26_1urdtyr atm_3f_1i26tc atm_9s_1txwivl atm_h_1h6ojuz atm_5j_9j92nk atm_l8_g9u13n atm_9j_tlke0l atm_kd_glywfm bq7k6dg")
# buttom.click()
# time.sleep(5)

#標題 title
titles = driver.find_elements(By.CLASS_NAME,"atm_cs_1hcvtr6 atm_c8_1csq7v7 atm_g3_1qqjw7d atm_7l_1pday2 atm_1938jqx_1yyfdc7 atm_2zt8x3_stnw88 atm_grwvqw_gknzbh atm_1ymp90q_idpfg4 atm_89ifzh_idpfg4 atm_1hh4tvs_1osqo2v atm_1054lsl_1osqo2v t1gihpsa")
for a in titles:
    print(a.text)

# xx秒後關閉 xx sec stop
# time.sleep(30)
# driver.quit()

