import requests
import io
import sys
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class currency_client():
    def __init__(self, api_key):
        self.api_key = api_key
        self.raw_currencyList = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=" + api_key).text
        self.currencyList = list(self.get_currency_list())


    def get_data(self, initial, target, amount=1):
        pair = "{}_{}".format(initial, target)
        getRequest = "https://free.currconv.com/api/v7/convert?q={}&apiKey={}".format(pair, self.api_key)
        res = json.loads(requests.get(getRequest).text)
        rate = res["results"][pair]["val"]
        return rate * amount
        

    def get_currency_list(self):
        data = json.loads(self.raw_currencyList)
        return data["results"].keys()
        

