from flask import Flask, session, redirect, url_for, request, render_template
from datetime import datetime
from api.weather_api import get_weather
import os
from dotenv import load_dotenv
from collections import defaultdict
from datetime import datetime
from utils.data_processing import group_weather_by_day


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', '')


def datetimeformat(value, format='%H:%M:%S'):
    return datetime.fromtimestamp(value).strftime(format)

# Register the filter with Jinja2
app.jinja_env.filters['datetimeformat'] = datetimeformat

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'favorites' not in session:
        session['favorites'] = []

    city = request.args.get('city', 'New York')
    weather = None
    grouped_weather = {}
    if city:
        weather = get_weather(city)
        if 'forecast' in weather:
            grouped_weather = group_weather_by_day(weather['forecast']['list'])

    if request.method == 'POST':
        favorite_city = request.form.get('favorite_city')
        if favorite_city not in session['favorites']:
            session['favorites'].append(favorite_city)

    return render_template('index.html', city=city, weather=weather, grouped_weather=grouped_weather, favorites=session['favorites'])

@app.route('/remove_favorite/<city>')
def remove_favorite(city):
    session['favorites'].remove(city)
    return redirect(url_for('index'))

@app.route('/weather-map')
def weather_map():
    api_key = os.getenv('API_KEY')
    return render_template('weather_map.html', api_key=api_key)

if __name__ == '__main__':
    app.run(debug=True, port=5015)
