import socket

token_range = 12

def connect(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    return s

s = connect('127.0.0.1', 8080)

id = '?'
s.send((id.encode()))
data = s.recv(12)
id = data.decode()

while True:
    
    s.send((id+input()).encode())
    if data.decode() == 'Bye':
        break