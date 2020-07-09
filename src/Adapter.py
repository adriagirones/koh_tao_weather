from abc import ABC

import numpy

from OpenWeather import OpenWeather
from Weather import Weather
from ClimaCell import ClimaCell


class Adapter(Weather, ABC):

    def __init__(self, coordinates: tuple):
        # koh_tao coordinates = ('10.100051', '99.840210')
        self._OP = OpenWeather('652661b4d9b718379cbe5cca2f4a0243', coordinates)
        self._CC = ClimaCell('N9sVmSxG9QpcpJ7xidHgq9rkdSwjGDB1', coordinates)

    def get_temperature(self):
        return numpy.mean([self._OP.temperature, self._CC.temp])

    def get_wind(self):
        pass

    def get_weather(self):
        # TODO: add a list of possible answers
        # TODO: mainstream 2 to 1 answers
        return self._OP.weather_main, self._CC.weather_code
