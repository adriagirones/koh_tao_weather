import requests


def kelvin_to_celcius(temp: float) -> float:
    """
    Return the temperature degrees in celcius

    :param temp: float

    :return: float
    """
    return temp - 273.16


class OpenWeather:
    """
    Does a request to the API to get the current weather from a coordinates that you send.


    :param: api: str, coordinates: tuple

    :return: __repr__ : str
    For example, we can get the info like this.
    Temperature: 29.989999999999952
    Visibility: 10000
    Pressure: 1007
    Humidity: 74
    Wind: Speed: 1.26, degrees: 176
    Sunrise: 1593817439
    Sunset: 1593863147
    Weather: Clouds, few clouds
    """

    def __init__(self, api: str, coordinates: tuple):
        self.api = api
        self.url = f'https://api.openweathermap.org/data/2.5/weather'

        self.lat, self.lon = coordinates

        response = requests.get(f"{self.url}?lat={self.lat}&lon={self.lon}&appid={self.api}").json()

        self.temperature = kelvin_to_celcius(float(response['main']['temp']))
        self.pressure = response['main']['pressure']
        self.humidity = response['main']['humidity']
        self.wind = f"Speed: {response['wind']['speed']}, degrees: {response['wind']['deg']}"
        self.sunrise = response['sys']['sunrise']
        self.sunset = response['sys']['sunset']
        self.weather = f"{response['weather'][0]['main']}, {response['weather'][0]['description']}"

    def __repr__(self):
        return f"Temperature: {self.temperature} \n" \
               f"Pressure: {self.pressure} \n" \
               f"Humidity: {self.humidity} \n" \
               f"Wind: {self.wind} \n" \
               f"Sunrise: {self.sunrise} \n" \
               f"Sunset: {self.sunset} \n" \
               f"Weather: {self.weather}"


if __name__ == '__main__':
    OP = OpenWeather('652661b4d9b718379cbe5cca2f4a0243', ('10.100051', '99.840210'))
    print(OP)
