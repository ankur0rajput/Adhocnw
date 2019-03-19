# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:00:37 2019

@author: hp
"""

import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345				

# connect to the server on local computer 
s.connect(('127.0.0.1', port))

print (s.recv(1024))
data_1=input()
str(data_1).encode("utf-8")
s.send(data_1)

print (s.recv(1024))
data_2=input()
str(data_2).encode("utf-8")
s.send(data_2)

s.close()
