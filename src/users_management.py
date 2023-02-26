from typing import Optional
from client import Client
import sqlite3
from getpass import getpass
from werkzeug.security import check_password_hash, generate_password_hash

USERS_DATABASE_FILE = '../data/users.db'

class UsersManager:
    def __init__(self):
        self.connection = sqlite3.connect(USERS_DATABASE_FILE)
    
    def create_users_table(self):
        with self.connection:
            c = self.connection.cursor()
            users_table_exists = c.execute(''' SELECT name FROM sqlite_master WHERE type='table' AND name='users'; ''').fetchone()

            if not users_table_exists:
                self.connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
            
            self.connection.commit()
    
    def get_user_credentials(self, username: Optional[str] = None, password: Optional[str] = None):
        if not username:
            username = input("Provide username: ")
        
        if not password:
            password = getpass("Provide password: ")

        return username, password

    def start_client_session(self, username: str):
        client = Client(username)
        print("Client session started.")
        client.loop()

    def login(self, username: Optional[str] = None, password: Optional[str] = None):

        username, password = self.get_user_credentials(username, password)

        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = (?)", (username,))
            user_exists = cursor.fetchone()

            if not user_exists:
                raise ValueError("Wrong Username")

            if not check_password_hash(user_exists[2], password):
                raise ValueError("Wrong Password")

            print("Logged in successfully!")

            self.start_client_session(username)

    def register(self, username: Optional[str] = None, password: Optional[str] = None):
        
        username, password = self.get_user_credentials(username, password)

        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = (?)", (username,))
            user_exists = cursor.fetchone()

            if not user_exists:
                cursor.execute(''' INSERT INTO users (username, password) VALUES (?, ?)''', (username, generate_password_hash(password)))
                print(f"User '{username}' added to the 'users' table.")
            else:
                raise ValueError(f"User '{username}' already exists in the 'users' table.")
            
            self.connection.commit()

        self.start_client_session(username)



        
        

