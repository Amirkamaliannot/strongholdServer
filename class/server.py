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
        token = "$";
        for i in range(token_range-1):
            token += chr(random.randint(48,79));
        self.id = token;

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
            time.sleep(0.0001)
            print("counter =======> ",self.count)

            if(self.count == 10):
                self.close();
                self.loopping = False
                print("Server closed");
            try:

                client, addr = self.s.accept();
                token = self.get_user_token(client)
                if(token is False):
                    continue

                print("token =======> ",token)
                client_obj = self.add_client(client, token)
                
                print("client_obj =======> ",client_obj)
                print("client_id =======> ",client_obj.id)
                self.count += 1
                client.send(client_obj.id.encode());
            
            except  Exception as e:
                print(e)
                pass

    def get_user_token(self, client):

        token = client.recv(token_range).decode()

        if(token == "?"):
            return token
        elif(token and token[0] == "$" and len(token) == token_range):
            return token
        else:
            return False


    def add_client(self, client, token):

        is_exist = self.is_client_exist(token)
        if(is_exist is not False):
            self.clients[is_exist].socket.close();
            self.clients[is_exist].socket = client;
            self.clients[is_exist].status = True;
            temp =self.clients[is_exist]
        else:
            temp = Client(client, True)
            self.clients.append(temp)
        
        return temp

        


    def is_client_exist(self, token):
        for c in range(len(self.clients)):
            if(self.clients[c].id == token):
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

                        if(len(data.decode()) < token_range):
                            self.clients.remove(c);
                            continue
                        
                        client_id = data.decode()[:token_range];
                        if(client_id != c.id):
                            self.clients.remove(c);
                            continue

                        
                        print("\n"+"clientID: "+client_id + "   Data:"+data.decode()[token_range:]+"\n")
                    else:
                        # c.socket.close();
                        c.status = False;
                except:
                    pass


    def send_data(self, id, data):
        for c in self.clients:
            if(c.id == id):
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
