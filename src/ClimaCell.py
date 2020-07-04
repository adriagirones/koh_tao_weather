from climacell_api.client import ClimacellApiClient


class ClimaCell(ClimacellApiClient):
    def __init__(self, api: str, coordinates: tuple):
        super().__init__(api)
        self.lat, self.lon = coordinates

    def __repr__(self):
        super().realtime(lat=self.lat, lon=self.lon, fields=[
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


if __name__ == '__main__':
    climacell = ClimaCell('N9sVmSxG9QpcpJ7xidHgq9rkdSwjGDB1', ('10.100051', '99.840210'))
