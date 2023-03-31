import Exchange.exchange.exchange_functions as Ex

exchangeObj = Ex.Exchange()

## get list of all currencies
obj = exchangeObj.currencies()

if(obj['status'] == True):
    print(obj['list'])
else:
    print(obj['message'])


## get rate of any currency

obj = exchangeObj.get_rate('USD', "2023-03-28", 'INR')

if(obj['status'] == True):
    print(obj['rate'])
else:
    print(obj['message'])


## convert currency

obj = exchangeObj.convert('INR', 'USD', 1.0, "2023-03-28")

if(obj['status'] == True):
    print(obj['result'])
else:
    print(obj['message'])