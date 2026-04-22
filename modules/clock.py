from datetime import datetime


def get_time_data():
    now = datetime.now()

    return {
        "time": now.strftime("%H:%M"),
        "date": now.strftime("%d.%m.%Y"),
        "weekday": now.strftime("%A")
    }