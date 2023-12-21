import tkinter as tk

def remove_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

my_window = tk.Tk()
my_window.title("刪除")

# 创建一个 Frame 来容纳要删除的小部件
frame_to_remove = tk.Frame(my_window)
frame_to_remove.pack()

# 添加要删除的小部件到 frame_to_remove
button_to_remove = tk.Button(frame_to_remove, text="这是一个要删除的按钮")
button_to_remove.pack()

text_to_remove = tk.Label(frame_to_remove, text="这是要删除的文本")
text_to_remove.pack()

# 创建一个按钮，点击它会触发删除操作
remove_button = tk.Button(my_window, text="刪除部分按鈕和文本", command=lambda: remove_widgets(frame_to_remove))
remove_button.pack()

my_window.mainloop()
