import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ALERT_THRESHOLD_TEMP = 35  # Celsius

def check_thresholds(weather_data, threshold=ALERT_THRESHOLD_TEMP):
    alerts = []
    for city, data in weather_data.items():
        if data['temperature'] > threshold:
            alert_message = f"Alert: {city} has exceeded the temperature threshold of {threshold}°C"
            alerts.append(alert_message)
    return alerts

def send_alerts(alerts):
    for alert in alerts:
        print(alert)
        send_email_alert(alert)

# Function to send email alert
def send_email_alert(alert_message):
    sender_email = "itzmevish15@gmail.com"
    receiver_email = "itzmevish15@gmail.com"
    password = "lzivzwzzroabgucz"  # Use App Password if needed
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Weather Alert"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Create the plain-text and HTML versions of your message
    text = f"""\
    Weather Alert:
    {alert_message}
    """
    
    # Add the plain-text version of the message
    part = MIMEText(text, "plain")
    message.attach(part)
    
    # Send the email via Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Email sent to {receiver_email}: {alert_message}")
    except Exception as e:
        print(f"Failed to send email: {e}")
