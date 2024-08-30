from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()


def get_weather(city):
    api_key = os.getenv('API_KEY')
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast"


    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    weather_response = requests.get(base_url, params=params)


    forecast_response = requests.get(forecast_url, params=params)

    if weather_response.status_code != 200 or forecast_response.status_code != 200:
        return {'error': 'City not found. Please check the city name.'}

    weather_data = weather_response.json()
    forecast_data = forecast_response.json()

    return {'current': weather_data, 'forecast': forecast_data}

