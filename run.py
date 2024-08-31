from flask import Flask, session, redirect, url_for, request, render_template
from datetime import datetime
from api.weather_api import get_weather
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your_default_secret_key')

# Define the datetimeformat filter
def datetimeformat(value, format='%H:%M:%S'):
    return datetime.fromtimestamp(value).strftime(format)

# Register the filter with Jinja2
app.jinja_env.filters['datetimeformat'] = datetimeformat

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'favorites' not in session:
        session['favorites'] = []

    city = request.args.get('city', 'New York')
    weather = None
    if city:
        weather = get_weather(city)

    if request.method == 'POST':
        favorite_city = request.form.get('favorite_city')
        if favorite_city not in session['favorites']:
            session['favorites'].append(favorite_city)

    return render_template('index.html', city=city, weather=weather, favorites=session['favorites'])

@app.route('/remove_favorite/<city>')
def remove_favorite(city):
    session['favorites'].remove(city)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5009)
