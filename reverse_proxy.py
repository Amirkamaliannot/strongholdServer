# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:03:33 2023

@author: Amir
"""



import socket
import struct


game_host_ip ='46.209.20.154'
proxy_ip='192.168.175.178'
client_ip='46.209.20.154'
client_list = {};

def filter_game_packets(port):
    if( (port >= 2300 and port <= 2400) or port==47624 or True):
        return True
    else:
        return False


def get_packet_data(packet, key):
    
    output = {}
    output['version_ihl'], output['tos'], output['tot_len'], output['ip_id'], output['frag_off'], output['ttl'], output['proto'], output['ip_check'], output['saddr'], output['daddr ']= struct.unpack('!BBHHHBBH4s4s', packet[:20])
    return output[key]



def reverse_send_udp(packet):
    
    # Extract the IP header fields
    version_ihl, tos, tot_len, id, frag_off, ttl, proto, check, saddr, daddr = struct.unpack('!BBHHHBBH4s4s', packet[:20])
    
    ip_ver = 4
    ip_ihl = 5
    ip_tos = 0
    ip_tot_len = 0  # This will be set later
    ip_id = id
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = 17#socket.IPPROTO_UDP
    ip_check = 0  # This will be set later
    
    src_address = socket.inet_ntoa(packet[12:16])
    # dst_address = socket.inet_ntoa(packet[16:20])
    # dst_port = struct.unpack('!H', packet[22:24])[0]
    
    ip_saddr = socket.inet_aton(proxy_ip)
    if(src_address==game_host_ip):
        ip_daddr = socket.inet_aton(client_ip)
        ip_daddr2=  client_ip#client_list[ip_id]
    else:
        ip_daddr = socket.inet_aton(game_host_ip)
        ip_daddr2=game_host_ip
    
    
    # Set the IP header fields for the new packet
    ip_tot_len = tot_len
    ip_check = check
    new_ip_header = struct.pack('!BBHHHBBH4s4s', (ip_ver << 4) + ip_ihl, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)
    
    
    # Extract the UDP header fields
    udp_header = packet[20:28]
    src_port, dst_port, udp_len, udp_check = struct.unpack('!HHHH', udp_header)
    
    # Create the new packet by combining the IP and UDP headers with the payload
    new_packet = new_ip_header + udp_header + packet[28:]
    

    # Send the new packet to the destination IP address
    # print(ip_daddr2)
    s.sendto(new_packet, (ip_daddr2, 0))

def calculate_checksum(data):
    # Pad the data if its length is odd
    if len(data) % 2 == 1:
        data += b'\x00'
    
    # Calculate the sum of 16-bit words
    total = sum(struct.unpack('!{}H'.format(len(data) // 2), data))
    
    # Fold the carry bits and complement the result
    checksum = (total & 0xffff) + (total >> 16)
    checksum = (~checksum) & 0xffff
    
    return checksum

def repack_tcp(pack, new_srs_ip, new_dst_ip):

    IHL = int.from_bytes(pack[:1] , 'big') & 0x0F
    ip_heder_size = IHL*4
    ip_header = pack[: ip_heder_size]

    data_offset = pack[ip_heder_size + 12] >> 4
    tcp_header_size = data_offset * 4
    tcp_header = pack[ip_heder_size: ip_heder_size+tcp_header_size]
    
    payload = pack[ip_heder_size+tcp_header_size : ]


    checksum = int.from_bytes(tcp_header[16:18], 'big')
    
    print(checksum)

    #replacing new ip
    ip_header = ip_header[:12] + socket.inet_aton(new_srs_ip) + socket.inet_aton(new_dst_ip) + ip_header[20:]
    
    # Remove the existing checksum from the TCP header
    tcp_header = tcp_header[:16] + b'\x00\x00' + tcp_header[18:]

    # Create the pseudo header
    source_addr = ip_header[12:16]
    dest_addr = ip_header[16:20]
    protocol = ip_header[9:10]
    tcp_segment_size = len(pack[ip_heder_size:])
    pseudo_header = source_addr + dest_addr + b'\x00' + protocol + struct.pack('!H', tcp_segment_size)

    # Calculate the checksum for the pseudo header and the TCP header
    checksum_data = pseudo_header + tcp_header + payload
    
    if len(checksum_data) % 2 == 1:
        checksum_data += b'\x00'
    calculated_checksum = calculate_checksum(checksum_data)
    
    print(calculated_checksum)
    
    new_packet = ip_header + tcp_header[:16] + calculated_checksum.to_bytes(2, 'big')+ tcp_header[18:] + payload
    
    return new_packet

def reverse_send_tcp(packet):
    
    src_port = struct.unpack('!H', packet[20:22])[0]
    # ip_saddr = socket.inet_aton(proxy_ip)
    # if(src_address==game_host_ip):
    #     ip_daddr2=  client_ip
    # else:
    #     ip_daddr2=game_host_ip
        
    src_ip = "192.168.175.137"
    dst_ip = "192.168.175.178"
    # src_ip = socket.inet_ntoa(packet[12:16])
    # dst_ip= socket.inet_ntoa(packet[16:20])
    new_packet = repack_tcp(packet, dst_ip, src_ip)
    
    s.sendto(new_packet, (src_ip, src_port))
    print('send')
        
        
# the public network interface
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
                # try:
                    reverse_send_tcp(packet)
                # except:
                    # pass
                    print("Protocol = TCP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
            
            
            
            
    if(header[6]==17):
        
        continue
        # print(binascii.hexlify(bytes(packet)).decode('utf-8'))
        src_port = struct.unpack('!H', packet[20:22])[0]
        dst_port = struct.unpack('!H', packet[22:24])[0]
        
        user_id = get_packet_data(packet, 'ip_id')
        
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
            
            if(src_address != proxy_ip):
                reverse_send_udp(packet)
            print("Protocol = UDP / src:"+src_address+" : "+str(src_port)+'  dst:'+dst_address+' : '+str(dst_port))
            
            
            
    elif(header[5]==1):
        print("Protocol = ICMP") 
    n=n+1





























