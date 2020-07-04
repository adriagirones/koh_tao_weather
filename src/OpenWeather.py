import datetime

from src.Weather import Weather


class OpenWeather(Weather):

    def __init__(self, api: str):
        self.url = f'api.openweathermap.org/data/2.5/weather?'
        self.url_city_name = self.url + f'q={self.city_name},{self.country}&appid={self.API}'
        self.url__city_id = self.url = f'id={self.city_id}&appid={self.API}'
        self.url_geographic_coordinates = self.url + f'lat={self.lat}&lon={self.lon}&appid={self.API}'
        self.url_zip_code = self.url + f'zip={self.zip_code},{self.country}&appid={self.API}'

        self.city_name, self.country, self.location, self.country, self.wind_information = str
        self.city_id, self.zip_code, self.visibility, self.humidity, self.pressure = int
        self.sunrise, self.sunrise = datetime
        self.lat, self.lon, self.temperature = float  # TODO: convert far to cel

    def get_weather(self, coordinates: tuple) -> str:
        pass
