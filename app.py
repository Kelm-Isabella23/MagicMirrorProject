from flask import Flask, render_template
from modules.clock import get_time_data
from modules.weather import get_weather_data
from modules.sensor_dht11 import read_dht11_data

app = Flask(__name__)


@app.route("/")
def index():
    time_data = get_time_data()
    weather_data = get_weather_data()
    sensor_data = read_dht11_data()

    return render_template(
        "index.html",
        time_data=time_data,
        weather_data=weather_data,
        sensor_data=sensor_data
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)