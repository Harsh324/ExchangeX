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

        """
        ### Function Description : 

            This Function is used to check if the account\n
            with the given userId exists or not\n
            Returns the json object with the all details of the row matched\n
            
        ### Function Parameters : 
            
            # userId : 
                This Parameter is the userId of the sender or reciever.\n

        """

        user = self.connUser.cursor().execute("SELECT * FROM users WHERE userId=?", (userId,)).fetchone()
        self.connUser.close()

        if user is None:
            return {'status' : False, 'info' : "user does not exist"}
        else :
            return {'status' : True, 'info' : {user}}


    def updateBalance(self, userId, amount):

        """
        ### Function Description : 

            This Function is takes the userId and amount and\n
            updates the balance of the sender and reciever\n

            
        ### Function Parameters : 
            
            # userId : 
                This Parameter is the userId of the sender or reciever.\n
            
            # amount : 
                The updated balance that need to update in database
                
        """

        self.connUser.cursor().execute("UPDATE users SET balance=? WHERE userId=?", (amount, userId))
        self.connUser.commit()
        self.connUser.close()

