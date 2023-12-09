# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:43:07 2023

@author: Amir
"""

import struct
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

###########################
def filter_game_packets(port, src):
    if(port >= 0 and port <= 55000):# or port==47624) and src==game_host_ip):
        return True
    else:
        return False
    

###########################
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

s.bind((local,0))



# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
n=1
############################

while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')



    # Receive data from the client
    # data = client_socket.recv(1024)
    # while True:
                                                      
    #                                                                                             # Print the data received
    #     # print(f'Received data from {client_address}: {data.decode()}')
    #     # data = client_socket.recv(1024)

    #     # client_socket.send(b'hello bitch')
    #     sleep(1)
    #     print(10)
    #     client_socket.sendall(b"data")
    # create a raw socket and bind it to the public interface

    #################################3
    while(n<=100):
        # print('Number ', n)
        data=s.recvfrom(65565)
        print('recive')
        packet=data[0]
        address= data[1]
        header=struct.unpack('!BBHHHBBHBBBBBBBB', packet[:20])
        
        
        if(header[6]==6): #header[6] is the field of the Protocol
        
            src_port = struct.unpack('!H', packet[20:22])[0]
            dst_port = struct.unpack('!H', packet[22:24])[0]
            src_address = socket.inet_ntoa(packet[12:16])
            dst_address = socket.inet_ntoa(packet[16:20])
            if(filter_game_packets(dst_port, src_address)):
                if(src_address != local):
                    
                    print("Protocol = TCP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
                    client_socket.sendall(packet)
                
                
                
        if(header[6]==17):
            
            # print(binascii.hexlify(bytes(packet)).decode('utf-8'))
            src_port = struct.unpack('!H', packet[20:22])[0]
            dst_port = struct.unpack('!H', packet[22:24])[0]
            
            # user_id = get_packet_data(packet, 'ip_id')
            
            src_address = socket.inet_ntoa(packet[12:16])
            dst_address = socket.inet_ntoa(packet[16:20])

            
            if(filter_game_packets(dst_port, src_address)):
                
                print("Protocol = UDP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
                client_socket.sendall(packet)
            
        n=n+1


# Close the client connection
client_socket.close()