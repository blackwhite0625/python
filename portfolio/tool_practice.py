while True:
        
    print('1.變數列印\n2.整數浮點數計算\n3.攝氏轉華氏,華氏轉攝氏\n4.判斷正負\n5.1+2...10\n6.字串分裂\n7.數據資料視覺化1\n8.len()函式 計算字數\n9.range用法\n10.數據資料視視覺化2')


    import matplotlib.pyplot as plt
    SHY = int(input('輸入1到10 (輸入其他數字退出): '))

    #變數列印
    if SHY == 1:
        print('整數20', '浮點數2.56', '字元B', '字串book')

    #整數浮點數計算
    elif SHY == 2:
        a = int(input('請輸入第一個整數: '))
        b = int(input('請輸入第二個整數: '))
        c = float(input('請輸入一個浮點數: '))
        hom = a + b
        boe = a - b
        cos = a * b
        soi = a + c, a * c, b + c, b * c
        print('兩整數相加為:', hom)
        print('兩整數相減為:', boe)
        print('兩整數相乘為:', cos)
        print('整數與浮點數相加相乘', soi)

    #攝氏轉華氏
    elif SHY == 3:
        CF = input (('攝氏轉華氏輸入（Ｃ）,華氏轉攝氏輸入（Ｆ）:'))
        if CF == 'C':
            C1 = float(input('請輸入攝氏溫度: '))
            F1 = (9/5) * C1 + 32
            print('華氏溫度為:', F1, '°F')
        if CF == 'F':
            F1 = float(input('請輸入華氏溫度: '))
            C1 = (F1-32)*(5/9)
            
    #判斷正負數
    elif SHY == 4:
        num1 = float(input("請輸入一個數: "))
        if num1 > 0:
            print(num1, '是一個正數')
        elif num1 < 0:
            print(num1, '是一個負數')
        else:
            print(num1, '是零')

    #1+2..10
    elif SHY == 5:
        sum1 = 0
        for i in range(1, 11):
            sum1 += i
        print('1+2...10為:', sum1)

    #字串分裂
    elif SHY == 6:
        word = 'performance'
        print(word[0], word[5], word[-3], word[0:5], word[2:6], word[-6:-2], word[:2], word[6:], 's'+word[1:])

    #數據資料視覺化1
    elif SHY == 7:
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

    #len()函式 計算字數
    elif SHY == 8:
        iou = ['C++', 'Python', 'java', 'C#']
        for pur in iou:
            print(pur, len(pur))

    #range用法
    elif SHY == 9:
        for osu in range(5):
            print(osu)

    #數據資料視覺化2
    elif SHY == 10:
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
        #plt.plot(listx,listy)
        #plt.plot(listx,listy,'g--o')#綠色,--是虛線,o是形狀
        #plt.plot(listx,listy,'r-<')#紅色,-是實線,v ^ < >三角形
        #plt.plot(listx,listy,'b-|')#藍色,實線,直線| 橫線_
        #plt.plot(listx,listy,'k-x')#黑色,實線,x是叉叉 +是十字
        #plt.plot(listx,listy,'y-p')#黃色,實線,五角形p
        #plt.plot(listx,listy,'c-d')#青色,實線,鑽石d 大D
        #plt.plot(listx,listy,'m:h')#洋紅色m,:是點線,矩形s 六角形h
        #plt.plot(listx,listy,'k-.3')#白色w,虛點線,上下左右人字形1234
        #plt.show()
    
    
    else:
        print("已退出程式")
        break
