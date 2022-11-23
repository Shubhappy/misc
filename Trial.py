'''# Define a class as 'student'
class student:

    # Method
    def __init__(self,name,age,gender):

        self.name = name

        self.age = age

        self.gender = gender


# Define a class as 'test' and inherit base class 'student'
class test(student):

    # Method

    def __init__(self,Class,literature,math,biology,physics):

        self.stuClass= Class

        self.literature= literature

        self.math= math

        self.biology=biology

        self.physics=physics


# Define a class as 'marks' and inherit derived class 'test'

class marks(test):

    # Method

    def __init__(self,name, age,gender,Class, literature,math,biology,physics):

        print("\n\nName: ",self.name)

        print("Age: ",self.age)

        print("Gender: ",self.gender)

        print("Study in: ",self.stuClass)

        print("Total Marks: ", self.literature + self.math + self.biology + self.physics)



m1 = marks('Shubham', 35,'male','High school',40,50,60,70)

# Call base class method 'getStudent()'

m1.getStudent()

# Call first derived class method 'getMarks()'

m1.getMarks()

# Call second derived class method 'display()'

m1.display()'''


# Program to define the use of super()

# function in multiple inheritance

'''class GFG1:
    def __init__(self):

        print('HEY !!!!!! GfG I am initialised(Class GEG1)')
  

    def sub_GFG(self, b):

        print('Printing from class GFG1:', b)
  

# class GFG2 inherits the GFG1

class GFG2(GFG1):
    def __init__(self):

        print('HEY !!!!!! GfG I am initialised(Class GEG2)')

        super().__init__()
  

    def sub_GFG(self, b):

        print('Printing from class GFG2:', b)

        super().sub_GFG(b + 1)
  

# class GFG3 inherits the GFG1 ang GFG2 both

class GFG3(GFG2):
    def __init__(self):

        print('HEY !!!!!! GfG I am initialised(Class GEG3)')

        super().__init__()
  

    def sub_GFG(self, b):

        print('Printing from class GFG3:', b)

        super().sub_GFG(b + 1)
  
  

# main function

if __name__ == '__main__':
  

    # created the object gfg

    gfg = GFG3()
  

    # calling the function sub_GFG3() from class GHG3

    # which inherits both GFG1 and GFG2 classes

    gfg.sub_GFG(10)'''




'''import threading


class Thread(threading.Thread):

    def __init__(self, t, *args):

        threading.Thread.__init__(self, target=t, args=args)
        self.start()

count = 0

lock = threading.Lock()

def increment():

    global count 

    lock.acquire()

    try:

        count += 1    

    finally:

        lock.release()
   

def bye():

    while True:
        increment()
        
def hello_there():

    while True:
        increment()

def main():    

    hello = Thread(hello_there)

    goodbye = Thread(bye)
    

    while True:

        print count


if __name__ == '__main__':
    main()'''

'''
from dash import Dash, html, dcc
import pandas as pd

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Avocado Analytics",),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)'''

# import pandas as pd
# df=pd.read_csv('Madhya Pradesh Population Data.csv')
# print(df.set_index("State/City").apply(list, 1).to_dict())

# from bs4 import BeautifulSoup as bs, SoupStrainer
# import requests, openpyxl
# import pandas as pd
# import numpy as np

# excel=openpyxl.Workbook()
# sheet=excel.active
# sheet.append(['Products & Categories','Name','Sizes', 'Description','More Info'])

# Navigation=[]
# n=0
# options=[]



# list_url=['https://www.wheelpaints.co.uk/ALLOY-WHEEL-MAIN-SILVERS/Solvent-Basecoat.Html?cPath=253_256','https://www.wheelpaints.co.uk/index.php?main_page=product_info&cPath=254_255&products_id=859']

# x=len(list_url)

# for k in range(0,x):
#     response4=requests.get(list_url[k])
#     parse_div4=SoupStrainer("div",attrs={'id':'main'})
#     # parse_div4=SoupStrainer("div",attrs={'class':'productContainer'})
#     htmlcontent4=response4.content
#     soup4 = bs(htmlcontent4,'html.parser',parse_only=parse_div4)
        
#     # heading.append(soup4.h1.contents)
#     # print(heading)
#     for nav in soup4.find(id='navBreadCrumb').find_all('div'):
#         Navigation.append(nav.get_text(strip=True))
#     # print(Navigation)

    
    
#     heading=str(soup4.h1.contents)
        
#     for opt in soup4.find_all('option'):
#             options.append(opt.contents)
#         # print(options)

#     l=len(list_url)
#     for k in range(0,l):
#         response5=requests.get(list_url[k])
#         parse_div5=SoupStrainer("div",attrs={'id':'productDescription'})
#         htmlcontent5=response5.content
#         soup5 = bs(htmlcontent5,'html.parser',parse_only=parse_div5)
#         # l+=1
            
#         # description.append(soup5.get_text(" → ",strip=True))
#     # print(description)
        
#         description=soup5.get_text(" , ",strip=True)
#         while n<len(Navigation):
                    
#             break
#     print([Navigation,heading,options,description,list_url[k]])
#     sheet.append([str(Navigation),heading,str(options),description,list_url[k]])
#     n+=1    
#     options=[]
# excel.save('wheel.xlsx')


from bs4 import BeautifulSoup as bs, SoupStrainer
import requests, openpyxl
import pandas as pd
import numpy as np
import time


excel=openpyxl.Workbook()
sheet=excel.active
sheet.append(['Image','Product Category','Product Name', 'Sizes','Description','More Info'])

urllist=[]
list_url=[]
product_list=[]
view_all_link=[]
Navigation=[]
options=[]
description=[]
image=[]

# url="https://www.wheelpaints.co.uk/"


# list_url=[]
# parse_div1=SoupStrainer("div",attrs={'id':'nav-cat'})
# response1=requests.get(url)
# htmlcontent1=response1.content
# soup1 = bs(htmlcontent1,'html.parser',parse_only=parse_div1)

# for link in soup1.find_all('a'):
#     list_url.append(link.get('href'))

# time.sleep(2)

# #Getting view all link from each page
# i=0
# while i<len(list_url):
#     response2=requests.get(list_url[i])
#     parse_div2=SoupStrainer("a",attrs={'style':'margin: 0 0 0 6px;'})
#     htmlcontent2=response2.content
#     soup2 = bs(htmlcontent2,'html.parser',parse_only=parse_div2)
#     i+=1
#     for link2 in soup2.find_all('a'):
#         view_all_link.append(link2.get('href'))

# list_url.extend(view_all_link)
# time.sleep(5)


urllist=[
   'https://www.wheelpaints.co.uk/ALLOY-WHEEL-MAIN-SILVERS/Solvent-Basecoat.Html?cPath=253_256',
'https://www.wheelpaints.co.uk/index.php?main_page=product_info&cPath=254_255&products_id=859',
'https://www.wheelpaints.co.uk/ALLOY-WHEEL-WET-PAINTS-COLOURS/?listings-display=all',
'https://www.wheelpaints.co.uk/ALLOY-WHEEL-MAIN-SILVERS/?listings-display=all',
'https://www.wheelpaints.co.uk/CAR-MANUFACTURERS-COLOURS-/?listings-display=all',
'https://www.wheelpaints.co.uk/CLEARCOATS-ACTIVATOR-THINNERS/CLEARCOATS-ACTIVATOR-PRIMERS-/?listings-display=all',
'https://www.wheelpaints.co.uk/Powder-Coating-Products/?listings-display=all',
'https://www.wheelpaints.co.uk/DIAMOND-CUT-TINTS-/?listings-display=all',
'https://www.wheelpaints.co.uk/EQUIPMENT/?listings-display=all',
'https://www.wheelpaints.co.uk/CHEMICAL-STRIPPING-TANKS/?listings-display=all',
'https://www.wheelpaints.co.uk/Masking-Spraying-Accessories/Masking-Spraying-Accessories/?listings-display=all',
'https://www.wheelpaints.co.uk/AEROSOLS/?listings-display=all',
'https://www.wheelpaints.co.uk/PPE-ABRASIVES-POLISHING/?listings-display=all',
'https://www.wheelpaints.co.uk/EQUIPMENT/TYRE-BAY-EQUIPMENT-CONSUMABLES/?listings-display=all',

]

#Getting more info link from page

j=0
while j<len(urllist):
    response3=requests.get(urllist[j])
    parse_div3=SoupStrainer("ul",attrs={'id':"listings-product"})
    htmlcontent3=response3.content
    soup3 = bs(htmlcontent3,'html.parser',parse_only=parse_div3)
    j+=1
    for link3 in soup3.find_all('a'):
        list_url.append(link3.get('href'))


x=len(list_url)
print(x)

for k in range(0,x):
    response4=requests.get(list_url[k])
    parse_div4=SoupStrainer("div",attrs={'id':'main'})
    htmlcontent4=response4.content
    soup4 = bs(htmlcontent4,'html.parser',parse_only=parse_div4)

    
    for imge in soup4.find('div').find_all('link'):
        image.append(imge['href'])
    # print (image)
    
    for nav in soup4.find(id='navBreadCrumb').find_all('div'):
        Navigation.append(nav.get_text(strip=True))
    # print(Navigation)
    
    heading=str(soup4.h1.contents)
    # print(heading)
        
    for opt in soup4.find_all("label"):
        options.append(opt.get_text(strip=True))
        # print(options)

    if soup4.find(id='productDescription'):      
        for des in soup4.find(id='productDescription').find_all('span'):    
            description.append(des.get_text(strip=True))
    # print(description)            
    
    print([image,Navigation,heading,options,description,list_url[k]])
    sheet.append([str(image),str(Navigation),heading,str(options),str(description),list_url[k]])
   
    time.sleep(2)

    options=[]
    Navigation=[]
    description=[]
    image=[]
excel.save('wheel7.xlsx')

# list_url='https://www.wheelpaints.co.uk/Powder-Coating-Products/Colours/ALLOY-GREEN-POWDER.Html?cPath=8_49'
# response3=requests.get(list_url)
# parse_div3=SoupStrainer("div",attrs={'id':'main'})
# htmlcontent3=response3.content
# soup3 = bs(htmlcontent3,'html.parser',parse_only=parse_div3)
# # print(soup3.prettify())

# for imge in soup3.find(id='product_image').find_all('link'):
#     image.append(imge['href'])
#     print (image)

            


