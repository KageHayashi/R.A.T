from etc import *
from .exchange import find_rates

class ExchangeInterface():
    name = "Currency Exchange"
    description = "Get weather forecast for any city in the US"
    def __init__(self):
        self.name = "Currency Exchange"
        self.description = "Currency Exchange Tool"
        self.base = ""
        self.exchange_currency = ""
        self.exchange = None
    
    def load(self):
        clear_screen()
        print(exchangelogo)
        print(f"= {self.description} =")
        print(f'{color.HEADER}')
        
        print(f'{color.reset}')
        if self.base == "":
            print(f"[ ] Base: {color.OKBLUE} {self.base}")
        else:
            print(f"{color.reset}[{color.OKGREEN}+{color.reset}] Base: {color.OKBLUE} {self.base}")
        print(f'{color.reset}')

        if self.exchange_currency == "":
            print(f"[ ] To: {color.OKBLUE} {self.exchange_currency}")
        else:
            print(f"{color.reset}[{color.OKGREEN}+{color.reset}] To: {color.OKBLUE} {self.exchange_currency}")
        print()
        
        if self.base != "" and self.exchange_currency != "":
            self.exchange = find_rates(self.base, self.exchange_currency)
        if self.exchange is not None:
            print(self.exchange)

        print(f'{color.reset}')
        print("[0] -- Back")
        print()
        self.prompt()


    def prompt(self):
        option = input(exchangeprompt)
        if "base" in option:
            option = option.split('=')
            #print(option)
            self.base = option[-1].replace(' ', '').upper()
            self.load()

        elif "to" in option:
            option = option.split('=')
            self.exchange_currency = option[-1].replace(' ', '').upper()
            #print(option)
            self.load()