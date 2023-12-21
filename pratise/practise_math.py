import math
pop = 5
pop1 = 3.6
pop2 = -9
pop = pop - 1
pop **= 2
pop1 /= 0.8

print(pop)
#max與min 最大最小
print("取最大值1:",max(5,2))
print("取最小值1:",min(5,2))
print("取最大值2:",max(pop,pop1))
print("取最小值2:",min(pop,pop1))

#pow 次方
print("次方1:",pow(3,2))
print("次方2:",pow(pop,pop1))

#round 四捨五入
print("四捨五入1:",round(pop1))
print("四捨五入2:",round(5.7))

#abs 絕對值
print("絕對值1:",abs(-2))
print("絕對值2:",abs(pop2))

#math_ceil and floor 無條件進位與無條件捨去
print("無條件進位1:",math.ceil(pop1))
print("無條件捨去1:",math.floor(pop1))
print("無條件進位2:",math.ceil(12.34))
print("無條件捨去2:",math.floor(12.34))

#圓周率 圓周長 圓面積
print("圓周率:",math.pi)

radius = float(input("輸入半徑:"))
co = 2 * math.pi * radius
print("周長為:",round(co,4))

co1 = math.pi * (radius ** 2)
print("面積為:",round(co1,3))