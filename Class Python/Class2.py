#考試
import random
import random as R
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


def list2():
    a = ["MAN","GIRL","JACK"]
    b = [90,78,89]

    zipped = zip(a,b)
    print(zipped)
    zipped_sort = sorted(zipped,key=lambda x:x[1],reverse=True)
    print(zipped_sort)
    print(*zipped_sort)
    a1,b1 = (list(t) for t in zip (*zipped_sort))
    print(a1)
    print(b1)

def list3():
    lst = [[4,8,5,9],[13,16,19,15],[28,25,29,24]]
    print(lst)
    n1 = len(lst)
    print(lst[1])
    n2 = len(lst[1])
    print(lst[1][2])

def list4():
    a = [1,2,3]
    b = a
    c = a[:]
    d = a[::-1]
    print(a,b,c,d,sep="\n")
    a[0]=4
    print(a,b,c,d,sep="\n")

def list5():
    lst = [[4,8,5,9],[13,16,19,15],[28,25,29,24]]
    print("lst = ",end=" ")
    print(lst)
    for i in range(len(lst)):
        print()
        for j in range(len(lst[i])):
            print(f"lst{[i]}{[j]} = {lst[i][j]:2d}",end=" ")

def list6():
    A = [0 for x in range(2)]
    print(A)
    arr = [A for Y in range(4)]
    print(arr)


def scorelist():
    no = [1,2,3,4]
    score = [[87,64,88],[93,72,86],[80,88,89],[79,91,90]]  
    print("編號 語文 數理 智力 總分")
    print("=========================")
    for i in range(len(no)):
        print(f"{no[i]:2d}",end="   ")
        hSum = 0
        for j in range(len(score[i])):
            print(f"{score[i][j]:3d}",end="  ")  
            hSum += score[i][j]
        print(f"{hSum:3d}")
        
    print("平均",end=" ")
    for j in range(3):
        vSum = 0
        for i in range(len(no)):
            vSum += score[i][j]
        print(f"{vSum/len(no):4.1f}",end="  ")
     
def randint2():
    max = 35
    min = 18
    num = 6
    arr = [0 for x in range(num)]
    n = 0
    while (n < num):
        isRepeat = False
        rnd = R.randint(min,max)
        for v in arr:
            if rnd == v:
                isRepeat = True
        if not isRepeat:
            arr[n] = rnd
            n += 1
    for i in range(num):
        print(f"第{i+1}個亂數:{arr[i]}")
randint2()