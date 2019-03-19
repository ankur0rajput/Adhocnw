#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  18 10:18:01 2019

@author: ankur
"""
#Baic way to extract deatails
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup    
import urllib.request
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('https://www.amazon.in/dp/B079WC1HZV/ref=sspa_dk_detail_2?psc=1')
bsobj=BeautifulSoup(response,"lxml")    

#Name
name=bsobj.findAll("span","a-size-large")
for i in name:
    print(i.get_text())


#some details    
d=[]
x =bsobj.findAll("ul",{"class":"a-unordered-list a-vertical a-spacing-none"})
z=BeautifulSoup(str(x)[1:-1],"lxml")
q=z.findAll("span","a-list-item")

for i,name in enumerate(q):
    d.append(name.get_text())
    print(i,d[i])
    print('\n')
