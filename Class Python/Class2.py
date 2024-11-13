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
