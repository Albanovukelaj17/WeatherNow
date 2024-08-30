from flask import Flask, request, render_template
from api.weather_api import get_weather

app = Flask(__name__)

@app.route('/')
def index():
    city = request.args.get('city', 'New York')
    weather = get_weather(city)
    if 'error' in weather:
        return weather['error']
    return render_template('index.html', city=city, weather=weather)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
