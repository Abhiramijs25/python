from datetime import datetime
import json

def get_trip(city, date, comment):
    """
    Returns trip details in dictionary format
    """
    return {
        "city": city,
        "date": date,
        "comment": comment
    }

trips = [
    get_trip("newyork", "15-03-2025", "Christmas lights everywhere!"),
    get_trip("paris", "20-04-2025", "Beautiful spring weather!"),
    get_trip("tokyo", "17-06-2025", "Loved the street food!")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

print(json.dumps(trips, indent=4))