#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  18 10:18:01 2019

@author: ankur
"""

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup    
import urllib.request
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
d=[]
opener = AppURLopener()
response = opener.open('https://www.amazon.in/dp/B079WC1HZV/ref=sspa_dk_detail_2?psc=1')
bsobj=BeautifulSoup(response,"lxml")

x =bsobj.findAll("ul",{"class":"a-unordered-list a-vertical a-spacing-none"})
z=BeautifulSoup(str(x)[1:-1],"lxml")
q=z.findAll("span","a-list-item")

for i,name in enumerate(q):
    d.append(name.get_text())
    print(i,d[i])
    print('\n')

#Name
name=bsobj.findAll("span","a-size-large")
for i in name:
    print(i.get_text())


    
    
    

    
    
    
    
    
#2nd way to do so    
    
    
#import all the required modules
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import warnings
from requests_html import HTMLSession

#declare a session object
session = HTMLSession()

#ignore warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

#uniqueue id of user's searched product   or we can directly use the url to access the page  
asin_array=['B0756CYWWD'] 
#The ASIN Number will be between the dp/ and another /
start = 'dp/'
end = '/'


#declare the header.
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }
all_items=[] #The final 2D list containing prices and details of products

for asin in asin_array:
    item_array=[] #An array to store details of a single product.
    amazon_url="https://www.amazon.com/dp/"+asin #The general structure of a url
    response = session.get(amazon_url, headers=headers, verify=False) #get the response
    item_array.append(response.html.search('a-color-price">${}<')[0]) #Extracting the price

    #Extracting the text containing the product details
    details=(response.html.search('P.when("ReplacementPartsBulletLoader").execute(function(module){ module.initializeDPX(); }){}</ul>;')[0])
    details_arr=[] #Declaring an array to store individual details
    details=re.sub("\n|\r", "", details) #Separate the details from text
    details_arr=re.findall(r'\>(.*?)\<', details) #Store details in the array.
    for i,row in enumerate(details_arr):
        details_arr[i]=row.replace("\t","") #Remove tabs from details
    details_arr=list(filter(lambda a: a != '', details_arr)) #Remove empty spaces.
    details_arr=[row.strip() for row in details_arr] #Remove trailing and starting spaces.

    #Store the details with the price in the same row
    for row in details_arr:
        item_array.append(row)
    #Append this array to the master-array of items
    all_items.append(item_array)


