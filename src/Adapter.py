from abc import ABC

from OpenWeather import OpenWeather
from Weather import Weather
import numpy


class Adapter(Weather, ABC):

    def __init__(self, coordinates: tuple):
        self._OP = OpenWeather('652661b4d9b718379cbe5cca2f4a0243', coordinates)
        #self._CC = OpenWeather('', coordinates)

    def get_temperature(self):
        return numpy.mean(self._OP.temperature)

    def get_wind(self):
        pass

    def get_weather(self):
        pass
