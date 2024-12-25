import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("oxxo.studio")
root.geometry("500x500")

img = Image.open("images.jpg").resize((150,240))
tk_img = ImageTk.PhotoImage(img)

label = tk.Label(root,image=tk_img,width=150,height=240,anchor="nw")
label.pack()
root.mainloop()