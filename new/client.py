# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:22:20 2023

@author: test
"""
import socket
import scapy.all as scapy
import random
import threading
import struct

#######
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
proxy_ip =s.getsockname()[0]
s.close()
del s
#######


ip_ng = proxy_ip.split('.')[:3] + [str(random.randint(1, 255))]
random_ip = ".".join(ip_ng)


print(f'Random ip : {random_ip}')

def send_data_loop_back(conn):
    
    while(True):
        data = conn.recv(1024)
        conn.sendall( b'E\x00\x00P\x8bB\x00\x00\x80\x11\xc4\xec\xc0\xa84N\xc0\xa84\xcf\xd0a\xba\x08\x00<&\xe94\x00\xb0\xfa\x02\x00\x08\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00play\x02\x00\x0e\x00\xf0M\x0cI\xc7\x9bLL\xb9Y\xd4\x1f\x1c\xceF\x0e\x00\x00\x00\x00\x91\x00\x00\x00')
        
        if not data:
            # Client has closed the connection
            print(f"Connection closed by {addr}")
            break
        
        ip= scapy.IP(data)
        ip[scapy.IP].src = random_ip
        ip[scapy.IP].dst= proxy_ip
        
        pack = ip
        scapy.send(pack)


# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
sock.bind((proxy_ip, 62254))

# Listen for incoming connections
sock.listen(1)
# while True:
    # Wait for a client to connect
conn, addr = sock.accept()
recive_proxy_data_ = threading.Thread(target=send_data_loop_back, args=(conn,))
recive_proxy_data_.start()
print(f"Connected by {addr}")










def filter_game_packets(port, src):
    if( ((port >= 2300 and port <= 2400) or port==47624) and src==proxy_ip):
        return True
    else:
        return False




# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

s.bind((proxy_ip,0))



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
    
    
    src_port = struct.unpack('!H', packet[20:22])[0]
    dst_port = struct.unpack('!H', packet[22:24])[0]
    src_address = socket.inet_ntoa(packet[12:16])
    dst_address = socket.inet_ntoa(packet[16:20])
    
    if(header[6]==6): #header[6] is the field of the Protocol
    

        if(filter_game_packets(dst_port, src_address)):
            print("Protocol = TCP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
            # conn.sendall(packet)
            
            
            
            
    if(header[6]==17):
        
        # print(binascii.hexlify(bytes(packet)).decode('utf-8'))
        src_port = struct.unpack('!H', packet[20:22])[0]
        dst_port = struct.unpack('!H', packet[22:24])[0]
        
        # user_id = get_packet_data(packet, 'ip_id')
        
        src_address = socket.inet_ntoa(packet[12:16])
        dst_address = socket.inet_ntoa(packet[16:20])

        
        if(filter_game_packets(dst_port, src_address)):
            print("Protocol = UDP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
            # conn.sendall(packet)
            
        
    n=n+1



    
    
    
conn.close()

    
    

