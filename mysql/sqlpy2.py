import mysql.connector

#建立一個連接物件，傳入主機名、埠號、使用者名稱、密碼和資料庫名稱
connet = mysql.connector.connect(host='127.0.0.1',port='3306',user='root',password='yahoo2209',database='jobroom')

#建立一個游標物件，用於執行SQL語句
job = connet.cursor()

#執行一個查詢語句，從branch表中選擇所有的資料
job.execute('select * from `branch`;')

#將查詢結果存入一個變數data，data是一個列表，每個元素是一個元組，代表一筆資料
data = job.fetchall()
#用一個迴圈來遍歷data，並將每個元素印出
for i in data:
    print(i)


#新增資料
#job.execute("insert into `company` values (107, '曹子垂', '2004-11-11', '男', 28000, 4, NULL);")
#修改資料
#job.execute('update `branch` set `manager_id` = 107 where `branch_id`=4')

#關閉游標物件
job.close()
#提交資料，將對資料庫的修改保存
connet.commit() #提交資料
#關閉連接物件
connet.close()
