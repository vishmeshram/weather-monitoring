import requests
import time

API_KEY = 'ebeabc1b67241ca3215e7118fb273424'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

def get_weather_data(city):
    url = API_URL.format(city=city, key=API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}")
        return None

def fetch_weather_data(interval=300):
    while True:
        weather_data = {}
        for city in CITIES:
            data = get_weather_data(city)
            if data:
                weather_data[city] = data
        yield weather_data
        time.sleep(interval)
