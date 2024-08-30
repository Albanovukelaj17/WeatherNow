from flask import Flask, render_template, request
from datetime import datetime
from api.weather_api import get_weather

app = Flask(__name__)

# Define the datetimeformat filter
def datetimeformat(value, format='%H:%M:%S'):
    return datetime.fromtimestamp(value).strftime(format)

# Register the filter with Jinja2
app.jinja_env.filters['datetimeformat'] = datetimeformat

@app.route('/')
def index():
    city = request.args.get('city', 'New York')
    weather = get_weather(city)
    if 'error' in weather:
        return weather['error']
    return render_template('index.html', city=city, weather=weather)

if __name__ == '__main__':
    app.run(debug=True, port=5007)
