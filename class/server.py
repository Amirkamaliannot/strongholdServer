import socket
import threading
import time
import random

token_range = 12

class Client:
    
    def __init__(self, socket, status):
        self.socket = socket;
        self.status = status;
        self.id = None;
        self.creat_random_token();
    
    def creat_random_token(self):
        token = "";
        for i in range(16):
            token += chr(random.randint(48,79));
        self.id = token;

a = Client(None, False)

print(a.creat_random_token())
class TCPserver:

    def __init__(self, ip, port):
        self.clients = [];

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.s.bind((ip, port));
        self.s.listen(8);


        self.count = 0
        self.loopping = True
        threading.Thread(target=self.accepting_loop).start();
        threading.Thread(target=self.listening_loop).start();


    def accepting_loop(self):

        while self.loopping:
            print("counter =======> ",self.count)

            if(self.count == 10):
                self.close();
                self.loopping = False
                print("Server closed");
            try:
                client, addr = self.s.accept();
                self.add_client(client)
                
                self.count += 1
                client.send(b'Hello, ' + addr[0].encode());
            except  Exception as e:
                print(e)
                pass


    def add_client(self, client):
        is_ip_exist = self.is_ip_exist(client.getpeername()[0])
        if(is_ip_exist is not False):
            self.clients[is_ip_exist].socket.close();
            self.clients[is_ip_exist].socket = client;
            self.clients[is_ip_exist].status = True;
        else:
            self.clients.append(Client(client, True))


    def is_ip_exist(self, ip):
        for c in range(len(self.clients)):
            if(self.clients[c].socket.getpeername()[0] == ip):
                return c
        return False;


    def listening_loop(self):
        while self.loopping:
            time.sleep(0.0001)
            for c in self.clients:
                if(c.status == False):
                    continue
                try:
                    data = c.socket.recv(1024);
                    if(data):
    
                        print("\ndata recived\n")
                    else:
                        # c.socket.close();
                        c.status = False;
                except:
                    pass


    def send_data(self, ip, data):
        for c in self.clients:
            if(c.socket.getpeername()[0] == ip):
                c.socket.send(data)
                return True
        return False
    

    def send_data_all(self, data):
        for c in self.clients:
            c.socket.send(data)
        return True;


    def close(self):
        self.loopping = False;
        # self.s.close();

        
    def __del__(self):
        self.close();


sokce = TCPserver('127.0.0.1', 8080);

print("sdads");

while True:
    text = input("\nenter message : \n");
    sokce.send_data_all(text.encode());
