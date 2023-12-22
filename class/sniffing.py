import socket
import struct
import time
import random
from enum import Enum




class Packet:
    def __init__(self, packet):
        self.packet = packet
        header_length = (packet[0] & 0x0F) * 4
        self.header_raw = packet[:header_length]
        self.header = struct.unpack('!BBHHHBBH4s4s', self.header_raw)
        self.version = self.header[0] >> 4
        self.header_length = header_length
        self.differentiated_services = self.header[1]
        self.total_length = self.header[2]
        self.identification = self.header[3]
        self.flags_and_fragment_offset = self.header[4]
        self.time_to_live = self.header[5]
        self.protocol = self.header[6]
        self.header_checksum = self.header[7]
        self.source_address = socket.inet_ntoa(self.header[8])
        self.destination_address = socket.inet_ntoa(self.header[9])
        # payload data starts after the header
        self.payload = packet[self.header_length:]
        self.payload_length = len(self.payload)

        if(self.protocol == socket.IPPROTO_TCP):

            self.transport_header_length = (self.payload[12] >> 4) * 4
            self.raw_transport_header = packet[self.header_length:self.header_length+self.transport_header_length]
            self.transport_header = struct.unpack('!HHIIBBHHH', self.raw_transport_header[:20])
            self.tcp_source_port = self.transport_header[0]
            self.tcp_destination_port = self.transport_header[1]
            self.tcp_sequence_number = self.transport_header[2]
            self.tcp_acknowledgment_number = self.transport_header[3]
            self.flags = self.transport_header[5]
            self.tcp_window_size = self.transport_header[6]
            self.transport_checksum = self.transport_header[7]
            self.tcp_urgent_pointer = self.transport_header[8]
            self.tcp_length =  self.payload_length - self.transport_header_length
            self.transport_data = self.payload[self.transport_header_length:]


        elif(self.protocol == socket.IPPROTO_UDP):
            
            self.transport_header_length = 8
            self.raw_transport_header = packet[self.header_length:self.header_length+self.transport_header_length]
            self.transport_header = struct.unpack('!HHHH', self.raw_transport_header)
            self.udp_source_port = self.transport_header[0]
            self.udp_destination_port = self.transport_header[1]
            self.udp_length = self.transport_header[2] # The length of the entire UDP datagram, including both header and data, in bytes.
            self.transport_checksum = self.transport_header[3]
            self.transport_data = self.payload[self.transport_header_length:]
            
        self.source_port = int.from_bytes(packet[self.header_length: self.header_length+2] , 'big')
        self.destination_port = int.from_bytes(packet[self.header_length+2: self.header_length+4], 'big')

        # print("payload :: ")
        # print(list(self.payload))

    def calculate_checksum(self):
        unpacked_header_with_zeroed_checksum = self.header[:7] + (0,) + self.header[8:]
        header_with_zeroed_checksum = struct.pack('!BBHHHBBH4s4s', *unpacked_header_with_zeroed_checksum)

        total = 0
        # Split the header into 16-bit words
        for i in range(0, len(header_with_zeroed_checksum), 2):
            word = (header_with_zeroed_checksum[i] << 8) + header_with_zeroed_checksum[i+1]
            total += word
            total = (total & 0xffff) + (total >> 16)

        # Finalize: Invert the bits
        checksum = ~total & 0xffff
        self.header_checksum =  checksum



    def calculate_transport_checksum(self):
        # Pseudo Header fields
        source_address = socket.inet_aton(self.source_address)
        destination_address = socket.inet_aton(self.destination_address)
        reserved = 0
        protocol = self.protocol
        tcp_length = self.payload_length
        
        # Pseudo Header
        psh = struct.pack('!4s4sBBH', source_address, destination_address, reserved, protocol, tcp_length)

        if(self.protocol == socket.IPPROTO_TCP):
            # TCP Header
            tcp_header = self.raw_transport_header[:16]  # without checksum
            zero_checksum = 0
            tcp_header_without_checksum = tcp_header + struct.pack('H', zero_checksum) + self.raw_transport_header[18:]
            
            checksum_feed = psh + tcp_header_without_checksum + self.transport_data

            if(len(checksum_feed) % 2 != 0): checksum_feed += b'\x00'

        elif(self.protocol == socket.IPPROTO_UDP):
            # UDP Header
            udp_header = self.raw_transport_header[:6]  # without checksum
            zero_checksum = 0
            udp_header_without_checksum = udp_header + struct.pack('H', zero_checksum)
            
            checksum_feed = psh + udp_header_without_checksum + self.transport_data
            if(len(checksum_feed) % 2 != 0): checksum_feed += b'\x00'
    

        total = 0
        # Split the header into 16-bit words
        for i in range(0, len(checksum_feed), 2):
            word = (checksum_feed[i] << 8) + checksum_feed[i+1]
            total += word
            total = (total & 0xffff) + (total >> 16)

        # Finalize: Invert the bits
        checksum = ~total & 0xffff
        
        self.transport_checksum =  checksum



    def change_source_address(self, new_address):
        self.source_address = new_address
        temp = bytearray(self.header_raw)
        temp[12:16] =  socket.inet_aton(new_address)
        self.header_raw = bytes(temp)
        self.header = struct.unpack('!BBHHHBBH4s4s', self.header_raw)
        self.calculate_checksum()
    

    def change_destination_address(self, new_address):
        self.source_address = new_address
        temp = bytearray(self.header_raw)
        temp[16:20] =  socket.inet_aton(new_address)
        self.header_raw = bytes(temp)
        self.header = struct.unpack('!BBHHHBBH4s4s', self.header_raw)
        self.calculate_checksum()

    def output_packet(self):
        return self.header_raw + self.payload


class Sniffing:
    def __init__(self, localIP):

        self.localIP = localIP
        self.socket = None
        self.creat_socket()


    def creat_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        s.bind((self.localIP,0))

        # Include IP headers
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        # receive all packages
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        self.socket = s

    def sniffing(self):
        while True:
            data = self.socket.recvfrom(65565)
            packet = Packet(data[0])

            if(self.filter_game_packets(packet)):
                yield packet

    def filter_game_packets(self, packet:Packet):

        if(packet.protocol == socket.IPPROTO_UDP or packet.protocol == socket.IPPROTO_TCP):
            if( 
                2400 < packet.destination_port <= 2400 or
                2400 < packet.source_port <= 2400 or
                packet.source_port == 47624 or 
                packet.destination_port  == 47624 or 
                packet.source_port == 443
            ):
                
                return True 
        return False


class Player:
    def __init__(self):
        pass



def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local =s.getsockname()[0]
    s.close()
    del s
    return local


def getRandomLocalIP(lacal_ip):
    ip_ng = lacal_ip.split('.')[:3] + [str(random.randint(100, 255))]
    return ".".join(ip_ng)


LocalIP = getLocalIP()
sniffing = Sniffing(LocalIP)

for i in sniffing.sniffing():

    pass
    # if(i.protocol == socket.IPPROTO_TCP):
        # print(i.raw_transport_header)
        # break
    # print(i.destination_address)
    # print(i.header_checksum)
    # print(i.total_length)
    # print(i.payload)
    # print(i.source_port)
    # print(i.destination_port)
    # print(i.output_packet())
    # break


