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
    print ('Got connection from', addr) 
    data_1=b'Enter the email'
    c.send(data_1)
    data_2=c.recv(1024)
    data_2=data_2.decode("utf-8")
    
    if data_2=="ankur":
        data_3=b'Enter the password'
        #data_3.encode("utf-8")
        c.send(data_3)
        
        #data_69=bytes(data_2, 'utf-8')
        #c.send(data_69)
        data_4=c.recv(1024)
        data_4=data_4.decode("utf-8")
        if data_4=="kumar":
            data_5=b'connection established'
            #data_5.encode("utf-8")
            c.send(data_5)
            c.close()
        else:
            c.send(b'not valid')
            c.close()
    else:
        c.send(b'not valid')
        c.close() 
