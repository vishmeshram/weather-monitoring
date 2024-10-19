

from weather_api import fetch_weather_data
from data_processing import process_weather_data, calculate_daily_summary
from visualization import create_dashboard
from alerts import check_thresholds, send_alerts

def main():
    daily_data = {}
    
    for weather_data in fetch_weather_data():
        processed_data = process_weather_data(weather_data)
        
        # Aggregate data for the day
        for city, data in processed_data.items():
            if city not in daily_data:
                daily_data[city] = []
            daily_data[city].append(data)
        
        # Check for alerts
        alerts = check_thresholds(processed_data)
        send_alerts(alerts)
        
        # Calculate daily summaries
        daily_summary = calculate_daily_summary(daily_data)

        # Create the dashboard with processed data, summaries, and alerts
        create_dashboard(daily_summary, processed_data, alerts)

if __name__ == "__main__":
    main()
