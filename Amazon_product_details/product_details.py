#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  18 12:18:01 2019

@author: ankur
"""   
#import all the required modules
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import warnings
from requests_html import HTMLSession

session = HTMLSession()

#ignore warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

#uniqueue id of user's searched product   or we can directly use the url to access the page  
asin_array=['B0756CYWWD'] 

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }
all_items=[] #The final 2D list containing prices and details of products

for asin in asin_array:
    item_array=[] #An array to store details of a single product.
    amazon_url="https://www.amazon.com/dp/"+asin
    response = session.get(amazon_url, headers=headers, verify=False) 
    item_array.append(response.html.search('a-color-price">${}<')[0]) #Extracting the price

    #Extracting the text containing the product details
    details=(response.html.search('P.when("ReplacementPartsBulletLoader").execute(function(module){ module.initializeDPX(); }){}</ul>;')[0])
    details_arr=[] 
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


