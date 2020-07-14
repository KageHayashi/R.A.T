from etc import *
from colors import color
from .request import requestForecast

class WeatherInterface():
    name = "Weather Forecast"
    description = "Get weather forecast for any city in the US"
    city = ""
    state = ""
    forecast = None

    def __init__(self):
        self.name = "Weather Forecast"
        self.description = "Get weather forecast for any city in the US"
        self.city = ""
        self.state = ""
        self.forecast = None
    
    def load(self):
        clear_screen()
        print(weatherlogo)
        print(f"= {self.description} =")
        print(f'{color.HEADER}')

        print(f'{color.reset}')
        if self.state == "":
            print(f"[ ] State: {color.OKBLUE} {self.state}")
        else:
            print(f"{color.reset}[{color.OKGREEN}+{color.reset}] State: {color.OKBLUE} {self.state}")
        print(f'{color.reset}')

        if self.city == "":
            print(f"[ ] City: {color.OKBLUE} {self.city}")
        else:
            print(f"{color.reset}[{color.OKGREEN}+{color.reset}] City: {color.OKBLUE} {self.city}")

        print(f'{color.reset}')

        if self.city != "" and self.state != "":
            self.forecast = requestForecast(self.state, self.city)
        # print(requestForecast("california", "san francisco"))
        if self.forecast is not None:
            print(self.forecast)

        print("[0] -- Back")
        print()
        self.prompt()



    def prompt(self):
        option = input(weatherprompt)
        if "city" in option:
            option = option.split('=')
            #print(option)
            self.city = option[-1].replace(' ', '')
            self.load()

        elif "state" in option:
            option = option.split('=')
            self.state = option[-1].replace(' ', '')
            #print(option)
            self.load()
