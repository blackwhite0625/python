import time

#碼表
#timer01
tim = int(input("sec:"))
for b in range(tim):
    print(b)
    time.sleep(1)
print("time stop")

#timer02 
ttime = int(input("sec:"))
for a in range(ttime,0,-1):
    sec = a % 60 
    min = a // 60 % 60
    print(f"{min:02}:{sec:02}")
    time.sleep(1)
print("time stop")