from abc import ABC
import numpy
from OpenWeather import OpenWeather
from Weather import Weather
from ClimaCell import ClimaCell
import pandas as pd
from itertools import chain



def convert_degrees_compass_direction(degrees: int) -> str:
    """
    Changes the wind direction to a compass direction

    :param
    degrees: int

    :return:
    compass_direction: str
    """
    wind_direction = {
        "N": chain(range(0, 23), range(338, 361)),
        "NE": range(23, 68),
        "E": range(68, 113),
        "SE": range(113, 158),
        "S": range(158, 203),
        "SW": range(203, 248),
        "W": range(248, 293),
        "NW": range(293, 338)
    }
    for direction in wind_direction:
        if degrees in wind_direction[direction]:
            compass_direction = direction
            break

    return compass_direction


class Adapter(Weather, ABC):
    """
    Adapter class for our weather application

    :param
    coordinates: tuple
    """
    def __init__(self, coordinates: tuple):
        # koh_tao coordinates = ('10.100051', '99.840210')
        self._OP = OpenWeather('652661b4d9b718379cbe5cca2f4a0243', coordinates)
        self._CC = ClimaCell('N9sVmSxG9QpcpJ7xidHgq9rkdSwjGDB1', coordinates)
        self.create_dataframe()

    def create_dataframe(self) -> pd.DataFrame:
        """
        Create a pandas dataframe with all the information from all the API

        :return: df: pd.DataFrame
        """
        data = [
            {'Temperature': self._OP.temperature, 'Wind Speed': self._OP.wind_speed,
             'Wind Direction': f"{convert_degrees_compass_direction(round(self._OP.wind_degrees))}({self._OP.wind_degrees})",
             'Weather': self._OP.weather_main},
            {'Temperature': self._CC.temp, 'Wind Speed': self._CC.wind_speed,
             'Wind Direction': f"{convert_degrees_compass_direction(round(self._CC.wind_direction))}({self._CC.wind_direction})",
             'Weather': self._CC.weather_code}
        ]
        df = pd.DataFrame(data, columns=['Temperature', 'Wind Speed', 'Wind Direction', 'Weather'], index=['OW', 'CC'])
        return df

    def get_temperature(self) -> int:
        """
        Get the current temperature

        :return:
        temperature: int
        """
        return numpy.mean([self._OP.temperature, self._CC.temp])

    def get_wind(self) -> str:
        """
        Get wind direction, degrees

        :return:
        wind: str
        """
        return numpy.mean([self._OP.wind_speed, self._CC.wind_speed]), convert_degrees_compass_direction(
            round(numpy.mean([self._OP.wind_degrees, self._CC.wind_direction]))), numpy.mean(
            [self._OP.wind_degrees, self._CC.wind_direction])

    def get_weather(self) -> str:
        """
        Get the current weather conditions

        :return:
        weather: str
        """
        return f"Our sources reveal the weather is {(self._CC.weather_code).replace('_', ' ').lower()} " \
               f"and thus will have {str.capitalize(self._OP.weather_main).lower()}"
