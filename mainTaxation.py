import Taxation.taxation.taxation_functions as Tx

taxationObj = Tx.Taxation()

## applying tax to the currency exchange

obj = taxationObj.apply_tax('USD', 'INR', "2023-03-28")

if(obj['status'] == True):
    print(obj['tax'])
else:
    print(obj['message'])
