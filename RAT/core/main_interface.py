import sys
import os
from etc import *
from colors import color
from weather_forecast import weather_interface
from currency_exchange import exchange_interface

class MainInterface():
    def __init__(self):
        self.name = 'R.A.T'
        self.description = "A collection of randomly assembled tools that you might use"
        self.author = "KageHayashi"
        self.tools = [weather_interface.WeatherInterface(), exchange_interface.ExchangeInterface()]
        self.load()

    def load(self):
        clear_screen()
        print(ratlogo)
        print(description)
        print()
        for i in range(len(self.tools)):
            print(f"{color.HEADER}   [{i + 1}] -- {self.tools[i].name}")
        print()
        print("---------------------------------------")
        print()
        print("   [0] -- EXIT")
        print(f'{color.reset}')
        choice = int(input(ratprompt))
        clear_screen()
        if choice == 0:
            sys.exit(0)
        else:
            self.tools[choice-1].load()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()
    


