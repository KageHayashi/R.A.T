import requests
from bs4 import BeautifulSoup
import json
import os.path
import pathlib
from difflib import get_close_matches
from colors import color

exchangebase = "https://api.exchangeratesapi.io/latest?base="

class Exchange():
    def __init__(self, base, exchange_currency, exchange_rate):
        self.base = base
        self.exchange_currency = exchange_currency
        self.exchange_rate = format(float(exchange_rate), '.2f')

    def __str__(self):
        offset = ' ' * 3
        indent = '\u00A4'
        
        Status_OK = f'[{color.OKGREEN}+{color.reset}]'
        Status_WARNING = f'[{color.WARNING}-{color.reset}]'
        Status_FAIL = f'[{color.RED}!{color.reset}]'
        Status_HEADER = f'[{color.HEADER}{indent}{color.reset}]'
        Status_KEY = f'{color.OKBLUE}'

        return(f'{Status_HEADER} Exchange from  {Status_KEY}{self.base} {color.reset} to {Status_KEY}{self.exchange_currency} {color.reset}\n'
               f'{offset}{Status_OK} Base: 1 {self.base}\n'
               f'{offset}{Status_OK} Exchange Rate: {self.exchange_rate} {self.exchange_currency}\n'
               )

def find_rates(base, exchange_currency):
    base = base.upper()
    request = requests.get(exchangebase + base)
    data = request.json()['rates']
    exchange_currency = exchange_currency
    return(Exchange(base, exchange_currency, data[exchange_currency]))
