# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:09:04 2023

@author: test
"""

import socket
from time import sleep 

#######
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local =s.getsockname()[0]
s.close()
del s
#######

# Define the server address and port
SERVER_ADDRESS = (local, 62254)

# Create a TCP socket and bind it to the server address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)

# Listen for incoming connections
server_socket.listen()

print(f'Server listening on {SERVER_ADDRESS}')

while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')

    # Receive data from the client
    data = client_socket.recv(1024)
    while data:
                                                      
                                                                                                # Print the data received
        # print(f'Received data from {client_address}: {data.decode()}')
        # data = client_socket.recv(1024)
        sleep(5)
        # client_socket.send(b'hello bitch')
        client_socket.sendall(b"data")

# Close the client connection
client_socket.close()