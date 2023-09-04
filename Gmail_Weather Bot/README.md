# Gmail Bot - Weather Report

This Python script allows you to send the weather report of a specified city via Gmail.

## Prerequisites

- Python 3.x
- `requests` library: You can install it using `pip install requests`.
- `secure-smtplib` library: You can install it using `pip install secure-smtplib`.
- Gmail account: You will need a Gmail account to send the email.
- OpenWeatherMap API key: You need to sign up and obtain an API key from OpenWeatherMap (https://openweathermap.org/) to fetch weather data.

## Setup

1. Clone this repository or download the script file `gmail_bot.py` to your local machine.

2. Install the required dependencies by running the following command:

3. Open the `gmail_bot.py` script in a text editor.

4. Replace the following placeholders in the script with your own values:
- `GMAIL_USERNAME`: Your Gmail email address.
- `GMAIL_PASSWORD`: Your Gmail app password (generated for this script).
- `API_KEY`: Your OpenWeatherMap API key.

5. Save the script.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where the `gmail_bot.py` script is located.

3. Run the script using the following command:

4. Enter the city name when prompted.

5. Enter the email address where you want to receive the weather report.

6. The script will fetch the weather report and send it via email to the specified email address.

Note: Make sure to enable "Less Secure Apps" access in your Gmail account settings, and generate an app password specifically for this script.

## License

This script is licensed under the [MIT License](LICENSE).
