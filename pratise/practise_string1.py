#查詢可使用的
#help(str)

#len 計算字元
pop1 = "comPuTer"
lenpop = len(pop1)
print("總共",lenpop,"個字元")

#.find 尋找字元在哪
pop2 = "com pu ter"
findpop = pop2.find("p")
print("第一個空格出現在第",findpop,"個字元")

#capitalize()第一改大寫 ,upper()全部大寫,lower()全部小寫 函數
pop_cap = pop1.capitalize()
print("第一改大寫:",pop_cap)
pop_upper = pop1.upper()
print("全部大寫",pop_upper)
pop_lower = pop1.lower()
print("全部小寫",pop_lower)

#count計算某字元出現次數
pop3 = "1002332032550"
pop_count = pop3.count("0")
print("共有",pop_count,"個0")

#replace取代
pop_replace = pop3.replace("0","9")
print("已把",pop3,"取代為",pop_replace)

#isalpha判斷全英文 數字
# username = input("輸入名稱:")
# if username.isalpha():
#     print("全部英文")
# elif " " in username:
#     print("不能包含空格")
# elif  not username.isalpha():
#     print("不能有數字")
# else:
#     print("沒有英文")

#字串索引
popq = "practise909"
popg = popq[4]
popf = popq[:5]
poph = popq[2:6]
popi = popq[-2]
popu = popq[:3]+popq[3:]
pops = popq[::2]
popa = popq[::-1]
print(popg,popf,poph,popi,popu,pops,popa)
