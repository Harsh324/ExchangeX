import os
import sqlite3 as Sq

class Kyc():

    def __init__(self, name, email, address, dob, docName, docNumber) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.dob = dob
        self.docName = docName
        self.docNumber = docNumber

        if not os.path.exists('database'):
            os.makedirs('database')

        self.kycObj = Sq.connect('kyc.db')


    def addToDatabase(self):

        """
        ### Function Description : 

            This Function is get all the kyc details updated in database\n
        
        """

        self.kycObj.cursor().execute('''
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

        self.kycObj.cursor().execute('INSERT INTO kyc (name, email, address, dob, doc_name, doc_number) VALUES (?, ?, ?, ?, ?, ?)', (self.name, self.email, self.address, self.dob, self.doc_name, self.doc_number))
        self.kycObj.commit()


    def updateKyc(self):
        pass


    