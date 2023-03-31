import Payment.payment.payment_functions as Py



## payment between sender and reciever

senderUserId = "1234"
recieverUserId = "5678"
amount = 1000
date = "2023-03-28"
paymentObj = Py.Payment(senderUserId, recieverUserId, amount, date).transaction()

if(paymentObj['status'] == True):
    print(paymentObj['info'])
else:
    print(paymentObj['info'])


    







