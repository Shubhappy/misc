from bs4 import BeautifulSoup as bs, SoupStrainer
import requests, openpyxl
import pandas as pd

# excel=openpyxl.Workbook()
# sheet=excel.active
# sheet.append(['','', '', '',''])

# linkpagelist=[]
# internallink=[]
# link=[]
product_list=[]
view_all_link=[]

url="https://www.wheelpaints.co.uk/"

#------------------------------------------------------------------------------------------------------
# Program to get product list
parse_div=SoupStrainer("li",attrs={'class':'submenu'})
response=requests.get(url)
htmlcontent=response.content
soup = bs(htmlcontent,'html.parser',parse_only=parse_div)
j=0
while j<12:    
    for i in soup.ul:
        j+=1
        soup.ul.decompose()

soup.get_text(strip=False)
for string in soup.stripped_strings:
    product_list.append(repr(string))
product_list.insert(9, 'CHEMICAL STRIPPING TANKS')
product_list.insert(11, 'AEROSOLS')                       #List of all products
# print(product_list)
#------------------------------------------------------------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Program to get sub category product list
subproduct_list=[]
parse_div1=SoupStrainer("ul",attrs={'class':'level2'})
response1=requests.get(url)
htmlcontent1=response1.content
soup1 = bs(htmlcontent1,'html.parser',parse_only=parse_div1)

soup1.get_text(strip=False)
# print(soup.get_text(strip=False))
for string in soup1.stripped_strings:
    subproduct_list.append(repr(string))

# for string in soup1.stripped_strings:                  #If want to skip sale category, use this code
#     if string=='SALE':
#         continue
#     else:
#         subproduct_list.append(repr(string))
print(subproduct_list)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#*****************************************************************************************************
# Program to get links of all products listed under sub-category product
# url_list=[]
# parse_div2=SoupStrainer("ul",attrs={'class':'level2'})
# response2=requests.get(url)
# htmlcontent2=response2.content
# soup2 = bs(htmlcontent2,'html.parser',parse_only=parse_div2)
# for link in soup2.find_all('a'):
#     url_list.append(link.get('href'))
# url_list.insert(39, 'https://www.wheelpaints.co.uk/CHEMICAL-STRIPPING-TANKS/')
# url_list.insert(44, 'https://www.wheelpaints.co.uk/AEROSOLS/')
# # print(len(url_list))

# i=0
# while i<len(url_list):
#     # print(i)
   
#     response3=requests.get(url_list[i])
#     parse_div3=SoupStrainer("a",attrs={'style':'margin: 0 0 0 6px;'})
#     htmlcontent3=response3.content
#     soup3 = bs(htmlcontent3,'html.parser',parse_only=parse_div3)
#     i+=1
#     for link1 in soup3.find_all('a'):
#         view_all_link.append(link1.get('href'))
# print(view_all_link)

# url_list.extend(view_all_link)

# k=0
# while k<len(view_all_link):
#     response4=requests.get(view_all_link[k])
#     parse_div4=SoupStrainer("a",attrs={'style':'margin: 0 0 0 6px;'})
#     htmlcontent4=response4.content
#     soup4 = bs(htmlcontent4,'html.parser',parse_only=parse_div4)
#     i+=1

    

