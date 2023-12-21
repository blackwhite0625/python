import tkinter as tk
import webbrowser #開啟網頁
import requests #http請求
from bs4 import BeautifulSoup #html解析

    
#主視窗
root = tk.Tk()
#標題
root.title("工具箱(待更新)")
#視窗大小
root.geometry()
#儲存刪除的內容
content_frame = tk.Frame(root)
content_frame.pack()

# 定義按鈕 執行該動作
def bomrr():
    SHY = int()

    #計算機
    if SHY == 1:
        show_io1()
    
    #攝氏轉華氏和華氏轉攝氏
    elif SHY == 2:
        show_io2()
            
    #數據資料視覺化1
    elif SHY == 3:
        show_io6()

    #數據資料視覺化2
    elif SHY == 4:
        show_io7()
        
    #開啟google
    elif SHY == 5:
        show_io8()
    
    #開啟動畫瘋
    elif SHY == 6:
        show_io9()
    
    #字串列印
    elif SHY == 7:
        show_io3()
    
    #網路資料爬取
    elif SHY == 8:
        show_io4()
        
    #bmi計算
    elif SHY == 9:
        show_io5()  
        
    #數據資料視覺化(自定義圓餅圖)
    elif SHY == 10:
        show_io11()
        
    #清空内容 Frame 中的小部件
    elif SHY == 11:
        show_io10()
    #開啟yt
    elif SHY == 12:
        show_io12()
         
    #起始數加到末尾數  
    elif SHY == 13:
        show_io13()

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

    #創建選擇單位
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
  
#rick roll
def show_io3():
    clear_content_frame()
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
    webbrowser.open(url)

#網路資料爬取
def show_io4():
    clear_content_frame()
    #數據資料爬取 定義
    name1_label = tk.Label(content_frame, text='')
    open1_label = tk.Label(content_frame, text='')
    size1_label = tk.Label(content_frame, text='')
    twoname1_label = tk.Label(content_frame, text='')
    
    url = 'https://www.taiwanlottery.com.tw/'
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')

    datas = sp.find('div', class_='contents_box02')
    title = datas.find('span', 'font_black15').text
    name1_label.config(text='威力彩期數: ' + title)

    nums = datas.find_all('div', class_="ball_tx ball_green")

    open1_label.config(text='開出順序: ' + ' '.join([num.text for num in nums[:6]]))
    size1_label.config(text='大小順序: ' + ' '.join([num.text for num in nums[6:12]]))

    num = datas.find('div', class_='ball_red').text
    twoname1_label.config(text='第二區: ' + num)

    name1_label.pack()
    open1_label.pack()
    size1_label.pack()
    twoname1_label.pack()

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

#柱狀圖
def show_io6():
    clear_content_frame()
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

#折線圖  
def show_io7():
    clear_content_frame()
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
    clear_label3 = tk.Label(content_frame, text="")
    clear_label3.pack()
 
#開啟google
def show_io8():
    clear_content_frame()
    url = 'https://www.google.com.tw'
    webbrowser.open(url)

#開啟巴哈動畫   
def show_io9():
    clear_content_frame()
    url = 'https://ani.gamer.com.tw/'
    webbrowser.open(url)
    
#回覆清空
def show_io10():
    clear_content_frame()
    clear_label = tk.Label(content_frame, text="")
    clear_label.pack()

#數據資料視覺化 自定義 (圓餅圖)
def show_io11():
    clear_content_frame()
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    
    def on_entry_click(event):
        if entry_default_text in dataf_entry.get():
            dataf_entry.delete(0, "end")
            dataf_entry.config(fg="black") 
    def on_entry_click1(event):
        if entry1_default_text in dataf1_entry.get():
            dataf1_entry.delete(0, "end")
            dataf1_entry.config(fg="black") 
    def on_entry_click2(event):
        if entry2_default_text in dataf2_entry.get():
            dataf2_entry.delete(0, "end")
            dataf2_entry.config(fg="black") 
    def on_entry_click3(event):
        if entry3_default_text in dataf3_entry.get():
            dataf3_entry.delete(0, "end")
            dataf3_entry.config(fg="black")
    def on_entry_click4(event):
        if entry4_default_text in datan_entry.get():
            datan_entry.delete(0, "end")
            datan_entry.config(fg="black") 
    def on_entry_click5(event):
        if entry5_default_text in datan1_entry.get():
            datan1_entry.delete(0, "end")
            datan1_entry.config(fg="black") 
    def on_entry_click6(event):
        if entry6_default_text in datan2_entry.get():
            datan2_entry.delete(0, "end")
            datan2_entry.config(fg="black") 
    def on_entry_click7(event):
        if entry7_default_text in datan3_entry.get():
            datan3_entry.delete(0, "end")
            datan3_entry.config(fg="black") 
    
    #數據%數框架創建
    input_frame = tk.LabelFrame(content_frame, text="請輸入數據(%數)")
    input_frame.pack()
    
    #設置提示輸入順序文字
    entry_default_text = "第一數: "
    dataf_entry = tk.Entry(input_frame, fg="gray")  
    dataf_entry.insert(0, entry_default_text)
    dataf_entry.grid(row=0, column=0)
    dataf_entry.bind("<FocusIn>", on_entry_click)
    
    entry1_default_text = "第二數: "
    dataf1_entry = tk.Entry(input_frame, fg="gray")  
    dataf1_entry.insert(0, entry1_default_text)
    dataf1_entry.grid(row=0, column=1)
    dataf1_entry.bind("<FocusIn>", on_entry_click1)
    
    entry2_default_text = "第三數: "
    dataf2_entry = tk.Entry(input_frame, fg="gray")  
    dataf2_entry.insert(0, entry2_default_text)
    dataf2_entry.grid(row=1, column=0)
    dataf2_entry.bind("<FocusIn>", on_entry_click2)
    
    entry3_default_text = "第四數: "
    dataf3_entry = tk.Entry(input_frame, fg="gray") 
    dataf3_entry.insert(0, entry3_default_text)
    dataf3_entry.grid(row=1, column=1)
    dataf3_entry.bind("<FocusIn>", on_entry_click3)
    
    input1_frame = tk.LabelFrame(content_frame, text="請輸入數據(名稱)")
    input1_frame.pack()
    
    entry4_default_text = "第一個數據名稱: "
    datan_entry = tk.Entry(input1_frame, fg="gray")  
    datan_entry.insert(0, entry4_default_text)
    datan_entry.grid(row=0, column=0)
    datan_entry.bind("<FocusIn>", on_entry_click4)
    
    entry5_default_text = "第二個數據名稱: "
    datan1_entry = tk.Entry(input1_frame, fg="gray")  
    datan1_entry.insert(0, entry5_default_text)
    datan1_entry.grid(row=0, column=1)
    datan1_entry.bind("<FocusIn>", on_entry_click5)
    
    entry6_default_text = "第三個數據名稱: "
    datan2_entry = tk.Entry(input1_frame, fg="gray")  
    datan2_entry.insert(0, entry6_default_text)
    datan2_entry.grid(row=1, column=0)
    datan2_entry.bind("<FocusIn>", on_entry_click6)
    
    entry7_default_text = "第四個數據名稱: "
    datan3_entry = tk.Entry(input1_frame, fg="gray") 
    datan3_entry.insert(0, entry7_default_text)
    datan3_entry.grid(row=1, column=1)
    datan3_entry.bind("<FocusIn>", on_entry_click7)

    
    def pie():
        #獲取用戶輸入數據
        data = dataf_entry.get(),dataf1_entry.get(),dataf2_entry.get(),dataf3_entry.get()
        labels = datan_entry.get(),datan1_entry.get(),datan2_entry.get(),datan3_entry.get()
        #數據(數字轉成浮點數_小數)
        data = [float(item) for item in data]
        #圖型顏色
        colors = ['#ff9999', '#0000ff', '#99ff99', '#ffcc99']
        #圖形突出
        explode = (0, 0, 0, 0)
        #圓餅圖繪製‘
        plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True, explode=explode)
        #圓餅圖標題
        plt.title('圓餅圖數據')
        #圓餅圖顯示
        plt.show()
        

    
    #輸出按鈕
    data_button = tk.Button(content_frame, text="產生", command=pie)
    data_button.pack()
    Data = tk.Label(content_frame, text="")
    Data.pack()
 
#開啟yt   
def show_io12():
    clear_content_frame()
    url = 'https://www.youtube.com/'
    webbrowser.open(url)

#起始數加到末尾數
def show_io13():

    clear_content_frame()
    
    start_lable = tk.Label(content_frame, text="請輸入起始數:")
    start_lable.pack( )
    start_entry = tk.Entry(content_frame)
    start_entry.pack()


    start1_lable = tk.Label(content_frame, text="請輸入末尾數:")
    start1_lable.pack( )
    start1_entry = tk.Entry(content_frame)
    start1_entry.pack()


    def start2_text1():
        userf1_input1 = start_entry.get()
        userf2_input1 = start1_entry.get()

        userf1_input1 = int(round(float(userf1_input1)))
        userf2_input1 = int(round(float(userf2_input1)))
        total_sum = 0
        for i in range(userf1_input1, userf2_input1 + 1):
            total_sum += i
        total_sum_label.config(text="從" + str(userf1_input1) + "加到"+ str(userf2_input1)+ "等於  " +str(total_sum))

    total_sum_button = tk.Button(content_frame, text="輸出", command=start2_text1)
    total_sum_button.pack()
    total_sum_label = tk.Label(content_frame, text="")
    total_sum_label.pack()

    
#按鈕功能文字框框
buttom_frame = tk.LabelFrame(root, text="學校工具類",font=("Helvetica",20))
buttom_frame.pack()
buttom_frame1 =tk.LabelFrame(root, text='數據分析類',font=("Helvetica",20))
buttom_frame1.pack()
buttom_frame2 =tk.LabelFrame(root, text='開啟網頁類',font=("Helvetica",20))
buttom_frame2.pack()

#創建功能按鈕
execute_button1 = tk.Button(buttom_frame,text='計算機',command=show_io1, width=15, height=1)
execute_button1.grid(row=0, column=0)

execute_button2 = tk.Button(buttom_frame,text='攝氏轉華氏和華氏轉攝氏',command=show_io2, width=15, height=1)
execute_button2.grid(row=0, column=1)

execute_button3 = tk.Button(buttom_frame1,text='柱狀圖數據',command=show_io6, width=15, height=1)
execute_button3.grid(row=0,column=0)

execute_button4 = tk.Button(buttom_frame1,text='折線圖數據',command=show_io7, width=15, height=1)
execute_button4.grid(row=0,column=1)

execute_button5 = tk.Button(buttom_frame2,text='開啟Google',command=show_io8, width=15, height=1)
execute_button5.grid(row=0,column=0)

execute_button6 = tk.Button(buttom_frame2,text='開啟巴哈動畫',command=show_io9, width=15, height=1)
execute_button6.grid(row=0,column=1)

execute_button7 = tk.Button(buttom_frame2,text='戶頭多一百萬',command=show_io3, width=15, height=1)
execute_button7.grid(row=1,column=0)

execute_button8 = tk.Button(buttom_frame1,text='數據資料爬取(威力彩)',command=show_io4, width=15, height=1)
execute_button8.grid(row=1,column=0)

execute_button9 = tk.Button(buttom_frame,text='bmi計算',command=show_io5, width=15, height=1)
execute_button9.grid(row=1,column=0)

execute_button10 = tk.Button(buttom_frame1,text='圓餅圖數據自定義繪製',command=show_io11, width=15, height=1)
execute_button10.grid(row=1,column=1)

execute_button11 = tk.Button(buttom_frame2,text='開啟youtube',command=show_io12, width=15, height=1)
execute_button11.grid(row=1,column=1)

execute_button12 = tk.Button(root,text='回復',command=show_io10, width=15, height=1)
execute_button12.pack()

execute_button13 = tk.Button(buttom_frame,text='起始末尾加總',command=show_io13, width=15, height=1)
execute_button13.grid(row=1,column=1)

# 顯示結果
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# 主循環
root.mainloop()
