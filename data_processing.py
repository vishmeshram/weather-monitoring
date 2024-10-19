import datetime

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def process_weather_data(weather_data):
    processed_data = {}
    for city, data in weather_data.items():
        temp_celsius = kelvin_to_celsius(data['main']['temp'])
        processed_data[city] = {
            'temperature': temp_celsius,
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'weather': data['weather'][0]['main'],
            'timestamp': data['dt']
        }
    return processed_data

def calculate_daily_summary(daily_data):
    summary = {}
    for city, records in daily_data.items():
        temps = [record['temperature'] for record in records]
        humidities = [record['humidity'] for record in records]
        weather_conditions = [record['weather'] for record in records]

        summary[city] = {
            'avg_temp': sum(temps) / len(temps),
            'max_temp': max(temps),
            'min_temp': min(temps),
            'avg_humidity': sum(humidities) / len(humidities),
            'dominant_weather': max(set(weather_conditions), key=weather_conditions.count)
        }
    return summary
