import socket


def connect(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    return s

s = connect('127.0.0.1', 8080)

while True:
    data = s.recv(1024)
    print(data.decode())
    s.send(input().encode())
    if data.decode() == 'Bye':
        break