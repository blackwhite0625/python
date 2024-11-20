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
    
    # 九九乘法表
    for i in range(1, 10):  
        for j in range(1, i + 1):  
            print(f"{j} x {i} = {i * j:2}", end="  ") 
        print()  

    # **行數
    rows = int(input("請輸入需要的行數: "))
    for i in range(1, rows + 1): 
        print("*" * i)  

        
textf()