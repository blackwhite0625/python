#list[]
food = ["雞排","牛肉麵","麥當勞","炒飯","火鍋"]
for a in food:
    print(a)
#append element加入元素
food.append("牛排")
print(food)

#repeat append
food.append("牛肉麵")
food.append("牛肉麵")

#remove element刪除元素
food.remove("雞排")
print(food)

#count element計算出現幾次
print(food.count("牛肉麵"))

#reverce element倒轉列表
food.reverse()
print(food)

#set{} 不會產生重複元素e,每一種只會存在一個
drink_set = {"奶茶","紅茶","綠茶"}
#NO set add 
drink_set.add("奶茶")
drink_set.add("咖啡")
for d in drink_set:
    print(d,end=" ")
#檢測元素有沒有在set裡
if "紅茶" in drink_set:
    print("有")
if "可樂" in drink_set:
    print("有")
else:
    print("沒有")

#tuple() 元組
drinkandfood = ("奶茶","紅茶","紅茶","綠茶")
#count計算元素總數
total = drinkandfood.count("紅茶")
#index計算元素位置
total1 = drinkandfood.index("綠茶")
print(f"{total},{total1}")
