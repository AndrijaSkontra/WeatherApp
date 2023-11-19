import requests
import dataclasses

@dataclasses.dataclass
class WeatherData:
    city: str
    api_key: str = "2ca5630c7892ba8104791e904382120d"
    url: str = ""

    def __post_init__(self):
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        json_file = requests.get(self.url).json()
        self.weather = json_file["weather"][0]
        self.main = self.weather["main"]
        self.description = self.weather["description"]
        self.icon = self.weather["icon"]
        self.temp = json_file["main"]["temp"]

    def __repr__(self):
        return f"WeatherData(city={self.city}, main={self.main}, description={self.description}, icon={self.icon}, temp={self.temp})"

if __name__ == '__main__':
    weatherTest = WeatherData("zadar")
    print(weatherTest)
