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
        self.payload = packet[self.header_length:self.total_length]

        self.source_port = int.from_bytes(packet[self.header_length: self.header_length+2] , 'big')
        self.destination_port = int.from_bytes(packet[self.header_length+2: self.header_length+4], 'big')


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
    print(i.source_address)
    print(i.destination_address)
    print(i.header_checksum)
    print(i.total_length)
    print(i.payload)
    print(i.source_port)
    print(i.destination_port)
    print(i.output_packet())
    # break


