import sqlite3 as Sq
import os

class Payment():

    def __init__(self, senderAccountNo, receiverAccountNo, amount, date) -> None:
        self.sender = senderAccountNo
        self.reciever = receiverAccountNo
        self.amount = amount
        self.date = date
        if not os.path.exists('database'):
            os.makedirs('database')
        self.connPay = Sq.connect('payment.db')
        #self.userObj = User()
    

    def connect(self):

        """Documentation"""
        self.sender = self.userObj.validate(self.sender)
        self.reciever = self.userObj.validate(self.sender)
        return {'sender' : self.sender, 'receiver' : self.reciever}
        


    def transaction(self):

        """Documentation"""
        connObj = self.connect()
        
        if(connObj['sender']['status'] == True and connObj['receiver']['status'] == True):
            if(connObj['sender']['balance'] >= self.amount):
                self.connPay.cursor().execute("INSERT INTO payments VALUES (?, ?, ?, ?)", (connObj['sender']['id'], connObj['receiver']['id'], self.amount, self.date))
            else:
                return {'status' : False, 'info' : "Not sufficient balance to perform transaction"}

        else:
            return {'status' : False, 'info' : "Unable to validate reciever"}

        self.disconnect()

    def disconnect(self):

        """Documentation"""
        self.connPay.commit()
        self.connPay.close()
        pass