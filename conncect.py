# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:25:30 2023

@author: test
"""

import socket
import threading
import time


# Set up the client socket

proxy_server = ('192.168.82.84', 25641)
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.connect(proxy_server)

game_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
game_socket.connect(('192.168.82.84', 8000))


# def 

def recive_proxy_data(x):
    while True:
        data = proxy_socket.recv(1024)
        print('312dsa')
        if not data:
            break
        print(data.decode())
        game_socket.send(data)
        
def recive_game_data(x):
    while True:
        data = game_socket.recv(1024)
        if not data:
            break
        print(data.decode())
        proxy_socket.send(data)
        
        
recive_proxy_data_ = threading.Thread(target=recive_proxy_data, args=(1,))
recive_game_data_ = threading.Thread(target=recive_game_data, args=(1,))

recive_proxy_data_.start()
recive_game_data_.start()
    
    




# Clean up the socket
# game_socket.close()
# proxy_socket.close()



