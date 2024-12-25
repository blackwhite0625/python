#考試
import random
import random as R
import os

def nrange():
    """
    輸出從 1 開始到 7（不含）之間的所有奇數，並列印最終的 n 值。
    """
    for n in range(1,8,2):
        print(n,end='')
    print("n=",n)

def ran():
    """
    產生三個隨機數，計算其和，並判斷是否大於 12 進行不同的輸出。
    """
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)

    i = a + b + c
    print(i)
    if i > 12:
        print("sum12")

#剪刀石頭布
def rock():
    """
    實現一個簡單的剪刀石頭布遊戲，玩家與電腦進行對戰。
    """
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
    """
    示範字串查找、轉換大小寫以及輸出星號圖形。
    """
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
    """
    輸出倒金字塔形的星號圖案。
    """
    a = int(input("請輸入需要的行數: "))
    for x in range(1,a):
        for j in range(1, a-x+1): 
            print("" ,end=" ")  
        for j in range(1, x+1): 
            print(" *" ,end="") 
        print()
    print()
def forrange1():
    """
    輸出標準金字塔形的星號圖案。
    """
    rows = int(input("請輸入需要的行數: "))
    for j in range(1, rows + 1):  
        spaces = rows - j
        print(" " * spaces + " *" * j) 
    print()

def forrange2():
    """
    輸出完整金字塔的星號圖案。
    """
    for x in range(1,12):
        for y in range(1,11-x+1):
            print(" ",end="")
        for y in range(1,2*x-1+1):
            print("*",end="")
        print()
    print()

# 九九乘法表
def ninix():
    """
    輸出格式化的九九乘法表。
    """
    for i in range(1, 10):  
        for j in range(1, i + 1):  
            print(f"{j} x {i} = {i * j:2}", end="  ") 
        print()  

def ninix1():
    """
    使用 while 循環輸出九九乘法表。
    """
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
    """
    示範列表的切片操作與遍歷。
    """
    lis1 = [1,2,"shit"]
    print(lis1[1:3])
    
    for i in lis1:
        print(i)

def list2():
    """
    示範列表排序及解壓縮操作。
    """
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
    """
    操作與輸出多維列表。
    """
    lst = [[4,8,5,9],[13,16,19,15],[28,25,29,24]]
    print(lst)
    n1 = len(lst)
    print(lst[1])
    n2 = len(lst[1])
    print(lst[1][2])

def list4():
    """
    示範列表的淺拷貝與深拷貝的差異。
    """
    a = [1,2,3]
    b = a
    c = a[:]
    d = a[::-1]
    print(a,b,c,d,sep="\n")
    a[0]=4
    print(a,b,c,d,sep="\n")

def list5():
    """
    輸出多維列表的每個元素。
    """
    lst = [[4,8,5,9],[13,16,19,15],[28,25,29,24]]
    print("lst = ",end=" ")
    print(lst)
    for i in range(len(lst)):
        print()
        for j in range(len(lst[i])):
            print(f"lst{[i]}{[j]} = {lst[i][j]:2d}",end=" ")

def list6():
    """
    使用列表生成式創建多維列表。
    """
    A = [0 for x in range(2)]
    print(A)
    arr = [A for Y in range(4)]
    print(arr)

def scorelist():
    """
    計算並輸出每位學生的總分與各科平均分。
    """
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
    """
    生成一組不重複的隨機數，並輸出結果。
    """
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

def openfilee():
    """
    檢查檔案是否存在，讀取內容，追加新數據後重新讀取檔案。
    """
    fName="class.txt"
    if os.path.isfile(fName):
        fr=open(fName,"r")
        flist = fr.readlines()
        for i in flist:
            print(i.strip())
        fr.close()
    else:
        print(fName,"不存在")

    fa = open(fName,"a")
    fa.write("\n共偉文,87,87")
    fa.write("\n周瑜安,23,43")
    fa.flush()
    fa.close()
    
    if os.path.isfile(fName):
        fr=open(fName,"r")
        flist=fr.readlines()
        for i in flist:
            print(i.strip())
        fr.close()
    else:
        print(fName,"不存在")

