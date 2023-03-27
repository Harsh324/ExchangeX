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


        print("IN parse_api")
        response = requests.request("GET", self.url + append, headers = self.headers, data = self.payload)
        status = self.exception(response.status_code)
        if(status):
            return response.json(), status
        return {}, status

    

    def currencies(self):

        """Documentation"""


        print("IN currencies")
        currencydict, status = self.parse_api("symbols")
        if(status):
            print(currencydict['symbols']['AED'])


    def get_rate(self, date, currency):

        """Documentation"""

        print("IN get_rate")
        append = date + "?symbols=" + currency + "&base=" + self.base
        ratedict = self.parse_api(append)
        print(ratedict)

    def get_variation(self):

        """Documentation"""
        pass



    def convert(self, from_currency = 'INR', to_currency = 'USD',
                amount = 1.4, date = "2023-03-25") -> float:

        """Documentation"""


        append = "convert?to=" + to_currency + "&from=" + from_currency + "&amount=" + str(amount) + "&date=" + date
        conversiondict = self.parse_api(append)

        print(conversiondict)


    def exception(self, status, ):
        
        """Documentation"""
        

        if(status >= 200 and status < 300):
            return True
        elif(status == 400):
            print("Bad request, The request was unacceptable, Check for any missing parameters")
            return False
        elif(status == 401):
            print("Unauthorized	No valid API key provided.")
            return False
        elif(status == 404):
            print("Not Found, The requested resource doesn't exist.")
            return False
        elif(status == 429):
            print("Too many requests API request limit exceeded.")
            return False
        elif(status >= 500):
            print("Unknow error occured")
            return False