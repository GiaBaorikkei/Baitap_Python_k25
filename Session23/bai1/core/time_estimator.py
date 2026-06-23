from datetime import datetime, timedelta


def predict_eta(departure_str, distance_km, speed=60):
    departure = datetime.strptime(
        departure_str,
        "%Y-%m-%d %H:%M:%S"
    )

    hours_needed = distance_km / speed

    eta = departure + timedelta(
        hours=hours_needed
    )

    return eta