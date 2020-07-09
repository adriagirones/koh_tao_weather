import enum
from abc import ABC
import numpy
from OpenWeather import OpenWeather
from Weather import Weather
from ClimaCell import ClimaCell
import pandas as pd
from itertools import chain


def convert_degrees_compass_direction(degrees):
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
    value = ''
    for direction in wind_direction:
        if degrees in wind_direction[direction]:
            value = direction
            break

    return value


class Adapter(Weather, ABC):

    def __init__(self, coordinates: tuple):
        # koh_tao coordinates = ('10.100051', '99.840210')
        self._OP = OpenWeather('652661b4d9b718379cbe5cca2f4a0243', coordinates)
        self._CC = ClimaCell('N9sVmSxG9QpcpJ7xidHgq9rkdSwjGDB1', coordinates)
        self.create_dataframe()

    def create_dataframe(self):
        data = [
            {'Temperature': self._OP.temperature, 'Wind Speed': self._OP.wind_speed,
             'Wind Direction': f"{convert_degrees_compass_direction(round(self._OP.wind_degrees))}({self._OP.wind_degrees})",
             'Weather': self._OP.weather_main},
            {'Temperature': self._CC.temp, 'Wind Speed': self._CC.wind_speed,
             'Wind Direction': f"{convert_degrees_compass_direction(round(self._CC.wind_direction))}({self._CC.wind_direction})",
             'Weather': self._CC.weather_code}
        ]
        df = pd.DataFrame(data, columns=['Temperature', 'Wind Speed', 'Wind Direction', 'Weather'], index=['OW', 'CC'])
        print(df)

    def get_temperature(self):
        return numpy.mean([self._OP.temperature, self._CC.temp])

    def get_wind(self):
        return numpy.mean([self._OP.wind_speed, self._CC.wind_speed]), convert_degrees_compass_direction(
            round(numpy.mean([self._OP.wind_degrees, self._CC.wind_direction]))), numpy.mean(
            [self._OP.wind_degrees, self._CC.wind_direction])

    def get_weather(self):
        pass


if __name__ == '__main__':
    adapter = Adapter(('10.100051', '99.840210'))
