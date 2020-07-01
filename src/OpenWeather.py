class OpenWeather:

    def __init__(self):
        self.API = ''
        self.city_name = ''
        self.city_id = ''
        self.lon = ''
        self.lat = ''
        self.country = ''
        self.zip_code = ''
        self.url_city_name = f'api.openweathermap.org/data/2.5/weather?' \
                             f'q={self.city_name},{self.country}&appid={self.API}'
        self.url__city_id = f'api.openweathermap.org/data/2.5/weather?' \
                            f'id={self.city_id}&appid={self.API}'
        self.url_geographic_coordinates = f'api.openweathermap.org/data/2.5/weather?' \
                                          f'lat={self.lat}&lon={self.lon}&appid={self.API}'
        self.url_zip_code = f'api.openweathermap.org/data/2.5/weather?' \
                            f'zip={self.zip_code},{self.country}&appid={self.API}'
