#a = int(input("Enter a:"))
#b = int(input("Enter b:"))
#print(a,"Square:",a**b)
#(+)不會有空格 (,)有空格 
#print(str(a)+" Square:"+str(a**b))
#float 浮點數(小數)

#1+...100
# c = int(input("Enter c:"))
# c = ((c+1)*c/2)
# print(f"1+..100:{c:.0f}")
# d = ((100+1)*100/2)
# print(f"1+..100:{d:.0f}")
# e = sum(range(1,101))
# print(e)

# f,g = 5,6
# print("f:",f,"g:",g)
# f,g = g,f
# print("f:",f,"g:",g)

# name = input("Please enter your name:")
# money = int(input("Enter your money:"))
# rate = float(input("Enter your rate:"))
# year = int(input("Enter year:"))
# total = money * ((1+rate) ** year)
# name[0]取第一字串
# print(name[0],"Sir/Women Hello")
# print(f"Ten Year:{total:.0f}")

Score = int(input("Enter your score:"))
Score = Score + 10
if Score >= 60:
    print("Pass! Your score:",Score)
else:
    print("Unpass! Your score:",Score)