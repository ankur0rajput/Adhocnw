# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 07:47:48 2019

@author: hp
"""
import socket

s = socket.socket()
port = 12345

s.bind(('', port))

s.listen(5)

while True: 

# Establish connection with client. 
    c, addr = s.accept()	 
    #print ('Got connection from', addr) 

# send a thank you message to the client. 
    c.send('Enter the email')
    data_1=c.recv(1024)
    data_1=data_1.decode("utf-8")
    
    if data_1=="ankur":
        c.send('Enter the password')
        data_2=c.recv(1024)
        data_2=data_2.decode("utf-8")
        if data_2=="kumar":
            c.send("connection established")
            c.close()
        else:
            c.send("not valid")
            c.close()
    else:
        c.send("not valid")
        c.close() 
