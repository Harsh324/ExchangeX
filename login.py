import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.create_table()

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

if __name__ == '__main__':
    user_manager = UserManager('users.db')
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")
    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        user_manager.register(username, password)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_manager.login(username, password)
    else:
        print("Invalid choice. Please try again.")
