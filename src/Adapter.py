from abc import ABC

from Weather import Weather


class Adapter(Weather, ABC):

    def get_temperature(self):
        pass

    def get_wind(self):
        pass

    def get_visability(self):
        pass

    def get_weather(self):
        pass
