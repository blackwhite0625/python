import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.ptt.cc/bbs/Stock/search?page=1&q=%E7%BE%8E%E8%82%A1"
#headers 模仿使用者User-Agent
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
ptt=requests.get(url,headers=headers)
datas=BeautifulSoup(ptt.text,"html.parser")
spider1=datas.find_all("li",class_="List(n)")
data_list=[]
for a in spider1:
    data = {}
    #人氣
    famous =a.find("div",class_="nrec")
    if famous and famous.span:
        famous = famous.span.text
    else:
        famous = "無"
    data["人氣"]=famous
    
    #標題
    title =a.find("div",class_="title")
    if title and title.a:
        title=title.a.text
    else:
        title="沒有標題"
    data["標題"]=title
    
    #日期
    date =a.find("div",class_="date")
    if date:
        date =date.text
    else:
        data ="無"
    data["日期"]=date
    data_list.append(data)

#檔案儲存為excel(xlsx檔案)
excel1 = pd.DataFrame(data_list)
excel1.to_excel("ptt_data.xlsx",index=False,engine="openpyxl")
print('儲存成功')

