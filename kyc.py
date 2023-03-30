import os
import sqlite3

class KYCForm:
    def __init__(self):
        self.name = None
        self.email = None
        self.address = None
        self.dob = None
        self.doc_name = None
        self.doc_number = None

    def get_info(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email address: ")
        self.address = input("Enter your physical address: ")
        self.dob = input("Enter your date of birth (DD-MM-YYYY): ")
        self.doc_name = input("Enter your document name: ")
        self.doc_number = input("Enter document number: ")

    def save_to_database(self):
        if not os.path.exists('databases'):
            os.makedirs('databases')

        conn = sqlite3.connect('databases/kyc.db')

        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS kyc (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                address TEXT,
                dob TEXT,
                doc_name TEXT,
                doc_number TEXT
            )
        ''')

        cursor.execute('INSERT INTO kyc (name, email, address, dob, doc_name, doc_number) VALUES (?, ?, ?, ?, ?, ?)', (self.name, self.email, self.address, self.dob, self.doc_name, self.doc_number))
        conn.commit()

        print("Thank you for submitting your KYC information. We will let you know after completing verification!")

def kyc_form():
    kyc = KYCForm()
    kyc.get_info()
    kyc.save_to_database()

if __name__ == '__main__':
    kyc_form()
