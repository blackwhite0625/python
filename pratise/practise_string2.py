#index 字串分析
email = "practise@gamil.com"
emailindex = email.index("@")
print(email[(emailindex+1):])
print(email[:emailindex])

#f-string格式化
#小數點精確度
pop1 = 32
pop2 = 59.332
pop3 = 62.29
print(f"數字1:{pop1:.2f}\n"
      f"數字2:{pop2:.2f}\n"
      f"數字3:{pop3:.2f}\n" )

#加上正負
print(f"數字1:{pop1:+.2f}\n"
      f"數字2:{pop2:+.2f}\n"
      f"數字3:{pop3:+.2f}\n" )      

#對齊符號 < > ^
print(f"數字1:{pop1:^10.2f}\n"
      f"數字2:{pop2:>10.2f}\n"
      f"數字3:{pop3:<10.2f}\n" )      

