from config import DHT_PIN

try:
    import Adafruit_DHT
    SENSOR = Adafruit_DHT.DHT11
except ImportError:
    Adafruit_DHT = None
    SENSOR = None


def read_dht11_data():
    if Adafruit_DHT is None:
        return {
            "temperature_indoor": "--",
            "humidity": "--"
        }

    try:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            return {
                "temperature_indoor": temperature,
                "humidity": humidity
            }

    except Exception:
        pass

    return {
        "temperature_indoor": "--",
        "humidity": "--"
    }