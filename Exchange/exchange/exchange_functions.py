import requests

class Exchange():

    def __init__(self) -> None:
        self.base = 'INR'
        self.url = "https://api.apilayer.com/fixer/"
        self.headers = {
            "apikey" : "6CEeYI140Af0AdsG0s2tdBJRdv5MUWPg"
        }   
        self.payload = {

        }     

    def parse_api(self, append):

        """Documentation"""

        response = requests.request("GET", self.url + append, headers = self.headers, data = self.payload)
        return response.json()


    def currencies(self):

        """Documentation"""

        currencydict = self.parse_api("symbols")
        if(currencydict['success'] == True):
            return {'status' : True, 'list' : list(currencydict['symbols'])}
        else:
            return {'status' : False, 'message' : str(currencydict['error']['info'])}


    def get_rate(self, currency, date = "2023-03-28", base = "INR"):

        """Documentation"""
        append = date + "?symbols=" + currency + "&base=" + base
        ratedict = self.parse_api(append)
        if(ratedict['success'] == True):
            return {'status' : True, 'rate' : ratedict['rates'][currency]}
        else:
            return {'status' : False, 'message' : ratedict['error']['info']}

    def get_variation(self):

        """Documentation"""
        pass



    def convert(self, from_currency = 'INR', to_currency = 'USD',
                amount = 1.0, date = "2023-03-25") -> float:

        """Documentation"""


        append = "convert?to=" + to_currency + "&from=" + from_currency + "&amount=" + str(amount) + "&date=" + date
        conversiondict = self.parse_api(append)
        if(conversiondict['success'] == True):
            return {'status' : True, 'result' : conversiondict['result']}
        else:
            return {'status' : False, 'message' : conversiondict['error']['info']}