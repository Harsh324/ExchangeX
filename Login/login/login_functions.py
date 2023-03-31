import os
import sqlite3 as Sq

class Login():

    def __init__(self) -> None:
        if not os.path.exists('database'):
            os.makedirs('database')

        self.logObj = Sq.connect('log.db')
        self.logObj.cursor().execute('''
            CREATE TABLE IF NOT EXISTS logs
            (userId TEXT PRIMARY KEY, password TEXT)
        ''')
        self.logObj.commit()
    

    def validateUser(self, userId, passWord):
        
        """
        ### Function Description : 

            This Function takes the userId and password as input and\n
            validates whether the user with the given credentials exists or not.\n
            Returns the json object.\n
            
        ### Function Parameters : 
            
            # userId : 
                This Parameter is the unique Id of a user.\n
            
            # password : 
                This Parameter is the password of the user.\n
        """
        
        user = self.logObj.cursor().execute('SELECT * FROM logs WHERE userId = ? AND password = ?',
                                 (userId, passWord)).fetchone()
        self.logObj.close()
        if user is not None:
            return {'status' : True, 'info' : {'userId' : userId}}
        else:
            return {'status' : False, 'info' : 'unable to login check the credentials again'} 



class Register():

    def __init__(self) -> None:
        if not os.path.exists('database'):
            os.makedirs('database')

        self.logObj = Sq.connect('log.db')
        self.logObj.cursor().execute('''
            CREATE TABLE IF NOT EXISTS logs
            (userId TEXT PRIMARY KEY, password TEXT)
        ''')
        self.logObj.commit()

        self.userObj = Sq.connect('user.db')
        self.userObj.cursor().execute('''
            CREATE TABLE IF NOT EXISTS users
            (userId TEXT PRIMARY KEY, kyc BOOL, balance FLOAT)
        ''')
        self.userObj.commit()

    def register(self, userId, password):

        """
        ### Function Description : 

            This Function takes the userId and password as input and\n
            registers whether the user with the given credentials in the database.\n
            Returns the json object of status.\n
            
        ### Function Parameters : 
            
            # userId : 
                This Parameter is the unique Id of a user.\n
            
            # password : 
                This Parameter is the password of the user.\n
        """

        try:
            self.logObj.cursor().execute('INSERT INTO logs VALUES (?, ?)', (userId, password))
            self.logObj.commit()
            self.logObj.close()

            self.userObj.cursor().execute('INSERT INTO users VALUES (?, ?, ?', (userId, 0.0, False))
            self.userObj.commit()
            self.userObj.close()
            return {'status' : True, 'info' : 'Registration successfull'}
        except Sq.IntegrityError:
            self.logObj.commit()
            self.logObj.close()
            self.userObj.close()
            return {'status' : False, 'info' : 'userId already exists'}

        
        