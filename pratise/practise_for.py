#for迴圈 固定次數
#in後面要接可迭代的物件
#reversed倒著

#for 1~10
for pop1 in range(1,10):
    print(pop1)

#for 10~1 倒數 reversed
for pop2 in reversed(range(1,10)):
    print(pop2)
print("成功")

#continue與break
pop3 = "109332-3232-434-32fre"
for x in pop3:
    if x == "2":
        #遇到2會繼續執行
        #continue 
        
        #遇到2不會再執行
        break 
    else:
        print(x)

#字典dictionary{} 鍵key跟值value
pop4 = {"sice":1,"tool":2,"break":3}
for y in pop4.items(): #使用items 可以在in前面迭代兩個變數
    print(y)


