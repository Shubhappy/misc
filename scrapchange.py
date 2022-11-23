from bs4 import BeautifulSoup as bs, SoupStrainer
import requests, openpyxl
import pandas as pd
import numpy as np
import time


excel=openpyxl.Workbook()
sheet=excel.active
sheet.append(['Product Image Link','Price Tag','Product Category','Product Name', 'Sizes','Description','Product Page Link'])

urllist=[]
list_url=[]
product_list=[]
view_all_link=[]
Navigation=[]
options=[]
description=[]
image=[]
price_tag=[]

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
'https://www.wheelpaints.co.uk/EQUIPMENT/TYRE-BAY-EQUIPMENT-CONSUMABLES/?listings-display=all'
]

#Appending product page link
j=0
while j<len(urllist):
    response3=requests.get(urllist[j])
    parse_div3=SoupStrainer("h3")
    htmlcontent3=response3.content
    soup3 = bs(htmlcontent3,'html.parser',parse_only=parse_div3)    
    j+=1
    # if soup3.find_all('div',class_='info'):
    for link3 in soup3.find_all('a'):
            list_url.append(link3.get('href'))
            # print(link3.get('href'))    

# x=len(list_url)
# print(x)
# print(list_url)


# Adding list of data including product image link, price tag, sizes, description and product page link in excel sheet
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

    for tag in soup4.find_all('p',attrs={'class':"shout2"}):
        price_tag.append(tag.get_text(strip=True))
    print(price_tag)
    
    if soup4.find_all(id='product_image'):
        for imge in soup4.find('div').find_all('link'):
            image.append(imge['href'])
    # print (image)
    
    if soup4.find_all('option'):
        for opt in soup4.find_all('option'): 
            options.append(opt.contents)
        # print(options)

    if soup4.find_all(class_='attribsRadioButton'):
        for opt in soup4.find_all(class_='attribsRadioButton'):
            options.append(opt.contents)
            # print(options)

        
    if soup4.find(id='productDescription'):      
       for des in soup4.find(id='productDescription').find_all('span'):   
            description.append(des.get_text(strip=True))   
          # print(description)  
    
                                                            
    # print([image,price_tag,Navigation,heading,options,description,list_url[k]])
    sheet.append([str(image),str(price_tag),str(Navigation),heading,str(options),str(description),list_url[k]])
    
    options=[]
    Navigation=[]
    description=[]
    image=[]
    price_tag=[]
    
excel.save('wheel9.xlsx')