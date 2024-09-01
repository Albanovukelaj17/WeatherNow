from collections import defaultdict
from datetime import datetime

def group_weather_by_day(forecast):
    grouped = defaultdict(list)
    for entry in forecast:
        # Extrahiere das Datum (ohne Zeit) als Schlüssel
        date = entry['dt_txt'].split(' ')[0]
        grouped[date].append(entry)
    return grouped
