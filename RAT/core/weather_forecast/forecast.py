from datetime import date
from colors import color
# from .forecast_type import ForecastType
class Forecast:
    def __init__(
        self, 
        state,
        city,
        current_temp,
        humidity,
        wind,
        high_temp=None,
        low_temp=None,
        description='',
        forecast_date=None,):
        self._current_temp = current_temp
        self._high_temp = high_temp
        self._low_temp = low_temp
        self._humidity = humidity
        self._wind = wind
        self._description = description
        self.city = city
        self.state = state
        # self._forecast_type = forecast_type
    
    @property
    def forecast_date(self):
        return self._forecast_date
    @forecast_date.setter
    def forecast_date(self, forecast_date):
        self._forecast_date = forecast_date.strftime("%a %b %d")
    @property
    def current_temp(self):
        return self._current_temp
    @property
    def humidity(self):
        return self._humidity
    @property
    def wind(self):
        return self._wind
    @property
    def description(self):
        return self._description
    @property
    def high_temp(self):
        return self._high_temp

    @property
    def low_temp(self):
        return self._low_temp

    def __str__(self):
        temperature = None
        offset = ' ' * 3
        indent = '\u00A4'

        Status_OK = f'[{color.OKGREEN}+{color.reset}]'
        Status_WARNING = f'[{color.WARNING}-{color.reset}]'
        Status_FAIL = f'[{color.RED}!{color.reset}]'
        Status_HEADER = f'[{color.HEADER}{indent}{color.reset}]'
        Status_KEY = f'{color.OKBLUE}'

        return(f'{Status_HEADER} Today\'s forecast for {Status_KEY}{self.city}, {self.state.title()} {color.reset}\n'
               f'{offset}{Status_OK} Temp: {self.current_temp}\n'
               f'{offset}{Status_OK} Humidity: {self.humidity}\n'
               f'{offset}{Status_OK} Wind: {self.wind}\n'
               f'{offset}{Status_WARNING} High/Low: {self.high_temp}/{self.low_temp}\n'
               )