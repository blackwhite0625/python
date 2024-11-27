#考試
import random
def nrange():
    for n in range(1,8,2):
        print(n,end='')
    print("n=",n)

def ran():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)

    i = a + b + c
    print(i)
    if i > 12:
        print("sum12")

#剪刀石頭布
def rock():
    while True:
        #剪刀1 石頭2 布3
        randoms = ["1","2","3"]
        
        rockrandom = random.choice(randoms)
  
        a = input("猜拳:")
        if a == rockrandom:
            print("平手")
        elif (a == "1" and rockrandom == "3")or(a == "2" and rockrandom == "1")or(a == "3" and rockrandom == "2"):
            print("你贏了 對手出的是:", rockrandom)
        else:
            print("你輸了廢物 對手出的是:",rockrandom)
        
        res =  input("是否要繼續:(輸入是否)")
        if res != "是":
            break
        else:
            continue


def textf():
    a = "aiopopu"
    b= a.find("io")
    print(b)
    
    c = "ieoskds"
    d = c.upper()
    print(d)
    
    for e in "sfgfdgf":
        print(e)
    for f in range(2,5):
        print(f)
    # **行數
    rows = int(input("請輸入需要的行數: "))
    for i in range(1, rows + 1): 
        print("*" * i)  

# *三角形
def forrange():
    a = int(input("請輸入需要的行數: "))
    for x in range(1,a):
        for j in range(1, a-x+1): 
            print("" ,end=" ")  
        for j in range(1, x+1): 
            print(" *" ,end="") 
        print()
    print()
def forrange1():
    rows = int(input("請輸入需要的行數: "))
    for j in range(1, rows + 1):  
        spaces = rows - j
        print(" " * spaces + " *" * j) 
    print()

def forrange2():
    for x in range(1,12):
        for y in range(1,11-x+1):
            print(" ",end="")
        for y in range(1,2*x-1+1):
            print("*",end="")
        print()
    print()



# 九九乘法表
def ninix():
    for i in range(1, 10):  
        for j in range(1, i + 1):  
            print(f"{j} x {i} = {i * j:2}", end="  ") 
        print()  
def ninix1():
    for i in range(10):
        if(i <= 0):
            continue
        j = 1
        while 1:
            print(i,"*",j,"=",i*j,end="\t")
            j = j + 1
            if(j > 9):
                break
        print()

def list1():
    lis1 = [1,2,"shit"]
    print(lis1[1:3])
    
    for i in lis1:
        print(i)
list1()