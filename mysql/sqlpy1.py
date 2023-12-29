import mysql.connector

connet = mysql.connector.connect(host='localhost',port=3306,user='root',password='yahoo2209')

test =connet.cursor()

#創建資料庫
#cursor.execute("create database `test`;")
#查看資料庫
#test.execute("show databases;")

# dataprint = test.fetchall()
# for i in dataprint:
#     print(i)
test.execute("use `test`;")
test.close()
connet.close()