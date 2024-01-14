import requests
import time
from bs4 import BeautifulSoup
while True:
    def send_line_message(token, message):
        
        headers = {
            #http身份驗證標準
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        #data傳送訊息
        data = {
            'message': message,
            # 'imageThumbnail': image_thumbnail,
            # 'imageFullsize': image_fullsize
        }
    
        #requests解析notify網址
        notify = requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)
        
        #檢查http請求
        if notify.status_code == 200:
            print("發送成功")
        else:
            print("發送失敗")


    #line notify權杖
    token = 'StsW43gQB49OgUnvwobGeXbL99RHSxH2CYzY2ExaXs9'
    #data傳送訊息
    url = "https://tw.stock.yahoo.com/cryptocurrencies"
    response2 = requests.get(url)
    yahoo2 = BeautifulSoup(response2.text,"html.parser")
    yahoom2 = yahoo2.find("li",class_="List(n)")

    for yahoos2 in yahoom2:
        data1={}
        name2 = yahoos2.find("div",class_="Lh(20px) Fw(600) Fz(16px) Ell")
        name2 = name2.text
        data1["股名"]=name2

        price2= yahoos2.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(90px)")
        price2 = price2.span.text
        data1["股價"]=price2
        
        times2 = yahoos2.find("div",class_="Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(48px) Fxg(0)")
        times2 = times2.span.text
        data1["時間"]=times2
    
    message = (f"{data1}")
    # image_thumbnail = 'https://cdn.vox-cdn.com/thumbor/ECCRE0goZLG60tO5IXvvOhqlDg4=/0x0:1000x563/1820x1213/filters:focal(420x202:580x362):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/69737432/S3e9_Fionna_playing_with_Cake.0.png'
    # image_fullsize = 'https://cdn.vox-cdn.com/thumbor/ECCRE0goZLG60tO5IXvvOhqlDg4=/0x0:1000x563/1820x1213/filters:focal(420x202:580x362):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/69737432/S3e9_Fionna_playing_with_Cake.0.png'

    #發送次數
    timeout = 0  
    while timeout < 1:
        send_line_message(token, message)#, image_thumbnail, image_fullsize
        timeout += 1
        time.sleep(3600)
   

