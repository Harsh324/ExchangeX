import os
import sqlite3 as Sq

class User():

    def __init__(self) -> None:
        
        if not os.path.exists('database'):
            os.makedirs('database')

        self.connUser = Sq.connect('user.db')
        self.connUser.cursor().execute('''
            CREATE TABLE IF NOT EXISTS users
            (userId TEXT PRIMARY KEY, kyc BOOL, balance FLOAT)
        ''')
        self.connUser.commit()

    
    def validateUser(self, userId):

        """Documentation"""

        user = self.connUser.cursor().execute("SELECT * FROM users WHERE userId=?", (userId,)).fetchone()
        self.connUser.close()

        if user is None:
            return {'status' : False, 'info' : "user does not exist"}
        else :
            return {'status' : True, 'info' : {user}}


    def updateBalance(self, userId, amount):

        """Documentation"""

        self.connUser.cursor().execute("UPDATE users SET balance=? WHERE userId=?", (amount, userId))
        self.connUser.commit()
        self.connUser.close()

