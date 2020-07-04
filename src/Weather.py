from abc import ABC, abstractmethod


class Weather(ABC):
    def __init__(self):
        self.API = ''
        self.url = ''