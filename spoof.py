# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:06:09 2023

@author: test
"""
from scapy.layers.l2 import Ether
import scapy.all as scapy
import struct
import socket
import random

import os

def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    
    return pingstatus


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip =s.getsockname()[0]
s.close()


ip_ng = ip.split('.')[:3] + [str(random.randint(1, 255))]
random_ip = ".".join(ip_ng)

# print(check_ping('192.168.175.178'))
print(check_ping(random_ip))


# spoofed_ip = "112.100.112.45"
# # spoofed_ip2 = "192.168.175.12"

# string ="""
# 0000   70 cf 49 eb e0 01 00 0c 42 85 4e 2e 08 00 45 00
# 0010   00 34 f7 d7 40 00 6a 06 71 16 0d 6b 2a 10 c0 a8
# 0020   af b2 01 bb c7 b1 27 16 3e 22 77 44 25 8c 80 10
# 0030   40 02 8c cf 00 00 01 01 05 0a 77 44 25 8b 77 44
# 0040   25 8c
# """

# string = string.replace('\n', ' ')
# hex_list = string.split(" ")
# hex_list = [int(i, 16) for i in hex_list if len(i)==2]

# bytes_ = struct.pack('>' + 'B' * len(hex_list), *hex_list)


# # bs = bytes.fromhex(bytes_)

# eth_header = Ether(src="00:11:22:33:44:55", dst="66:77:88:99:aa:bb")
# ip = scapy.IP(bytes_[14:])
# ip.show()
# pack = ip/ b"hellow world"

# pack[scapy.IP].src = "112.100.112.45"
# pack[scapy.IP].dst="192.168.175.178"
# del pack[scapy.IP].chksum
# del pack[scapy.TCP].chksum

# pack.show()
# scapy.send(pack)










# data_offset = pack[ip_heder_size + 12] >> 4
# tcp_header_size = data_offset * 4
# tcp_header = pack[ip_heder_size: ip_heder_size+tcp_header_size]

# payload = pack[ip_heder_size+tcp_header_size : ]


# # Spoofed IP address


# # Create IP packet 
# ip = scapy.IP(src=spoofed_ip, dst="192.168.175.178")

# # # Create TCP packet
# tcp = scapy.TCP(sport=4444, dport=22292, flags="S") 
# udp = scapy.UDP(dport=4444, sport=555)

# # # Add TCP packet to IP packet
# packet1 = ip/tcp/b'sdasdajkdsadsajdnbvxvcbvbbvvbbvxbvvc,s'
# packet2 = ip/udp/b'sdasdajkdsadsajvbvccxvvbbcbv12bvvbdn,s'

# # packet1[scapy.IP].src = spoofed_ip2



# # # Send the packet 
# scapy.send(packet1)
# scapy.send(packet2)

# ether.show()

# scapy.send(ether)