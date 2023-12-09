# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:27:30 2023

@author: Amir
"""

import socket
import struct
from scapy.layers.l2 import Ether
import scapy.all as scapy
import struct

# def get_mac(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
#     if len(answered_list) == 0:
#         return None
#     else:
#         return answered_list[0][1].hwsrc

# ip = '192.168.52.207' # Example IP address
# mac = get_mac(ip) # Get MAC address of device with the specified IP address

# if mac is not None:
#     packet = scapy.IP()/scapy.TCP() # Create packet with IP and TCP layers
#     packet[scapy.IP].dst = ip # Set destination IP address
#     packet[scapy.IP].src = "192.168.1.2" # Set source IP address
#     scapy.sendp(packet, dst=mac) # Send packet over Ethernet to the device's MAC address
# else:
#     print("Could not find MAC address for", ip)
    
    
#######
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
proxy_ip =s.getsockname()[0]
s.close()
del s
#######


game_host_ip = '192.168.52.207'
client_ip='192.168.52.78'
client_list = {};

def filter_game_packets(port):
    if( (port >= 2300 and port <= 2400) or port==47624):
        return True
    else:
        return False
    
HOST = socket.gethostbyname(socket.gethostname())


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
    
    if(header[6]==6): #header[6] is the field of the Protocol
    

        src_port = struct.unpack('!H', packet[20:22])[0]
        dst_port = struct.unpack('!H', packet[22:24])[0]
        src_address = socket.inet_ntoa(packet[12:16])
        dst_address = socket.inet_ntoa(packet[16:20])
        if(filter_game_packets(dst_port)):
            if(src_address != proxy_ip):
                
                
                
                ip = scapy.IP(packet)
                # ip.show()


                # if(ip[scapy.IP].src == proxy_ip or ip[scapy.IP].dst == proxy_ip ):
                    
                #     if(ip[scapy.IP].src != game_host_ip):
                #         ip[scapy.IP].src = proxy_ip
                #         ip[scapy.IP].dst= game_host_ip
                #     else:
                #         ip[scapy.IP].dst= client_ip
                #         ip[scapy.IP].src = proxy_ip
                        
                #     del ip[scapy.IP].chksum
                #     del ip[scapy.TCP].chksum
                    
                    
                #     print(get_mac(ip[scapy.IP].dst))
                #     eth = scapy.Ether(dst=get_mac(ip[scapy.IP].dst), src=get_mac(ip[scapy.IP].src))
                #     pack = eth /ip
                #     print(ip[scapy.IP].dst)
                #     scapy.send(pack)



                # try:
                    # reverse_send_tcp(packet)
                # except:
                    # pass
                print("Protocol = TCP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
            
            
            
            
    if(header[6]==17):
        
        continue
        # print(binascii.hexlify(bytes(packet)).decode('utf-8'))
        src_port = struct.unpack('!H', packet[20:22])[0]
        dst_port = struct.unpack('!H', packet[22:24])[0]
        
        # user_id = get_packet_data(packet, 'ip_id')
        
        src_address = socket.inet_ntoa(packet[12:16])
        dst_address = socket.inet_ntoa(packet[16:20])
        
        # print(user_id)
        
        # if(dst_address== proxy_ip):
        #     addressed = src_address
        # else:
        #     addressed = dst_address
        
        
        # if(user_id not in client_list):

        #         client_list[user_id] =dst_address
        #     else:
        #         client_list[user_id] =src_address
            
        
        
        if(filter_game_packets(dst_port)):
            
            # if(src_address != proxy_ip):
                # reverse_send_udp(packet)
            print("Protocol = UDP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
            
            
            
    elif(header[5]==1):
        print("Protocol = ICMP") 
    n=n+1