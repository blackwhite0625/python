import requests
from bs4 import BeautifulSoup
import pandas as pd


url="https://www.dcard.tw/f/oit?tab=latest"
headers ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
          "Cookie":"_gcl_au=1.1.2044839712.1700456978; _ga=GA1.1.1815450109.1700456978; __cf_bm=wGFrI0l9tSMLj2IYqfESeZAanDgtmIWDDTuQ8qPNY_A-1701151048-0-AfyPqQbxl5KLCcBuO99LhA3Ww395e2vK2Tsl2Tk506/9Ol4MCUPdjGSrnInD1QQy1Waa1zMSfRMcl7SAHE9D98Y=; _cfuvid=I2btr5yj.Xwt0oJOIs3D7aMWB8WT5I3XVksfxm2A7N4-1701151048836-0-604800000; __cf_dm=YWRtaW46MDox.126.crc.cf4dca1e; NID=44901020; cf_clearance=6HCgvu7fJQpSXKeoez5WaMCBuCGbPsUeZEGLwCjhvmE-1701151061-0-1-d70ac7a0.cd0f6624.3b42c358-0.2.1701151061; dcsrd=2Gd6dhE_wN97dV4vQXce4vBI; dcard-web-oauth-tk=eyJhY2Nlc3NUb2tlbiI6ImV5SmhiR2NpT2lKRlpFUlRRU0lzSW10cFpDSTZJbEpMTFVoZlRUUm9VVkpET1dzeFUxcEdZMEZ1UkRBMVZreFljV1JZUm1kUVZYQXdWbGx0YjJ4eWFqZzlJbjAuZXlKaGNIQWlPaUpqTW1VM05qTTVOUzB6T0dFeExUUTRaamN0WVRsbE1DMWhaamN6TldJNFpqZGpOREVpTENKbGVIQWlPakUzTURFeE5USXdNamNzSW1saGRDSTZNVGN3TVRFMU1URXlOeXdpYVhOeklqb2laR05oY21RaUxDSnFkR2tpT2lKak5UazBZbUZsWWkxaFptRXpMVFJrTnpjdFlURXpZeTAwWXpFME16STJObVJqTmpZaUxDSnpZMjl3WlhNaU9sc2liV1Z0WW1WeUlpd2liV1Z0WW1WeU9uZHlhWFJsSWl3aVpXMWhhV3dpTENKbGJXRnBiRHAzY21sMFpTSXNJbVJsZG1salpTSXNJbVJsZG1salpUcDNjbWwwWlNJc0luQm9iM1J2SWl3aWJtOTBhV1pwWTJGMGFXOXVJaXdpWm05eWRXMGlMQ0ptYjNKMWJUcHpkV0p6WTNKcFltVWlMQ0p3YjNOMElpd2ljRzl6ZERwemRXSnpZM0pwWW1VaUxDSm1ZV05sWW05dmF5SXNJbkJvYjI1bElpd2ljR2h2Ym1VNmRtRnNhV1JoZEdVaUxDSndhRzl1WlRwM2NtbDBaU0lzSW5CbGNuTnZibUVpTENKd1pYSnpiMjVoT25OMVluTmpjbWxpWlNJc0ltTnZibVpwWnlJc0ltTnZibVpwWnpwM2NtbDBaU0lzSW5SdmEyVnVPbkpsZG05clpTSXNJbWxrWTJGeVpDSXNJblJ2Y0dsaklpd2lkRzl3YVdNNmMzVmljMk55YVdKbElpd2labVZsWkRwemRXSnpZM0pwWW1VaUxDSnNiMmRwYmxabGNtbG1hV05oZEdsdmJpSXNJbXh2WjJsdVZtVnlhV1pwWTJGMGFXOXVPblpsY21sbWVTSXNJbU52Ykd4bFkzUnBiMjRpTENKamIyeHNaV04wYVc5dU9uZHlhWFJsSWl3aVpuSnBaVzVrSWl3aVpuSnBaVzVrT25keWFYUmxJaXdpYldWemMyRm5aU0lzSW0xbGMzTmhaMlU2ZDNKcGRHVWlMQ0p3YjJ4c09uZHlhWFJsSWl3aWFXUmxiblJwZEhrNmRtRnNhV1JoZEdWa0lpd2liR2xyWlNJc0luSmxZV04wYVc5dUlpd2ljRzl6ZERwM2NtbDBaU0lzSW1OdmJXMWxiblE2ZDNKcGRHVWlMQ0p5WlhCdmNuUWlMQ0prYjNkdWRtOTBaU0lzSW5CbGNuTnZibUU2ZDNKcGRHVWlMQ0p0WlhOellXZGxPbkJ5YVhaaGRHVWlYU3dpYzJsa0lqb2lNRE0wT0RKa01Ua3RZakkwT0MwME9XSTVMVGd6T0RBdFkyVTNOVFk0TW1SaU5USXlJaXdpYzNWaUlqb2lPVGt5TlRFd01DSjkudXdac28wSHJYTVd0S1pnSkJwVVE5em40by1XdVhseGdJYktWXy1fdnJHTDQzN0ZhVjNubnNpQVhTbi14YS1CQW9rTncwMHZ4elpTeFpfd2ZQX3F1REEiLCJ0b2tlblR5cGUiOiJCZWFyZXIiLCJyZWZyZXNoVG9rZW4iOiIxQklDUCsyMVRvbXB6bHZJUnp0dy9nPT0iLCJleHBpcmVzQXQiOiIyMDIzLTExLTI4VDA2OjEzOjQ3LjAwMFoifQ==; dcard-web-oauth-tk.sig=RWAy15OyD0Xn4FYGoOBW6jttGdY; _ga_DSM1GSYX4C=GS1.1.1701151053.8.1.1701151130.43.0.0"}

response=requests.get(url,headers=headers)
dcard=BeautifulSoup (response.text,"html.parser")
# print(dcard)
dcards=dcard.find_all("div",class_="atm_mk_h2mmj6 wkay9zb")
data_list=[]

for dcardm in dcards:
        data={}
        news = dcardm.find("a",class_="atm_cs_1urozh atm_c8_1csq7v7 atm_g3_1qqjw7d atm_7l_1pday2 atm_1938jqx_1yyfdc7 atm_2zt8x3_stnw88 atm_grwvqw_gknzbh atm_1ymp90q_idpfg4 atm_89ifzh_idpfg4 atm_1hh4tvs_1osqo2v atm_1054lsl_1osqo2v t1gihpsa")
        if news and news.span:
            news = news.span.text
        else:
            news = "無"
        data["最新消息-標題"]=news

        newscaption = dcardm.find("div",class_="atm_d2_1gzgpud atm_ks_15vqwwr m16n7y82")
        if newscaption and newscaption.span:
            newscaption = newscaption.span.text
        else:
            newscaption = "無"
        data["說明"]=newscaption
        
        
        data_list.append(data)
        excel1 = pd.DataFrame(data_list)
        excel1.to_excel("dcard_data.xlsx",index=False,engine="openpyxl")
        
