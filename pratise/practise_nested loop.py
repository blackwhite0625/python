#巢狀迴圈
# for pop1 in range(1,11):
#     print(pop1,end=" ") #end=""print結果到同一行

for pop2 in range(10):
    for pop1 in range(1,11):
        print(pop1,end=" ") #end=""print結果到同一行
    print()
    
op = int(input("行數:"))
lis = int(input("列數:"))
ans = input("字:")
for a in range(op):
    for b in range(lis):
        print(ans,end=" ")
    print()