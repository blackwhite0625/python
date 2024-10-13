#if two
# num1 = int(input("Input one number:"))
# num2 = int(input("Input two number:"))
# if num1 > num2:
#     print(f"Max One:{num1:.0f}")
# else:
#     print(f"Max Two:{num2:.0f}")

# #if three
# num3 = int(input("Input three number:"))
# num4 = int(input("Input four number:"))
# num5 = int(input("Input five number:"))
# if num3 >= num4 and num3 >= num5:
#     print(f"Max Three:{num3:.0f}")
# elif num4 >= num3 and num4 >= num5:
#     print(f"Max Four:{num4:.0f}")
# else:
#     print(f"Max Five:{num5:.0f}")

# #max two
# num1 = int(input("Input one number:"))
# num2 = int(input("Input two number:"))
# max1 = max(num1, num2)
# # print(f"Max:{max1:.0f}")
# print("Max:",max1)

# #max three
# num3 = int(input("Input three number:"))
# num4 = int(input("Input four number:"))
# num5 = int(input("Input five number:"))
# max2 = max(num3, num4, num5)
# #print(f"Max:{max2:.0f}")
# print("Max:",max2)

# #Max mer
# a = int(input("Input a number:"))
# b = int(input("Input b number:"))
# c = int(input("Input b number:"))
# x = a
# if b > x:
#     x = b
# if c > x:
#     x = c
# print("Max:",x)

# #price dollar
# price = 500
# age = int(input("Input a age:"))
# if age < 10 or age >= 70:
#     price = int(price/2)
# print("Your Price:",price,"Dollar")

# #guess num
# guess = 18
# nug = int(input("Input your num:"))
# if nug == guess:
#     print("Youre great")
# else:
#     print("youre shit")

# #level
# age = int(input("Input a age:"))
# level = "普遍級"
# if age >= 18:
#     level = "限制級"" 輔導級"" 保護級"" 普遍級"
# elif age >= 12:
#     level = "輔導級"" 保護級"" 普遍級"
# elif age >= 6:
#     level = "保護級"" 普遍級"
# else:
#     level = "普遍級"
# print("Your age is:",age,",So the levels you can watch are:",level)

#bmi
Height = int(input("Input a Height:"))
weight = int(input("Input a weight"))
bmi = weight/((Height/100)**2)
if bmi < 18.5:
    print("Your bmi Underweight")
elif bmi >= 24 and bmi < 27:
    print("Your bmi overweight")
elif bmi >= 27 and bmi < 30:
    print("Your bmi Mild obesity")
elif bmi >= 30 and bmi < 25:
    print("Your bmi Moderately obese")
elif bmi >= 18.5 and bmi > 24:
    print("Your bmi Normal")
else:
    print("Severe obesity")