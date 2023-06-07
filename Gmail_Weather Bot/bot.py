import smtplib
import requests

# Gmail credentials
GMAIL_USERNAME = "YOUR_GMAIL_ADDRESS"
GMAIL_PASSWORD = "YOUR_PASSWORD"

# OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

def send_email(subject, body, to_email):
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        # Create the email message
        subject = subject.encode("utf-8")
        body = body.encode("utf-8")
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(GMAIL_USERNAME, to_email, message)

        # Close the connection
        server.close()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

def get_weather(city):
    try:
        # Make a request to OpenWeatherMap API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Extract relevant weather information
        weather_main = data["weather"][0]["main"]
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Create the weather report message
        report = f"Weather report for {city}:"
        report += f"Weather: {weather_main} ({weather_description})"
        report += f"Temperature: {temperature}°C"
        report += f"Humidity: {humidity}%"

        return report
    except Exception as e:
        print(f"Error fetching weather data: {str(e)}")

# Get the city from the user
city = input("Enter the city name: ")

# Fetch the weather report
weather_report = get_weather(city)

if weather_report:
    # Send the weather report via email
    subject = f"Weather Report for {city}"
    to_email = input("Enter your email address: ")

    send_email(subject, weather_report, to_email)
else:
    print("Unable to fetch weather report for the enterd city.")
