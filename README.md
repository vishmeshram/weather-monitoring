# weather-monitoring
# Weather Monitoring System
##Dashboard
![Dashboard](https://github.com/vishmeshram/weather-monitoring/blob/main/Screenshot%202024-10-19%20165111.png?raw=true)
![Dashboard](https://github.com/vishmeshram/weather-monitoring/blob/main/Screenshot%202024-10-19%20165144.png?raw=true)
![Dashboard](https://github.com/vishmeshram/weather-monitoring/blob/main/Screenshot%202024-10-19%20165203.png?raw=true)



## Overview
This is a real-time weather monitoring system that fetches weather data from the OpenWeatherMap API and provides interactive visualizations. The system also triggers SMS alerts if the temperature exceeds a user-defined threshold.

## Features
- Real-time weather data fetching for multiple cities
- Data visualization using Dash (interactive graphs for temperature and humidity)
- SMS alerts using Twilio when weather thresholds are exceeded
- Dashboard displaying weather summaries and alerts

## Project Structure
```plaintext
/Weather-Monitoring-System
│
├── /weather_api.py        # Fetches real-time weather data
├── /data_processing.py    # Processes and summarizes weather data
├── /alerts.py             # Checks for thresholds and sends SMS alerts
├── /visualization.py      # Generates the dashboard with graphs
├── /main.py               # The entry point to run the application
├── /requirements.txt      # Dependencies for the project
└── /README.md             # Project documentation



