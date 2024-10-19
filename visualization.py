from dash import Dash, html, dcc
import plotly.graph_objs as go

# Create the dashboard
def create_dashboard(daily_summary, processed_data, alerts):
    cities = list(daily_summary.keys())
    avg_temps = [summary['avg_temp'] for summary in daily_summary.values()]
    avg_humidities = [summary['avg_humidity'] for summary in daily_summary.values()]
    
    # Interactive temperature graph
    temp_fig = go.Figure()
    temp_fig.add_trace(go.Scatter(x=cities, y=avg_temps, mode='lines+markers', name='Average Temperature (°C)'))
    temp_fig.update_layout(title='Average Temperature by City', xaxis_title='City', yaxis_title='Temperature (°C)')

    # Interactive humidity graph
    humidity_fig = go.Figure()
    humidity_fig.add_trace(go.Scatter(x=cities, y=avg_humidities, mode='lines+markers', name='Average Humidity (%)'))
    humidity_fig.update_layout(title='Average Humidity by City', xaxis_title='City', yaxis_title='Humidity (%)')

    # Initialize the Dash app
    app = Dash(__name__)

    # Display processed weather data and daily summaries
    processed_data_display = [html.P(f"{city}: {data}") for city, data in processed_data.items()]
    summary_display = [html.P(f"{city}: {summary}") for city, summary in daily_summary.items()]

    # Display alerts
    alert_display = html.Div([html.P(alert) for alert in alerts], style={'color': 'red', 'font-weight': 'bold'})

    # Define the layout for the dashboard
    app.layout = html.Div([
        html.H1("Weather Dashboard"),
        html.H2("Processed Weather Data"),
        html.Div(processed_data_display),
        html.H2("Daily Weather Summaries"),
        html.Div(summary_display),
        html.H2("Alerts"),
        alert_display,
        dcc.Graph(
            id='temp-graph',
            figure=temp_fig
        ),
        dcc.Graph(
            id='humidity-graph',
            figure=humidity_fig
        )
    ])

    app.run_server(debug=True)


