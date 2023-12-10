import socket
import struct
import time

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



#######
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local =s.getsockname()[0]
s.close()
del s
#######

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

s.bind((local,0))



# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


while True:
    print('waiting')
    time.sleep(0.0001)

    # receive a package
    data = s.recvfrom(65565)
    print('recive')
    address = data[1]
    packet = Packet(data[0])
    break

