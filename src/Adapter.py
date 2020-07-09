import enum
from abc import ABC
import numpy
from OpenWeather import OpenWeather
from Weather import Weather
from ClimaCell import ClimaCell


def convert_degrees_compass_direction(degrees):
    return {
        range(337.5, 22.5): "N",
        range(22.5, 67.5): "NE",
        range(67.5, 112.5): "E",
        range(112.5, 157.5): "SE",
        range(157.5, 202.5): "S",
        range(202.5, 247.5): "SW",
        range(247.5, 292.5): "W",
        range(292.5, 337.5): "NW",

    }[degrees]


class Adapter(Weather, ABC):

    def __init__(self, coordinates: tuple):
        # koh_tao coordinates = ('10.100051', '99.840210')
        self._OP = OpenWeather('652661b4d9b718379cbe5cca2f4a0243', coordinates)
        self._CC = ClimaCell('N9sVmSxG9QpcpJ7xidHgq9rkdSwjGDB1', coordinates)

    def get_temperature(self):
        return numpy.mean([self._OP.temperature, self._CC.temp])

    def get_wind(self):
        return numpy.mean([self._OP.wind_speed, self._CC.wind_speed]), convert_degrees_compass_direction(
            numpy.mean([self._OP.wind_degrees, self._CC.wind_direction])), numpy.mean(
            [self._OP.wind_degrees, self._CC.wind_direction])

    def get_weather(self):
        # TODO: add a list of possible answers
        # TODO: mainstream 2 to 1 answers
        return self._OP.weather_main, self._CC.weather_code
