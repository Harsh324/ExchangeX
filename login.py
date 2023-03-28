import os
import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.create_table()

    if not os.path.exists('databases'):
            os.makedirs('databases')

    def create_table(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                    (username TEXT PRIMARY KEY, password TEXT)''')
        conn.commit()
        conn.close()

    def register(self, username, password):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        try:
            c.execute('INSERT INTO users VALUES (?, ?)', (username, password))
            conn.commit()
            print("Registration successful!")
        except sqlite3.IntegrityError:
            print("Username already exists.")
        conn.close()

    def login(self, username, password):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            print("Login successful!")
        else:
            print("Invalid username or password.")

