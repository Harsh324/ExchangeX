import sqlite3 as Sq

class Payment():

    def __init__(self, senderAccountNo, receiverAccountNo, amount, date) -> None:
        self.sender = senderAccountNo
        self.reciever = receiverAccountNo
        self.amount = amount
        self.date = date
        self.connPay = Sq.connect('payment.db').cursor()
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
                self.connPay.execute("INSERT INTO payments VALUES (?, ?, ?, ?)", (connObj['sender']['id'], connObj['receiver']['id'], self.amount, self.date))
            else:
                return {'status' : False, 'info' : "Not sufficient balance to perform transaction"}

        else:
            return {'status' : False, 'info' : "Unable to validate reciever"}



        self.disconnect()
        pass

    def disconnect(self):

        """Documentation"""
        pass