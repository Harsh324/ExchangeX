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

        """
        ### Function Description : 

            This Function is used to parse the api request.\n
            For different purpose different type of query is\n
            given to the api hence the append parameter will vary according to that.\n
            Returns the response obtained as json object.\n
            
        ### Function Parameters : 
            
            # append : 
                This Parameter takes the query part of the API request\n

        """

        response = requests.request("GET", self.url + append, headers = self.headers, data = self.payload)
        return response.json()


    def currencies(self):

        """
        ### Function Description : 

            This Function is used to get list of all available currencies worldwide.\n
            Using the parseApi method query is given and list of currencies is obtained.\n
            Returns the list of currencies as json object.\n

        """

        currencydict = self.parse_api("symbols")
        if(currencydict['success'] == True):
            return {'status' : True, 'list' : list(currencydict['symbols'])}
        else:
            return {'status' : False, 'message' : str(currencydict['error']['info'])}


    def get_rate(self, currency, date = "2023-03-28", base = "INR"):

        """
        ### Function Description : 

            This Function is used to get the rate of any currency\n
            as per the base currency using api request.\n
            Returns the json object with the rates of the input currency.\n
            
        ### Function Parameters : 
            
            # currency : 
                This Parameter is the input currency of which we want to get the rate.\n
            
            # date : 
                This parameter takes the date of whcih we want the rate.\n

            # base : 
                This parameter takes the base currecnt in whcih we want the rates is given.\n
        """

        append = date + "?symbols=" + currency + "&base=" + base
        ratedict = self.parse_api(append)
        if(ratedict['success'] == True):
            return {'status' : True, 'rate' : ratedict['rates'][currency]}
        else:
            return {'status' : False, 'message' : ratedict['error']['info']}




    def convert(self, fromCurrency = 'INR', toCurrency = 'USD',
                amount = 1.0, date = "2023-03-25") -> float:

        """
        ### Function Description : 

            This Function is used to convert rate from\n
            one currency to other using api requests.\n
            Returns the json object with the value of the currency\n
            in the base currency of the input currency.\n
            
        ### Function Parameters : 
            
            # fromCurrency : 
                This Parameter is the input currency of which we want to convert.\n
            
            # toCurrency : 
                This Parameter is the base currency in which we want to convert.\n

            # date : 
                This parameter takes the date of whcih we want the rate.\n

            # amount : 
                This parameter takes value we want to convert.\n
        """


        append = "convert?to=" + toCurrency + "&from=" + fromCurrency + "&amount=" + str(amount) + "&date=" + date
        conversiondict = self.parse_api(append)
        if(conversiondict['success'] == True):
            return {'status' : True, 'result' : conversiondict['result']}
        else:
            return {'status' : False, 'message' : conversiondict['error']['info']}