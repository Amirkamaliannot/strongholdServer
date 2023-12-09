import socket
import threading
import time

class Client:
    
    def __init__(self, socket, status):
        self.socket = socket;
        self.status = status;



class tcp_server:

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
            time.sleep(0.001)
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

    def close(self):
        self.loopping = False;
        self.s.close();

        
    def __del__(self):
        self.close();


sokce = tcp_server('127.0.0.1', 8080);

print("sdads");