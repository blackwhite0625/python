#boolean if 布林值if
pop = True
if pop:
    print("啟動")
else:
    print("未啟動")
    
#年齡判斷 if else elif
age = int(input("你的年齡:"))
if age >= 65:
    print("你超過使用年齡")
elif age >= 18:
    print("你滿18了")
else:
    print("你未滿18")
    
#簡易計算機
import math

op = input("輸入運算符(+,-,*,/):") 
num1 = float(input("輸入一個數:"))
num2 = float(input("輸入一個數:"))

if op == "+":
    numx = num1+num2
    
elif op == "-":
    numx = num1+num2
    
elif op == "*":
    numx = num1*num2
    
elif op == "/":
    numx = num1/num2
    
else:
    print("無效")

print("答案是:",math.floor(numx))

