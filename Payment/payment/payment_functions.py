import sqlite3 as Sq
import os
import User.user.user_functions as user

class Payment():

    def __init__(self, senderUserId, receiverUserId, amount, date) -> None:
        self.sender = senderUserId
        self.reciever = receiverUserId
        self.amount = amount
        self.date = date

        if not os.path.exists('database'):
            os.makedirs('database')
        self.connPay = Sq.connect('payment.db')
        self.userObj = user.User()
    

    def connect(self):

        """Documentation"""
        self.sender = self.userObj.validateUser(self.sender)
        self.reciever = self.userObj.validateUser(self.sender)
        return {'sender' : self.sender, 'receiver' : self.reciever}
        

    def transaction(self):

        """Documentation"""
        connObj = self.connect()
        
        if(connObj['sender']['status'] == True and connObj['receiver']['status'] == True):
            if(connObj['sender']['info']['balance'] >= self.amount):
                self.userObj.updateBalance(self.sender, connObj['sender']['info']['balance'] - self.amount)
                self.userObj.updateBalance(self.reciever, connObj['reciever']['info']['balance'] + self.amount)

                self.connPay.cursor().execute("INSERT INTO payments VALUES (?, ?, ?, ?)", (connObj['sender']['id'], connObj['receiver']['id'], self.amount, self.date))
                self.disconnect()
                return {'status' : True, 'info' : "Payment done successfully"}
            else:
                return {'status' : False, 'info' : "Not sufficient balance to perform transaction"}

        else:
            return {'status' : False, 'info' : "Unable to validate sender or reciever"}


    def disconnect(self):

        """Documentation"""
        self.connPay.commit()
        self.connPay.close()
    