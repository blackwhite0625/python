import tkinter as tk
from tkinter import messagebox as msgbox

def tktk():
    data = " "
    total = 0
    for i in foodch:
        if foodch[i].get() == True:
            data += fooda[i] + ", "
            total += price[i]
    
    result = "{0}您好，你選購的餐點為{1}，總共{2}元".format(name.get(),data,total)
    msgbox.showinfo("點餐結果",result)
    
win = tk.Tk()
win.title("按鈕範例")
win.geometry("500x130")

name = tk.StringVar()

lblName = tk.Label(win,text="姓名",padx=10,pady=8)
lblName.grid(row=0,column=0)

txtName = tk.Entry(win,width=10,textvariable=name)
txtName.grid(row=0,column=1)

lblScore = tk.Label(win,text="餐點",padx=10,pady=8)
lblScore.grid(row=1,column=0)

foodch = {}
fooda = ['牛肉套餐','豬肉套餐',"雞腿套餐","鍵盤套餐","滑鼠套餐"]
price = [100,110,120,130,140]
for i in range(5):
    foodch[i] = tk.BooleanVar()
    tk.Checkbutton(win,text=fooda[i],variable=foodch[i]).grid(row=1,column=(1+i))
    
btn = tk.Button(win,text="確定",command=tktk)
btn.grid(row=2,column=0)
win.mainloop()