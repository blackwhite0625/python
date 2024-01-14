import requests
from bs4 import BeautifulSoup
import json

url="https://www.ptt.cc/bbs/Stock/search?page=1&q=%E7%BE%8E%E8%82%A1"
#headers 模仿使用者User-Agent
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
ptt=requests.get(url,headers=headers)
datas=BeautifulSoup(ptt.text,"html.parser")
spider1=datas.find_all("div",class_="r-ent")
data_list=[]
for a in spider1:
    data = {}
    famous =a.find("div",class_="nrec")
    if famous and famous.span:
        famous = famous.span.text
    else:
        famous = "無"
    data["人氣"]=famous
    
    title =a.find("div",class_="title")
    if title and title.a:
        title=title.a.text
    else:
        title="沒有標題"
    data["標題"]=title
    
    date =a.find("div",class_="date")
    if date:
        date =date.text
    else:
        data ="無"
    data["日期"]=date
    data_list.append(data)

#把結果儲存到ptt_data.json
with open("ptt_data.json","w",encoding="utf-8")as file:
    json.dump(data_list,file,ensure_ascii=False,indent=4)
print("資料儲存成功")
        
    # print(f"人氣:{famous} 日期:{date} 標題:{title}")
    

# for a in spider1:
#     title=a.find("ul",class_="")
#     print(title)

# for b in spider1:
#     ul =b.find("ul",class_="table-body-wrapper")
#     if ul and ul.b:
#         ul=ul.b.text
#     else:
#         ul="沒ul"
#     print(ul)
#尋找標題
# for a in spider1:
#     title = a.find("div",class_="W(152px) Ta(start)")
#     if title and title.a:
#         title=title.a.text
#     else:
#         title = "沒有標題"
#     print(title)
#print(yahoo.text)

# 判斷網址是否錯誤 是的話就產生html
# if yahoo.status_code == 200:
#     with open('yahoo.html','w',encoding='utf-8')as f:
#         f.write(title.a.text)
#     print('寫入成功')
# else:
#     print('寫入失敗')