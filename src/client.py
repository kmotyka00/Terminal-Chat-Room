import socket
from settings import HEADER, ADDR, FORMAT

class Message:
    def __init__(self, msg):
        self.content = msg.encode(FORMAT)
        self.length = len(self.content)
        self.length = str(self.length).encode(FORMAT)
        self.length += b' ' * (HEADER - len(self.length))

    def get_content(self):
        return self.content

    def get_length(self):
        return self.length

class Client:
    def __init__(self, username=""):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(ADDR)
        self.username = username
        
    def send_message(self, msg):
        message = Message(f"{[self.username]} {msg}")

        self.socket.send(message.get_length())
        self.socket.send(message.get_content())

    def loop(self):
        while True:
            message = input("Write message: ")
            self.send_message(message)
