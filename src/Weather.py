from abc import ABC, abstractmethod


class Weather(ABC):
    def __init__(self):
        self.API = ''
        self.url = ''

    @abstractmethod
    def get_weather(self, coordinates: tuple) -> str:
        pass
