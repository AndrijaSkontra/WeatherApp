import requests
from typing import Tuple, List


class WorkingWithAPI():

    def __init__(self, city):
        self.api_key = "2ca5630c7892ba8104791e904382120d"
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        self.json_file = requests.get(self.url).json()

    def get_lan_lon(self) -> Tuple:
        cord = self.json_file["coord"]
        lon = cord["lon"]
        lan = cord["lat"]
        return lon, lan

    def get_current_weather(self) -> List:
        weather = self.json_file["weather"]
        return weather