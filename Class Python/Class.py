import random
def Square():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a,"Square:",a**b)
    #(+)不會有空格 (,)有空格 
    print(str(a)+" Square:"+str(a**b))
    #float 浮點數(小數)

def Sum():
    #1+...100
    c = int(input("Enter c:"))
    c = ((c+1)*c/2)
    print(f"1+..100:{c:.0f}")
    d = ((100+1)*100/2)
    print(f"1+..100:{d:.0f}")
    e = sum(range(1,101))
    print(e)

def Swap():
    f,g = 5,6
    print("f:",f,"g:",g)
    f,g = g,f
    print("f:",f,"g:",g)

def TenYear():
    name = input("Please enter your name:")
    money = int(input("Enter your money:"))
    rate = float(input("Enter your rate:"))
    year = int(input("Enter year:"))
    total = money * ((1+rate) ** year)
    name[0]#取第一字串
    print(name[0],"Sir/Women Hello")
    print(f"Ten Year:{total:.0f}")

def Score():
    Score = int(input("Enter your score:"))
    Score = Score + 10
    if Score >= 60:
        print("Pass! Your score:",Score)
    else:
        print("Unpass! Your score:",Score)

#if two
def Max():
    num1 = int(input("Input one number:"))
    num2 = int(input("Input two number:"))
    if num1 > num2:
        print(f"Max One:{num1:.0f}")
    else:
        print(f"Max Two:{num2:.0f}")

# #if three
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

#max two
def MaxTwo():
    num1 = int(input("Input one number:"))
    num2 = int(input("Input two number:"))
    max1 = max(num1, num2)
    # print(f"Max:{max1:.0f}")
    print("Max:",max1)
    
#max three
def MaxThreenum():
    num3 = int(input("Input three number:"))
    num4 = int(input("Input four number:"))
    num5 = int(input("Input five number:"))
    max2 = max(num3, num4, num5)
    #print(f"Max:{max2:.0f}")
    print("Max:",max2)

# #Max mer
def MaxMer():
    a = int(input("Input a number:"))
    b = int(input("Input b number:"))
    c = int(input("Input b number:"))
    x = a
    if b > x:
        x = b
    if c > x:
        x = c
    print("Max:",x)

#price dollar
def PriceDollar():
    price = 500
    age = int(input("Input a age:"))
    if age < 10 or age >= 70:
        price = int(price/2)
    print("Your Price:",price,"Dollar")  

#guess num
def GuessNum():
    guess = 18
    nug = int(input("Input your num:"))
    if nug == guess:
        print("Youre great")
    else:
        print("youre shit")

#level
def Level():
    age = int(input("Input a age:"))
    level = "普遍級"
    if age >= 18:
        level = "限制級"" 輔導級"" 保護級"" 普遍級"
    elif age >= 12:
        level = "輔導級"" 保護級"" 普遍級"
    elif age >= 6:
        level = "保護級"" 普遍級"
    else:
        level = "普遍級"
    print("Your age is:",age,",So the levels you can watch are:",level)

#bmi
def Bmi():
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

def TextNum():
    a = int(input("Enter int A:"))
    b = int(input("Enter int B:"))
    c = str(input("Enter Text c:"))
    if a >= 10 :
        b = 3
    else :
        b = b
    print(type(a),type(c))
    print("int A + int B:",a+b)
    print("Text B + int C:",str(b)+c)
    #print(a/int(c)*b)
    print("Text A + int B:",str(a)+str(b))

def ScoreClass():
    Name=input("Enter your name:")
    print("Hello",Name)
    #Square = 55 ** 2
    #print("Square:",Square)
    Chinese = int(input("Enter Chiners:"))
    Math = int(input("Enter Math:"))
    English = int(input("Enter English:"))
    Average1 = (Math+English+Chinese)/3
    print("Chinese:",Chinese,"English:",English,"Math:",Math)
    # sep='\n' #分隔符
    # end=''#結尾符
    print ("Average:",int(Average1))

#1^2 + 2^2 + ... + n^2
def sum1002():
    a = int(input("Enter a:"))
    s = 0
    for i in range(1,a+1):
        s = s + (i**2)
    print(s)


#1 + 2 + ... + n
def sum100():
    a = int(input("Enter a:"))
    s = 0
    for i in range(1,a+1):
        s = s + i
    print(s)

def while100():
    a = int(input("Enter a:"))
    s = 0
    i = 1
    while i <= a:
        s = s + i
        i = i + 1
    print(s)
    
#while 1+2+...+n <= 100
def onewhilebil():
    s = 0
    i = 1
    while s <= 100:
        s = s + i
        i = i + 1
    print(i - 1)

#continue
def forcontinue():
    for i in range(10):
        if i == 5:
            continue
        print(i)
#break
def forbreak():
    for i in range(10):
        if i == 5:
            break
        print(i)


#期中考會考
def inputcontinuenum():
    s = input("Enter a text:")
    for ch in s:
        if ch > "9" or ch < "0":
            continue
        print(ch,end="")
    print()

#inputcontinuenu
def inputcontinuetext():
    s = input("Enter a text：")
    for ch in s:
        if ch >= "0" and ch <= "9" :
            continue
        print(ch, end="")
    print()

#inputbreaktext()
def inputmi():
    i = 0
    while i < 5:
        a = input("Enter your password:")
        if a == "you":
            print("yes")
            break
        else:
            print("no")
            i = i + 1
        if i == 5:
            print("get out")


def guessnumbergame():
    i = 42 
    a = 0
    while True:
        guess = int(input("Guess your number："))
        a = a + 1
        if guess < i:
            print("錯了繼續")
        elif guess > i:
            print("錯了繼續")
        else:
            print("yes")
            break

def randomgame():
    i = random.randint(1,100)
    a = 0
    while True:
        guess = int(input("Guess your number："))
        a = a + 1
        if guess < i:
            print("再大一點")
        elif guess > i:
            print("再小一點")
        else:
            print("yes")
            break


def randomrange():
    random.sample(range(1, 50), 6)  
    numbers = randomrange()
    print(numbers)
randomrange()