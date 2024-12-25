import tkinter as tk

def tktk():
    vName = name.get()
    vScore = score.get()
    if vScore >=90 :
        level = "A"
    elif vScore >= 80:
        level = "B"
    elif vScore >= 70:
        level = "C"
    elif vScore >= 65:
        level = "D"
    else:
        level = "F"
    lblResult["text"] = "{0}成績是{1},等級是{2}".format(vName,vScore,level)
    

win = tk.Tk()
win.title("按鈕範例")
win.geometry("200x120")

name = tk.StringVar()
score = tk.IntVar()

lblName = tk.Label(win,text="姓名",padx=10,pady=8)
lblName.grid(row=0,column=0)

txtName = tk.Entry(win,width=15,textvariable=name)
txtName.grid(row=0,column=1)

lblScore = tk.Label(win,text="分數",padx=10,pady=8)
lblScore.grid(row=1,column=0)

txtScore = tk.Entry(win,width=15,textvariable=score)
txtScore.grid(row=1,column=1)

btn = tk.Button(win,text="確定",width=15,command=tktk)
btn.grid(row=3,column=1)

lblResult = tk.Label(win,text=" ",padx=10,pady=8)
lblResult.grid(row=2,column=1)
win.mainloop()