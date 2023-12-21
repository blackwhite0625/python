import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time


#美股
def yahoo_data(url):
    response = requests.get(url)
    yahoo = BeautifulSoup(response.text,"html.parser")
    yahoom = yahoo.find_all("li",class_="List(n)")
    data_list=[]
    for yahoos in yahoom:
        data={}
 
        name = yahoos.find("div",class_="Lh(20px) Fw(600) Fz(16px) Ell")
        if name and name.span:
            name = name.span.text
        else:
            name = "無"
        data["股名"]=name
        
        enname = yahoos.find("div",class_="D(f) Ai(c)")
        if enname and enname.span:
            enname = enname.span.text
        else:
            enname = "無"
        data["股號"]=enname
        
        price = yahoos.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(90px)")
        if price and price.span:
            price = price.span.text
        else:
            price = "無"
        data["股價"]=price
        
        updown = yahoos.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Miw($w-table-cell-min-width) Ta(end) Mend($m-table-cell-space) Mend(0):lc")
        if updown and updown.span:
            updown = updown.span.text
        else:
            updown = "無"
        data["漲幅"]=updown
        
        updowns = yahoos.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Miw($w-table-cell-min-width) Ta(end) Mend($m-table-cell-space) Mend(0):lc")
        if updowns and updowns.span:
            updowns = updowns.span.text
        else:
            updowns = "無"
        data["漲跌幅%"]=updowns
        
        times = yahoos.find("div",class_="Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(48px) Fxg(0)")
        if times and times.span:
            times = times.span.text
        else:
            times = "無"
        data["時間"]=times
        data_list.append(data)
        #print(f"{name} {enname} {price} {updown} {updowns}")
        excel = pd.DataFrame(data_list)
        excel.to_excel("./excel/yahoo_data.xlsx",index=False,engine="openpyxl")
        
#港股
def yahoo1_data(url1):
    response1 = requests.get(url1)
    yahoo1 = BeautifulSoup(response1.text,"html.parser")
    yahoom1 = yahoo1.find_all("li",class_="List(n)")
    data1_list=[]
    for yahoos1 in yahoom1:
        data1={}

        name1 = yahoos1.find("div",class_="Lh(20px) Fw(600) Fz(16px) Ell")
        if name1 and name1:
            name1 = name1.text
        else:
            name1 = "無"
        data1["股名"]=name1
        
        enname1 = yahoos1.find("div",class_="D(f) Ai(c)")
        if enname1 and enname1.span:
            enname1 = enname1.span.text
        else:
            enname1 = "無"
        data1["股號"]=enname1
        
        price1= yahoos1.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(90px)")
        if price1 and price1.span:
            price1 = price1.span.text
        else:
            price1 = "無"
        data1["股價"]=price1
        
        updown1 = yahoos1.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Miw($w-table-cell-min-width) Ta(end) Mend($m-table-cell-space) Mend(0):lc")
        if updown1 and updown1.span:
            updown1 = updown1.span.text
        else:
            updown1 = "無"
        data1["漲幅"]=updown1
        
        updowns1 = yahoos1.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Miw($w-table-cell-min-width) Ta(end) Mend($m-table-cell-space) Mend(0):lc")
        if updowns1 and updowns1.span:
            updowns1 = updowns1.span.text
        else:
            updowns1 = "無"
        data1["漲跌幅%"]=updowns1
        
        times1 = yahoos1.find("div",class_="Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(48px) Fxg(0)")
        if times1 and times1.span:
            times1 = times1.span.text
        else:
            times1 = "無"
        data1["時間"]=times1
        data1_list.append(data1)
        excel1 = pd.DataFrame(data1_list)
        excel1.to_excel("./excel/yahoo1_data.xlsx",index=False,engine="openpyxl")

#虛擬貨幣
def yahoo2_data(url2):
    response2 = requests.get(url2)
    yahoo2 = BeautifulSoup(response2.text,"html.parser")
    yahoom2 = yahoo2.find_all("li",class_="List(n)")
    data2_list=[]
    for yahoos2 in yahoom2:
        data2={}

        name2 = yahoos2.find("div",class_="Lh(20px) Fw(600) Fz(16px) Ell")
        if name2 and name2:
            name2 = name2.text
        else:
            name2 = "無"
        data2["股名"]=name2
        
        enname2 = yahoos2.find("div",class_="D(f) Ai(c)")
        if enname2 and enname2.span:
            enname2 = enname2.span.text
        else:
            enname2 = "無"
        data2["股號"]=enname2
        
        price2= yahoos2.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(90px)")
        if price2 and price2.span:
            price2 = price2.span.text
        else:
            price2 = "無"
        data2["股價"]=price2
        
        updown2 = yahoos2.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Miw($w-table-cell-min-width) Ta(end) Mend($m-table-cell-space) Mend(0):lc")
        if updown2 and updown2.span:
            updown2 = updown2.span.text
        else:
            updown2 = "無"
        data2["漲幅"]=updown2
        
        updowns2 = yahoos2.find("div",class_="Fxg(1) Fxs(1) Fxb(0%) Miw($w-table-cell-min-width) Ta(end) Mend($m-table-cell-space) Mend(0):lc")
        if updowns2 and updowns2.span:
            updowns2 = updowns2.span.text
        else:
            updowns2 = "無"
        data2["漲跌幅%"]=updowns2
        
        times2 = yahoos2.find("div",class_="Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(48px) Fxg(0)")
        if times2 and times2.span:
            times2 = times2.span.text
        else:
            times2 = "無"
        data2["時間"]=times2
        data2_list.append(data2)
        excel2 = pd.DataFrame(data2_list)
        excel2.to_excel("./excel/yahoo2_data.xlsx",index=False,engine="openpyxl")
        

        
url ="https://tw.stock.yahoo.com/us-market"
yahoo_data(url)
url1 ="https://tw.stock.yahoo.com/hk-market"
yahoo1_data(url1)
url2 ="https://tw.stock.yahoo.com/cryptocurrencies"
yahoo2_data(url2)

print("產生成功")