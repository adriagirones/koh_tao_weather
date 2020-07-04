from abc import ABC, abstractmethod


class Weather(ABC):
    def __init__(self):
        self.API = ''
        self.url = ''

    @abstractmethod
    def get_temperature(self):
        pass

    @abstractmethod
    def get_wind(self):
        pass

    @abstractmethod
    def get_visability(self):
        pass

    @abstractmethod
    def get_weather(self):
        pass
