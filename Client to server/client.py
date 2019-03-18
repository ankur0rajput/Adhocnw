# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:00:37 2019

@author: hp
"""

import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))

client.send("I am a client \n")

from_server=client.recv(4096)

client.close()

print(from_server)
