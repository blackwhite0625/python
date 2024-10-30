import random 

# 計算 a 的 b 次方
def Square():
    
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a,"Square:",a**b)
    # (+)不會有空格 (,)有空格 
    print(str(a)+" Square:"+str(a**b))
    # float 浮點數(小數)

# 計算從 1 到 c 的總和
def Sum():
    
    c = int(input("Enter c:"))
    c = ((c+1)*c/2)
    print(f"1+..100:{c:.0f}")
    d = ((100+1)*100/2)
    print(f"1+..100:{d:.0f}")
    e = sum(range(1,101))
    print(e)

# 交換 f 和 g 的值
def Swap():
    
    f, g = 5, 6
    print("f:", f, "g:", g)
    f, g = g, f
    print("f:", f, "g:", g)

# 計算十年後的總金額
def TenYear():
    
    name = input("Please enter your name:")
    money = int(input("Enter your money:"))
    rate = float(input("Enter your rate:"))
    year = int(input("Enter year:"))
    total = money * ((1 + rate) ** year)
    print(name[0], "Sir/Women Hello")
    print(f"Ten Year:{total:.0f}")

# 計算加分後的成績
def Score():
    
    Score = int(input("Enter your score:"))
    Score += 10
    if Score >= 60:
        print("Pass! Your score:", Score)
    else:
        print("Unpass! Your score:", Score)

# 比較兩個數字的大小
def Max():
    num1 = int(input("Input one number:"))
    num2 = int(input("Input two number:"))
    if num1 > num2:
        print(f"Max One:{num1:.0f}")
    else:
        print(f"Max Two:{num2:.0f}")

# 比較三個數字的大小
def MaxThree():
    num3 = int(input("Input three number:"))
    num4 = int(input("Input four number:"))
    num5 = int(input("Input five number:"))
    if num3 >= num4 and num3 >= num5:
        print(f"Max Three:{num3:.0f}")
    elif num4 >= num3 and num4 >= num5:
        print(f"Max Four:{num4:.0f}")
    else:
        print(f"Max Five:{num5:.0f}")

# 找出兩個數字中的最大值
def MaxTwo():
    num1 = int(input("Input one number:"))
    num2 = int(input("Input two number:"))
    max1 = max(num1, num2)
    print("Max:", max1)

# 找出三個數字中的最大值
def MaxThreenum():
    num3 = int(input("Input three number:"))
    num4 = int(input("Input four number:"))
    num5 = int(input("Input five number:"))
    max2 = max(num3, num4, num5)
    print("Max:", max2)

# 找出三個數字中的最大值（使用條件判斷）
def MaxMer():
    a = int(input("Input a number:"))
    b = int(input("Input b number:"))
    c = int(input("Input c number:"))
    x = a
    if b > x:
        x = b
    if c > x:
        x = c
    print("Max:", x)

# 計算票價
def PriceDollar():
    price = 500
    age = int(input("Input a age:"))
    if age < 10 or age >= 70:
        price = int(price / 2)
    print("Your Price:", price, "Dollar")  

# 猜數字遊戲
def GuessNum():
    guess = 18
    nug = int(input("Input your num:"))
    if nug == guess:
        print("You're great")
    else:
        print("you're shit")

# 根據年齡決定可觀看的影片等級
def Level():
    age = int(input("Input a age:"))
    level = "普遍級"
    if age >= 18:
        level = "限制級 輔導級 保護級 普遍級"
    elif age >= 12:
        level = "輔導級 保護級 普遍級"
    elif age >= 6:
        level = "保護級 普遍級"
    else:
        level = "普遍級"
    print("Your age is:", age, ", So the levels you can watch are:", level)

# 計算 BMI
def Bmi():
    Height = int(input("Input a Height:"))
    weight = int(input("Input a weight:"))
    bmi = weight / ((Height / 100) ** 2)
    if bmi < 18.5:
        print("Your bmi Underweight")
    elif bmi >= 24 and bmi < 27:
        print("Your bmi overweight")
    elif bmi >= 27 and bmi < 30:
        print("Your bmi Mild obesity")
    elif bmi >= 30 and bmi < 35:
        print("Your bmi Moderately obese")
    elif bmi >= 18.5 and bmi <= 24:
        print("Your bmi Normal")
    else:
        print("Severe obesity")

# 數字與文本的運算
def TextNum():
    
    a = int(input("Enter int A:"))
    b = int(input("Enter int B:"))
    c = str(input("Enter Text c:"))
    if a >= 10:
        b = 3
    print(type(a), type(c))
    print("int A + int B:", a + b)
    print("Text B + int C:", str(b) + c)
    print("Text A + int B:", str(a) + str(b))

# 計算成績的平均值
def ScoreClass():
    
    Name = input("Enter your name:")
    print("Hello", Name)
    Chinese = int(input("Enter Chinese:"))
    Math = int(input("Enter Math:"))
    English = int(input("Enter English:"))
    Average1 = (Math + English + Chinese) / 3
    print("Chinese:", Chinese, "English:", English, "Math:", Math)
    print("Average:", int(Average1))

# 計算 1^2 + 2^2 + ... + n^2
def sum1002():
    a = int(input("Enter a:"))
    s = 0
    for i in range(1, a + 1):
        s += (i ** 2)
    print(s)

# 計算 1 + 2 + ... + n
def sum100():
    a = int(input("Enter a:"))
    s = 0
    for i in range(1, a + 1):
        s += i
    print(s)

def while100():
    # 使用 while 循環計算 1 + 2 + ... + n
    a = int(input("Enter a:"))
    s = 0
    i = 1
    while i <= a:
        s += i
        i += 1
    print(s)

# 直到總和超過 100
def onewhilebil():
    s = 0
    i = 1
    while s <= 100:
        s += i
        i += 1
    print(i - 1)

# 使用 continue 跳過某些值
def forcontinue():
    for i in range(10):
        if i == 5:
            continue
        print(i)

# 使用 break 結束循環
def forbreak():
    for i in range(10):
        if i == 5:
            break
        print(i)

# 輸入數字並過濾
def inputcontinuenum():
    s = input("Enter a text:")
    for ch in s:
        if ch > "9" or ch < "0":
            continue
        print(ch, end="")
    print()

# 輸入文本並過濾數字
def inputcontinuetext():
    s = input("Enter a text：")
    for ch in s:
        if ch >= "0" and ch <= "9":
            continue
        print(ch, end="")
    print()

# 密碼驗證
def inputmi():
    i = 0
    while i < 5:
        a = input("Enter your password:")
        if a == "you":
            print("yes")
            break
        else:
            print("no")
            i += 1
        if i == 5:
            print("get out")

# 猜數字遊戲
def guessnumbergame():
    i = 42 
    a = 0
    while True:
        guess = int(input("Guess your number："))
        a += 1
        if guess < i:
            print("錯了繼續")
        elif guess > i:
            print("錯了繼續")
        else:
            print("yes")
            break

# 隨機猜數字遊戲
def randomgame():
    i = random.randint(1, 100)
    a = 0
    while True:
        guess = int(input("Guess your number："))
        a += 1
        if guess < i:
            print("再大一點")
        elif guess > i:
            print("再小一點")
        else:
            print("yes")
            break

# 隨機範圍生成數字
def randomrange():
    numbers = random.sample(range(1, 50), 6)
    print(numbers)

# 考試print1
def testprint1():
    r = 6.4
    PI = 3.14
    # 輸出圓的半徑
    print("半徑", r)
    # 計算並輸出圓的面積
    print("面積", PI * r ** 2, end="")
    # 計算並輸出圓的周長
    print("周長", PI * r * 2)
    # 計算並輸出圓的體積
    print("體積", PI * r ** 3 * 4/3)

    a = 1
    b = 5.3
    # 輸出變數 a 和 b 的值
    print(a, b)
    # 使用格式化輸出整數 a 和浮點數 b
    print("%d %f" % (a, b))
    # 格式化輸出整數 a 和保留一位小數的 b
    print("%d %.1f" % (a, b))
    # 格式化輸出整數 a 和保留兩位小數的 b
    print("%d %3.2f" % (a, b))
    # 輸出 a 的值並換行
    print(a, "\n")
    # 輸出 b 的值
    print(b)

    # 輸入用戶名稱
    username = input("name:")
    # 輸入用戶年齡並轉換為整數
    agee = int(input("age:"))
    # 格式化輸出用戶名稱和年齡
    print("name:%s\tage:%d" % (username, agee))

    s1 = 'WTF'
    s2 = 3290
    # 格式化輸出項目名稱 s1 和金額 s2
    print("項目:{0} 金額:{1}".format(s1, s2))

    str1 = "OPOOOD"
    num1 = 18
    # 格式化輸出字符串 str1 和整數 num1
    print("I'm{name}I'm{age}".format(name=str1, age=num1))

# 考試print2
def testprint2():
    u = int(input("輸入u:"))
    f = int(input("輸入f:"))
    tt = u * f + u

    def mux(num1,num2):
        num3 = num1 * num2 + num1
        return num3
    print(mux(5,4))
    print(mux(u,f))
    print(mux(f,u))

testprint2()