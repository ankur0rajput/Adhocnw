# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 07:47:48 2019

@author: hp
"""

import socket
serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
while True:
    conn,addr =serv.accept()
    from_client=''
    while True:
        attempts=0
        while attempts<3:
            username=input('username?')
            password=input('password?')
            if username=='correctusername'and password=='correctpassword':
                print("you are in!")
                data=conn.recv(4096)
                if not data:
                    break
                from_client += data
                print(from_client)
        
                conn.send("I am a server \n")                
            else:
                attempts += 1
                print("incorrect!")
                if attempts==3:
                    print("too many attempts")            
    conn.close()
    print("client disconnected")
    
    
