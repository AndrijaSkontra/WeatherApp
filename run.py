from flask import Flask, render_template, request
from WWAPI2 import WeatherData

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    data = None
    if request.method == "POST":
        city = request.form["cityName"]
        weather_for_zadar = WeatherData(city)
        data = weather_for_zadar
    return render_template("index.html", data=data)
