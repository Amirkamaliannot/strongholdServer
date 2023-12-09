# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:20:01 2023

@author: test
"""

import socket
import time
import threading
import time




# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.82.84', 25641))
server_socket.listen()
print('Waiting for client connection...')


def handle_proxy_outbound(client_socket):
    while True:
        client_socket.send(b'Hello, world!\n')
        time.sleep(3)
        
def handle_proxy_inbound(client_socket):
    while True:
        data = client_socket.recv(1024)
        print(f'Received data : {data.decode()}')


client_list=[]
while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')
    client_list.append((client_socket, client_address))
    
    print(client_list)
    

    # Create a new thread to handle the client request
    client_thread_ = threading.Thread(target=handle_proxy_inbound, args=(client_socket,))
    client_thread = threading.Thread(target=handle_proxy_outbound, args=(client_socket,))
    client_thread_.start()
    client_thread.start()




