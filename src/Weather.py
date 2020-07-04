from abc import ABC, abstractmethod


class Weather(ABC):
    @abstractmethod
    def get_temperature(self):
        pass

    @abstractmethod
    def get_wind(self):
        pass

    @abstractmethod
    def get_weather(self):
        pass
