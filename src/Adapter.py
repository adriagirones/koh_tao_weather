from abc import ABC
from itertools import chain

import numpy
import pandas as pd

from ClimaCell import ClimaCell
from OpenWeather import OpenWeather
from Weather import Weather


class Adapter(Weather, ABC):
    """
    Adapter class for our weather application

    :param
    coordinates: tuple
    """

    def __init__(self, coordinates: tuple):
        # koh_tao coordinates = ('10.100051', '99.840210')
        self.OP = OpenWeather('652661b4d9b718379cbe5cca2f4a0243', coordinates)
        self.CC = ClimaCell('N9sVmSxG9QpcpJ7xidHgq9rkdSwjGDB1', coordinates)

    def get_temperature(self) -> int:
        """
        Get the current temperature

        :return:
        temperature: int
        """
        return numpy.mean([self.OP.temperature, self.CC.temp])

    def get_wind(self) -> str:
        """
        Get wind direction, degrees

        :return:
        wind: str
        """
        return numpy.mean([self.OP.wind_speed, self.CC.wind_speed]), convert_degrees_compass_direction(
            round(numpy.mean([self.OP.wind_degrees, self.CC.wind_direction]))), numpy.mean(
            [self.OP.wind_degrees, self.CC.wind_direction])

    def get_weather(self) -> str:
        """
        Get the current weather conditions

        :return:
        weather: str
        """
        return f"Our sources reveal the weather is {(self.CC.weather_code).replace('_', ' ').lower()} " \
               f"and thus will have {str.capitalize(self.OP.weather_main).lower()}"


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
            return direction


def create_dataframe(adapter: Adapter) -> pd.DataFrame:
    """
    Create a pandas dataframe with all the information from all the API

    :return: df: pd.DataFrame
    """
    data = [
        {'Temperature': adapter.OP.temperature, 'Wind Speed': adapter.OP.wind_speed,
         'Wind Direction': f"{convert_degrees_compass_direction(round(adapter.OP.wind_degrees))}({adapter.OP.wind_degrees})",
         'Weather': adapter.OP.weather_main},
        {'Temperature': adapter.CC.temp, 'Wind Speed': adapter.CC.wind_speed,
         'Wind Direction': f"{convert_degrees_compass_direction(round(adapter.CC.wind_direction))}({adapter.CC.wind_direction})",
         'Weather': adapter.CC.weather_code}
    ]
    df = pd.DataFrame(data, columns=['Temperature', 'Wind Speed', 'Wind Direction', 'Weather'], index=['OW', 'CC'])
    return df


def create_plot(frame: pd.DataFrame) -> pd.DataFrame.plot:
    return frame.plot.bar(title="Best graph ever")

