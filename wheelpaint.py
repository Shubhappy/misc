from bs4 import BeautifulSoup as bs, SoupStrainer
import requests, openpyxl
import pandas as pd
import re
# excel=openpyxl.Workbook()
# sheet=excel.active
# sheet.append(['','', '', '',''])

# list_url=[]
# infolink=[]

# url="https://www.wheelpaints.co.uk/"

# response=requests.get(url)
# parse_only=SoupStrainer("ul",attrs={'class':'level2'})

# htmlcontent=response.content
# soup = bs(htmlcontent,'html.parser',parse_only=parse_only)

# for link in soup.find_all('a'):
#     list_url.append(link.get('href'))

# list_url.append('https://www.wheelpaints.co.uk/CHEMICAL-STRIPPING-TANKS/')
# list_url.append('https://www.wheelpaints.co.uk/AEROSOLS/')
# # print(list_url)
# # print(len(list_url))

# #Getting all products link inside sub-categories link from 3rd product's subcategory to last products's category
# parse_div=SoupStrainer("div",attrs={'class':'sale-buttons'})
# souplist=[]
# for j in range(2,3):
#     response=requests.get(list_url[j])
#     htmlcontent1=response.content
#     soup1 = bs(htmlcontent1,'html.parser',parse_only=parse_div)
#     souplist.append(soup1)
    
# for n in souplist:  
#     for link in n.find_all('a'):
#         infolink.append(link.get('href'))
# # print(infolink)
# # k=len(infolink)
# # print(len(infolink))

# #Getting data of product information page navigated through more info link
# # parse_container=SoupStrainer("select")
# parse_container=SoupStrainer('div','')
# for i in range(0,1):
#     response1=requests.get(infolink[i])
#     infocontent=response1.content
#     soup2= bs(infocontent,'html.parser',parse_only=parse_container)
#     print(soup2)




url="https://www.wheelpaints.co.uk/CAR-MANUFACTURERS-COLOURS/CAR-MAN-DIAMOND-CUT-COLOURS/"

response=requests.get(url)
parse_div=SoupStrainer("a",attrs={'style':'margin: 0 0 0 6px;'})

htmlcontent=response.content
soup = bs(htmlcontent,'html.parser',parse_only=parse_div)

for link in soup.find_all('a'):
    print(link.get('href'))

# list_url=[]
# souplist=[]
# for j in range(0,164):
#     response=requests.get(list_url[j])
#     htmlcontent1=response.content
#     soup1 = bs(htmlcontent1,'html.parser',parse_only=parse_div)
#     souplist.append(soup1)
    
# for n in souplist:  
#     for link in n.find_all('a'):
#         infolink.append(link.get('href'))
# # print(infolink)
# # k=len(infolink)
# # print(len(infolink))

# #Getting data of product information page navigated through more info link
# # parse_container=SoupStrainer("select")
# parse_container=SoupStrainer('div','')
# for i in range(0,1):
#     response1=requests.get(infolink[i])
#     infocontent=response1.content
#     soup2= bs(infocontent,'html.parser',parse_only=parse_container)
#     print(soup2)