# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:19:19 2023

@author: test
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:27:30 2023

@author: Amir
"""

import socket
import struct
import scapy.all as scapy

import random
import threading
    
    
#######
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
game_host_ip =s.getsockname()[0]
s.close()
del s
#######


ip_ng = game_host_ip.split('.')[:3] + [str(random.randint(1, 255))]
random_ip = ".".join(ip_ng)

print(f'random IP : {random_ip}')

proxy_ip='192.168.52.84'
client_list = {};

def filter_game_packets(port, src):
    if(((port >= 2300 and port <= 2400) or port==47624) and src==game_host_ip):
        return True
    else:
        return False
    
    
    
    
    
    

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((proxy_ip, 62254))
print(f"Connected to {proxy_ip}:{62254}")





def send_data_loop_back(sock):
    
    while(True):
        print('give')
        data = sock.recv(1024)
        if not data:
            # Client has closed the connection
            print("Connection closed")
            break
        
        ip= scapy.IP(data)
        
        ip[scapy.IP].src = random_ip
        ip[scapy.IP].dst= game_host_ip
        
        pack = ip
        pack.show()
        scapy.send(pack)

loopback_forward = threading.Thread(target=send_data_loop_back, args=(sock,))
loopback_forward.start()

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

s.bind((game_host_ip,0))



# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
n=1

while(n<=100):
    # print('Number ', n)
    data=s.recvfrom(65565)
    packet=data[0]
    address= data[1]
    header=struct.unpack('!BBHHHBBHBBBBBBBB', packet[:20])
    
    
    if(header[6]==6): #header[6] is the field of the Protocol
    
        src_port = struct.unpack('!H', packet[20:22])[0]
        dst_port = struct.unpack('!H', packet[22:24])[0]
        src_address = socket.inet_ntoa(packet[12:16])
        dst_address = socket.inet_ntoa(packet[16:20])
        if(filter_game_packets(dst_port, src_address)):
            if(src_address != proxy_ip):
                
                print("Protocol = TCP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
                sock.sendall(packet)
            
            
            
    if(header[6]==17):
        
        # print(binascii.hexlify(bytes(packet)).decode('utf-8'))
        src_port = struct.unpack('!H', packet[20:22])[0]
        dst_port = struct.unpack('!H', packet[22:24])[0]
        
        # user_id = get_packet_data(packet, 'ip_id')
        
        src_address = socket.inet_ntoa(packet[12:16])
        dst_address = socket.inet_ntoa(packet[16:20])

        
        if(filter_game_packets(dst_port, src_address)):
            
            print("Protocol = UDP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
            sock.sendall(packet)
        
    n=n+1

sock.close()
