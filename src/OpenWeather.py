import datetime

import requests

from src.Weather import Weather


class OpenWeather(Weather):

    def __init__(self, api: str):
        self.api = api
        self.lat = self.lon = self.wind = str
        self.visibility = self.humidity = self.pressure = int
        self.sunrise = self.sunrise = datetime
        self.temperature = float  # TODO: convert far to cel
        self.url = f'https://api.openweathermap.org/data/2.5/weather?'

    def get_weather(self, coordinates: tuple) -> str:
        """
        Do API call to get the weather from a concrete coordinates
        :param coordinates: tuple
        :return: weather: str
        """
        self.lat = coordinates.__getitem__(0)
        self.lon = coordinates.__getitem__(1)
        url_geographic_coordinates = self.url + f'lat={self.lat}&lon={self.lon}&appid={self.api}'
        response = requests.get(url_geographic_coordinates).json()
        self.temperature = response['main']['temp']
        self.visibility = response['visibility']
        self.pressure = response['main']['pressure']
        self.humidity = response['main']['humidity']
        self.wind = f"Speed: {response['wind']['speed']}, degrees: response['wind']['deg']"
        self.sunrise = response['sys']['sunrise']
        self.sunrise = response['sys']['sunset']
        weather = f"{response['weather'][0]['main']}, {response['weather'][0]['description']}"

        return weather


if __name__ == '__main__':
    OP = OpenWeather('652661b4d9b718379cbe5cca2f4a0243')
    info = OP.get_weather(('10.100051', '99.840210'))
