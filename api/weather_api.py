from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()


def get_weather(city):
    api_key = os.getenv('API_KEY')  # Retrieve the API key from the environment
    if not api_key:
        return {"error": "API key not found. Please check your .env file."}

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()


if __name__ == '__main__':
    city = 'London'
    weather_data = get_weather(city)
    print(weather_data)
