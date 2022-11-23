from bs4 import BeautifulSoup as bs, SoupStrainer
import requests, openpyxl
import pandas as pd
import numpy as np
import time

excel=openpyxl.Workbook()
sheet=excel.active
sheet.append(['Product Category','Product Name', 'Sizes','Description','More Info'])


product_list=[]
view_all_link=[]
Navigation=[]
options=[]
description=[]

url="https://www.wheelpaints.co.uk/"

#------------------------------------------------------------------------------------------------------
# Program to get product list
# parse_div=SoupStrainer("li",attrs={'class':'submenu'})
# response=requests.get(url)
# htmlcontent=response.content
# soup = bs(htmlcontent,'html.parser',parse_only=parse_div)
# j=0
# while j<12:    
#     for i in soup.ul:
#         j+=1
#         soup.ul.decompose()

# soup.get_text(strip=False)
# for string in soup.stripped_strings:
#     product_list.append(repr(string))
# product_list.insert(9, 'CHEMICAL STRIPPING TANKS')
# product_list.insert(11, 'AEROSOLS')                       #List of all products
# print(product_list)
#------------------------------------------------------------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Program to get link of all products and sub-categories
list_url=[]
parse_div1=SoupStrainer("div",attrs={'id':'nav-cat'})
response1=requests.get(url)
htmlcontent1=response1.content
soup1 = bs(htmlcontent1,'html.parser',parse_only=parse_div1)

for link in soup1.find_all('a'):
    list_url.append(link.get('href'))

time.sleep(2)

#Getting view all link from each page
i=0
while i<len(list_url):
    response2=requests.get(list_url[i])
    parse_div2=SoupStrainer("a",attrs={'style':'margin: 0 0 0 6px;'})
    htmlcontent2=response2.content
    soup2 = bs(htmlcontent2,'html.parser',parse_only=parse_div2)
    i+=1
    for link2 in soup2.find_all('a'):
        view_all_link.append(link2.get('href'))

list_url.extend(view_all_link)
time.sleep(5)

#Getting more info link from page
moreinfo_link=[]
j=0
while j<len(list_url):
    response3=requests.get(list_url[j])
    parse_div3=SoupStrainer("div",attrs={'class':'info'})
    htmlcontent3=response3.content
    soup3 = bs(htmlcontent3,'html.parser',parse_only=parse_div3)
    j+=1
    for link3 in soup3.find_all('a'):
        moreinfo_link.append(link3.get('href'))
    time.sleep(2)

list_url.extend(moreinfo_link)
# print(list_url)
# print(len(list_url))

# #Getting all unique links
# x = np.array(list_url)
# # print(np.unique(x))
# uniq_url=list(np.unique(x))
# print(uniq_url)
# print(len(uniq_url))


x=len(list_url)
print(x)

for k in range(0,x):
    response4=requests.get(list_url[k])
    parse_div4=SoupStrainer("div",attrs={'id':'main'})
    htmlcontent4=response4.content
    soup4 = bs(htmlcontent4,'html.parser',parse_only=parse_div4)
    
    for nav in soup4.find(id='navBreadCrumb').find_all('div'):
        Navigation.append(nav.get_text(strip=True))
    # print(Navigation)
    
    heading=str(soup4.h1.contents)
    # print(heading)

    for opt in soup4.find_all('option'):
        options.append(opt.contents)
        # print(options)

    if soup4.find(id='productDescription'):      
        for des in soup4.find(id='productDescription').find_all('p'):    
            description.append(des.get_text(strip=True))
    # print(description)         
      
    print([Navigation,heading,options,description,list_url[k]])
    sheet.append([str(Navigation),heading,str(options),str(description),list_url[k]])
   
    time.sleep(2)

    options=[]
    Navigation=[]
    description=[]
excel.save('wheel2.xlsx')