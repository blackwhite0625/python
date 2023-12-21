#while基礎用法
# pop = ""
# while pop == "":
#     pop = input("輸入:")
# print(pop)

#while不等於!=
# pop = input("輸入:")
# while pop != " ":
#     print(pop)
#     pop = input("輸入:")
# print("無")

#while < or > 判斷
pop1 = int(input("輸入數字:"))
while pop1 < 1 or pop1 > 25:
    print(f"數字{pop1}無效")
    pop1 = int(input("輸入數字:"))
print(pop1)

#重點:while迴圈可以驗證使用者輸入是否有效