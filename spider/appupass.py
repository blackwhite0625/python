import requests
from bs4 import BeautifulSoup


#mimi韓旅遊生活
url1="https://mimihan.tw/songshan-culturalpark/"
response1=requests.get(url1)

taipei1=BeautifulSoup (response1.text,"html.parser")



tai1=taipei1.find_all("div",class_="atm_mk_h2mmj6 wkay9zb")
# data_list=[]
# for dcardm in dcards:
#         data={}
#         news = dcardm.find("h3")
#         if news and news.strong:
#             news = news.strong.text
#         else:
#             news = "無"
#         data["地址"]=news



        # data_list.append(data)
        # excel1 = pd.DataFrame(data_list)
        # excel1.to_excel("taipei_data.xlsx",index=False,engine="openpyxl")
        
