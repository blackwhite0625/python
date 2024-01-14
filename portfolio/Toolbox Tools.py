import tkinter as tk
import webbrowser
import requests
from bs4 import BeautifulSoup
    
#主視窗
root = tk.Tk()
root.title("小工具")

#儲存刪除的內容
content_frame = tk.Frame(root)
content_frame.pack()

#定義網路資料爬取函數
power_title_label = tk.Label(content_frame, text='')
open_order_label = tk.Label(content_frame, text='')
size_order_label = tk.Label(content_frame, text='')
second_zone_label = tk.Label(content_frame, text='')

# 定義按鈕 執行該動作
def bomrr():
    SHY = int(entry.get())

    #計算機
    if SHY == 1:
        show_io1()
    
    #攝氏轉華氏和華氏轉攝氏
    elif SHY == 2:
        show_io2()
            
    #數據資料視覺化1
    elif SHY == 3:
        import matplotlib.pyplot as plt
        from matplotlib.font_manager import FontProperties
        import numpy as np
        
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        font = FontProperties()
        
        listx = ['c', 'c++', 'c#', 'java', 'python']
        listy1 = [56, 20, 20, 16, 28]
        listy2 = [20, 8, 18, 16, 22]
        listy3 = [5, 10, 13, 6, 17]
        listy4 = []

        for i in range(0, 5):
            listy4.append(listy1[i] + listy2[i])

        plt.bar(listx, listy1, width=0.3, color="blue",label='男生')
        plt.bar(listx, listy2, width=0.3, bottom=listy1,color="red",label='女生')
        plt.bar(listx, listy3, width=0.3, bottom=listy4,color="lime", label='中性')
        plt.legend(prop=font)  
        plt.xlabel('程式語言', fontproperties=font)
        plt.ylabel('人數(萬)', fontproperties=font)
        plt.show()

  

    #數據資料視覺化2
    elif SHY == 4:
        import matplotlib.pyplot as plt
        from matplotlib.font_manager import FontProperties
        import numpy as np
        
        #將matplotlib字體設置為Arial Unicode MS
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        font1 = FontProperties()
        listx = [13, 14, 15, 16, 17, 18,19,20,21,22,23]
        listy = [108, 138, 140, 185, 229, 226,333,232,652,636,533]
        
        
        #繪製折線圖
        plt.plot(listx, listy, color="red", lw=2.0, ls="-.", label="漲幅")  
       
        plt.legend(prop=font1)
        
        #標題
        plt.title('台積電', fontproperties=font1, fontsize=20)
        
        #XＹ軸標籤
        plt.xlabel('年份', fontproperties=font1, fontsize=16)
        plt.ylabel('股價', fontproperties=font1, fontsize=16)
        plt.xticks(range(0, 24, 1))
        plt.yticks(range(0, 700, 80))
        plt.xlim(13, 23)

        #網格
        plt.grid(True)
        plt.grid(color='black', linestyle='-', linewidth=1, alpha=0.3)
        
        #顯示圖表
        plt.show()
        
    #開啟google
    elif SHY == 5:
        url = 'https://www.google.com.tw'
        webbrowser.open(url)
    
    #開啟動畫瘋
    elif SHY == 6:
        url = 'https://ani.gamer.com.tw/'
        webbrowser.open(url)
    
    #字串列印
    elif SHY == 7:
        show_io3()
    
    #網路資料爬取
    elif SHY == 8:
        show_io4(power_title_label, open_order_label, size_order_label, second_zone_label)
        
    #bmi計算
    elif SHY == 9:
        show_io5()  
        
    #清空内容 Frame 中的小部件
    elif SHY == 10:
        clear_content_frame()

# 創建函數清空Frame
def clear_content_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()
        
#計算機
def show_io1():
    clear_content_frame()

    # 輸入數字1
    a_lable = tk.Label(content_frame, text="請輸入第一個數字:")
    a_lable.pack( )

    # 數字1輸入框
    a_entry = tk.Entry(content_frame)
    a_entry.pack()

    def get_text1():
        user_input1 = a_entry.get()
        A.config(text="第一個數字是： " + user_input1)
    A = tk.Label(content_frame, text="")
    A.pack()

    # 輸入數字2
    b_lable = tk.Label(content_frame, text="請輸入第二個數字:")
    b_lable.pack()
    b_entry = tk.Entry(content_frame)
    b_entry.pack()

    def get_text2():
        user_input2 = b_entry.get()
        B.config(text="第二個數字是： " + user_input2)
    B = tk.Label(content_frame, text="")
    B.pack()

    # 加法
    def get_text4():
        user_input1 = a_entry.get()
        user_input2 = b_entry.get()

        user_input1 = float(user_input1)
        user_input2 = float(user_input2)

        user_input4 = user_input1 + user_input2 
        DD.config(text="相加結果為 " + str(user_input4))

    sum_button = tk.Button(content_frame, text="加法", command=get_text4)
    sum_button.pack()
    DD = tk.Label(content_frame, text="")
    DD.pack()

    # 減法
    def get_text5():
        user_input1 = a_entry.get()
        user_input2 = b_entry.get()
        user_input1 = float(user_input1)
        user_input2 = float(user_input2)
        user_input5 = user_input1 - user_input2 
        EE.config(text="相減結果為 " + str(user_input5))

    sum1_button = tk.Button(content_frame, text="減法", command=get_text5)
    sum1_button.pack()
    EE = tk.Label(content_frame, text="")
    EE.pack()
    
    #乘法
    def get_text6():
        user_input1 = a_entry.get()
        user_input2 = b_entry.get()
        user_input1 = float(user_input1)
        user_input2 = float(user_input2)
        user_input6 = user_input1 * user_input2 
        FF.config(text="相乘結果為 " + str(user_input6))

    sum2_button = tk.Button(content_frame, text="乘法", command=get_text6)
    sum2_button.pack()
    FF = tk.Label(content_frame, text="")
    FF.pack()
    
    #除法

    def get_text7():
        user_input1 = a_entry.get()
        user_input2 = b_entry.get()
        user_input1 = float(user_input1)
        user_input2 = float(user_input2)
        user_input7 = user_input1 / user_input2 
        GG.config(text="相除結果為 " + str(user_input7))

    sum3_button = tk.Button(content_frame, text="除法", command=get_text7)
    sum3_button.pack()
    GG = tk.Label(content_frame, text="")
    GG.pack()
    
#攝氏轉華氏和華氏轉攝氏
def show_io2():  
    clear_content_frame()
    #創建標籤 問題
    cf_label = tk.Label(content_frame, text="請輸入溫度:")
    cf_label.pack()
    
    #創建輸入框
    cf_entry = tk.Entry(content_frame)
    cf_entry.pack()


    result_label = tk.Label(content_frame, text="")
    result_label.pack()


    def convert_temperature():
        C01 = cf_entry.get()
        try:
            C01 = float(C01)
            F01 = 0
            if cf_var.get() == 0:  
                F01 = (C01 * 9/5) + 32
                result_label.config(text=f"華氏溫度為: {F01} °F")
            elif cf_var.get() == 1:  
                F01 = (C01 - 32) * 5/9
                result_label.config(text=f"攝氏溫度為: {F01} °C")
            
        except ValueError:
            result_label.config(text="請輸入有效的數字")

    # 创建温度单位选择部分
    cf_var = tk.IntVar()
    cf_var.set(0)  

    cf_frame = tk.Frame(content_frame)
    cf_frame.pack()
    #創建選擇按鈕（。）
    c_to_f = tk.Radiobutton(cf_frame, text="攝氏轉華氏", variable=cf_var, value=0)
    f_to_c = tk.Radiobutton(cf_frame, text="華氏轉攝氏", variable=cf_var, value=1)
    c_to_f.pack(side=tk.LEFT)
    f_to_c.pack(side=tk.LEFT)
    
    #轉換按鈕
    convert_button = tk.Button(content_frame, text="轉換", command=convert_temperature)
    convert_button.pack()
  
#字串列印      
def show_io3():
    label = tk.Label(content_frame,text="你好傻欸")
    label.pack()

#網路資料爬取
def show_io4(power_title_label, open_order_label, size_order_label, second_zone_label):
    clear_content_frame()

    
    power_title_label = tk.Label(content_frame, text='')
    open_order_label = tk.Label(content_frame, text='')
    size_order_label = tk.Label(content_frame, text='')
    second_zone_label = tk.Label(content_frame, text='')

    url = 'https://www.taiwanlottery.com.tw/'
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')

    datas = sp.find('div', class_='contents_box02')
    title = datas.find('span', 'font_black15').text
    power_title_label.config(text='威力彩期數: ' + title)

    nums = datas.find_all('div', class_="ball_tx ball_green")

    open_order_label.config(text='開出順序: ' + ' '.join([num.text for num in nums[:6]]))
    size_order_label.config(text='大小順序: ' + ' '.join([num.text for num in nums[6:12]]))

    num = datas.find('div', class_='ball_red').text
    second_zone_label.config(text='第二區: ' + num)

    power_title_label.pack()
    open_order_label.pack()
    size_order_label.pack()
    second_zone_label.pack()

#bmi計算
def show_io5():
    clear_content_frame()
    height_label = tk.Label(content_frame, text="請輸入身高(請輸入公尺):")
    height_label.pack()
    height_entry = tk.Entry(content_frame)
    height_entry.pack()
    weight_label = tk.Label(content_frame, text="請輸入體重:")
    weight_label.pack()
    weight_entry = tk.Entry(content_frame)
    weight_entry.pack()

    def bmi_text():
        bmi_input1 = height_entry.get()
        bmi_input2 = weight_entry.get()

        bmi_input1 = float(bmi_input1)
        bmi_input2 = float(bmi_input2)

        bmi_input3 = bmi_input2 / (bmi_input1 ** 2)
        Bmi.config(text="你的bmi為 " + str(bmi_input3))

    bmi_button = tk.Button(content_frame, text="輸出", command=bmi_text)
    bmi_button.pack()
    Bmi = tk.Label(content_frame, text="")
    Bmi.pack()

  
    

# 創建輸入框
entry_label = tk.Label(root, text="請輸入1~10做選擇\n1.計算機\n2.攝氏轉華氏與華氏轉攝氏\n3.數據資料視覺化1\n4.數據資料視覺化2\n5.開啟Google\n6.開啟巴哈動畫\n7.戶頭多一百萬\n8.威力彩號碼\n9.bmi計算\n10.刪除")

entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# 執行按鈕
execute_button = tk.Button(root, text="執行", command=bomrr)
execute_button.pack()

# 顯示結果
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# 主循環
root.mainloop()
