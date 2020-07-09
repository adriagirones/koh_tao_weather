from climacell_api.client import ClimacellApiClient


class ClimaCell(ClimacellApiClient):
    def __init__(self, api: str, coordinates: tuple):
        super().__init__(api)
        response = super().realtime(lat=coordinates[0], lon=coordinates[1], fields=[
            'temp',
            'feels_like',
            'dewpoint',
            'humidity',
            'wind_speed',
            'wind_direction',
            'wind_gust',
            'baro_pressure',
            'precipitation',
            'precipitation_type',
            # 'precipitation_probability',
            # 'precipitation_accumulation'
            'sunrise',
            'sunset',
            'visibility',
            'cloud_cover',
            'cloud_base',
            'cloud_ceiling',
            # 'cloud_satellite'
            'surface_shortwave_radiation',
            'moon_phase',
            'weather_code'
            # 'weather_groups'
        ])
        data = {key: response.data().measurements[key].value for key, value in response.data().measurements.items()}
        self.__dict__.update(data)

    def __repr__(self):
        return f"Temperature: {self.temp} \n" \
               f"Humidity: {self.humidity} \n" \
               f"Wind: \n" \
               f"   Speed: {self.wind_speed} \n" \
               f"   Gust: {self.wind_gust} \n" \
               f"   Direction: {self.wind_direction} \n" \
               f"Sunrise: {self.sunrise} \n" \
               f"Sunset: {self.sunset} \n" \
               f"Weather:  \n" \
               f"   Main: {self.weather_code} \n"


if __name__ == '__main__':
    climacell = ClimaCell('N9sVmSxG9QpcpJ7xidHgq9rkdSwjGDB1', ('10.100051', '99.840210')).__repr__()
    print(climacell)
