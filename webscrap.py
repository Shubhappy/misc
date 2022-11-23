from bs4 import BeautifulSoup as bs
import requests, openpyxl
import pandas as pd

excel=openpyxl.Workbook()
sheet=excel.active
sheet.append(['Name of Athlete','Sponsors', 'University', 'Sport','More Info'])

url='https://nilcollegeathletes.com/athletes'


# For getting the url of all pages
list=['https://nilcollegeathletes.com/athletes']
for i in range(2,3):
    list.append(url+"?page="+str(i))  #Getting list of all pages

about=[]
linkinfodata=[]
souplist=[]
addinfo=[]
infolink=[]
name=[]
sponsors=[]
university=[]
sport=[]

for j in range(0,1):
    response=requests.get(list[j])
    htmlcontent=response.content
    soup = bs(htmlcontent,'html.parser')   
    data=soup.find('tbody',class_='bg-white divide-y divide-gray-200').find_all('tr')
    for n in data:
        name=n.find('td',class_='px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900').a.text #Find athlete name
        sponsors=n.find('td',class_='px-6 py-4 whitespace-nowrap').ul.text # Find sponsor name
        university=n.find('td',class_='hidden sm:table-cell px-6 py-4 max-w-xs whitespace-nowrap text-sm text-gray-900').span.text # Find university name
        sport=n.find('td',class_='hidden lg:table-cell px-6 py-4 whitespace-nowrap').ul.text # Find sport name
       
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       
#Code to get About details inside 'More Info' link

for k in range(0,1):                        #8391
        req=requests.get(list[k])
        multi_page=req.content
        soup = bs(multi_page,'html.parser')
        # product=soup.find('tbody',class_='bg-white divide-y divide-gray-200').find_all('tr')
            
        souplist.append(soup)


# for link in soup.find_all(class_='flex text-blue-600 hover:text-blue-900'):
for n in souplist:  
    for link in n.find_all(class_='flex text-blue-600 hover:text-blue-900'):
        infolink.append(link.get('href'))
                # for l in range(0,1):
                #     additionalinfo=requests.get(infolink[l])
                #     addhtmlcontent=additionalinfo.content
                #     soup=bs(addhtmlcontent,'html.parser')
                #     # for abt in soup.find_all(class_='mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2'):
                #     #     addinfo.append(abt.get('string'))
# print(infolink)

for m in range(0,20):
    getlinkdata=requests.get(infolink[m])
    linkcontent=getlinkdata.content
    linksoup=bs(linkcontent,'html.parser')
    linkinfodata.append(linksoup)

for y in linkinfodata:
    for abtdata in y.find_all(class_='mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2'):
        if abtdata.string != None:
            if len(abtdata.string)>30:
                print(abtdata.string)








##############################################################################

        # print([name,sponsors,university,sport])
        # sheet.append([name,sponsors,university,sport])


# for k in range(0,2):                        #8391
#     req=requests.get(list[k])
#     multi_page=req.content
#     soup = bs(multi_page,'html.parser')
#     # product=soup.find('tbody',class_='bg-white divide-y divide-gray-200').find_all('tr')
#     for link in soup.find_all(class_='flex text-blue-600 hover:text-blue-900'):
#         print(link.get('href'))

#         info.append(link.get('href'))
#         sheet.append([info])

# excel.save('Athlete Data4.xlsx')

##############################################################################







# print(soup)
    # data.append(soup.find('td',class_="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",attrs={'class':'hover:underline hover:text-blue-700'}).a.text)             #.find_all('a',class_='hover:underline hover:text-blue-700',href=True))

    # data.append(soup.find_all('a',class_='hover:underline hover:text-blue-700',href=True))     # for loop to be run on it

    # for d in soup.find_all('tbody',class_='bg-white divide-y divide-gray-200'):
    #     # data=d.find('a',attrs={'class':'hover:underline hover:text-blue-700'})
    #     data=d.find()
    #     print(data.string)

    # data=soup.find('tbody',class_='bg-white divide-y divide-gray-200').find_all('tr')
    # print (data)
    # for n in data:
    #     # name=n.find('td',class_='hover:underline hover:text-blue-700').a.text
    #     print(n)

    # for link in soup.find_all(class_='flex text-blue-600 hover:text-blue-900'):
    #     product.append(link.get('href'))   # Getting more info links from tables of all pages
# print(product)
# print(data)
# print(soup.prettify())
# print(htmlcontent)




# multicontent=[]
# for k in range(0,2):                        #8391
#     req=requests.get(product[k])
#     multi_page=req.content
#     soup = bs(multi_page,'html.parser')
#     multicontent.append(soup)

# print(multicontent)


# # Html
# html_source = '<a class="1" href="https://ex.com/home">Converting File Size in Python</a>'


# # BeautifulSoup
# soup = bs(html_source, 'html.parser')

# # Find element by class which have href attr
# el = soup.find(class_='1', href=True)

# # Print href value
# print(el['href'])





# for j in list:

# URL = ['https://www.geeksforgeeks.org','https://www.geeksforgeeks.org/page/10/']
  
# for url in range(0,2):
#     req = requests.get(URL[url])
#     soup = bs(req.text, 'html.parser')
# print(soup)
    # titles = soup.find_all('div',attrs={'class','head'})
    # for i in range(4, 19):
    #     if url+1  > 1:
    #         print(f"{(i - 3) + url * 15}" + titles[i].text)
    #     else:
    #         print(f"{i - 3}" + titles[i].text)







# response = requests.get(url)
# htmlcontent = response.content
# soup = BeautifulSoup(htmlcontent, 'html.parser')

# weblink= soup.find_all('div',attrs = {'class','head'})

# for link in soup.find_all('a'):
#     print(link.get('href'))

# URL = 'https://www.geeksforgeeks.org/page/'
  
# for page in range(1,10):
#       # pls note that the total number of
#     # pages in the website is more than 5000 so i'm only taking the
#     # first 10 as this is just an example
  
#     req = requests.get(URL + str(page) + '/')
#     soup = bs(req.text, 'html.parser')
  
#     titles = soup.find_all('div',attrs={'class','head'})
  
#     for i in range(4,19):
#         if page>1:
#             print(f"{(i-3)+page*15}" + titles[i].text)
#         else:
#             print(f"{i-3}" + titles[i].text)

