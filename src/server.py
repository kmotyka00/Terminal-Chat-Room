import threading
import socket

HEADER = 64 # first message to the server will have 64 bytes and tell the length of the message 
PORT = 5054
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(ADDR)

    def start(self):
        self.socket.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")
        while True:
            conn, addr = self.socket.accept() # waits for a new connection to the server
            thread = threading.Thread(target=self.handle_client, args = (conn, addr)) # when new client occurs create new thread to handle it, pass function and arguments
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # print info about clients active

    def handle_client(self, connection, address):
        print(f"[NEW CONNECTION] {address} connected")

        connected = True
        while connected:
            msg_length = connection.recv(HEADER).decode(FORMAT) # blocking until we receive the message from a client, thanks to threads we are not blocking other clients
            if msg_length:
                msg_length = int(msg_length)
                msg = connection.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{address}] {msg}")

        connection.close()


print("[STARTING] server is starting...")
server = Server()
server.start()
