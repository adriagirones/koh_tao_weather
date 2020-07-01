from src.Weather import Weather


class OpenWeather(Weather):

    def __init__(self, api: str):
        self.url = f'api.openweathermap.org/data/2.5/weather?'
        self.city_name = ''
        self.city_id = ''
        self.lat = ''
        self.lon = ''
        self.country = ''
        self.zip_code = ''
        self.url_city_name = self.url + f'q={self.city_name},{self.country}&appid={self.API}'
        self.url__city_id = self.url = f'id={self.city_id}&appid={self.API}'
        self.url_geographic_coordinates = self.url + f'lat={self.lat}&lon={self.lon}&appid={self.API}'
        self.url_zip_code = self.url + f'zip={self.zip_code},{self.country}&appid={self.API}'
        self.humidity = ''
        self.temperature = ''
        self.pressure = ''
        self.wind_information = ''
        self.location = ''
