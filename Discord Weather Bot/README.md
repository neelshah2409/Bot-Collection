# Weather Bot
### Your Personal Weather Assistant for Discord

<div align="center">
   <img src="https://forthebadge.com/images/badges/built-with-love.svg" />
   <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" />
   <img src="https://forthebadge.com/images/badges/open-source.svg" />
</div>

It is an intelligent Discord bot that brings real-time weather information right to your server. With just a command, you can instantly retrieve accurate weather details for any city around the globe. Stay informed about temperature, humidity, wind speed, and more with beautiful visual displays. WeatherMate is your go-to companion for planning outings, staying prepared, and impressing your friends with up-to-the-minute weather data.

## Features
- Command-based weather updates for any city
- Detailed forecasts and current conditions
- Interactive visualizations for better understanding
- Global coverage with accurate weather data
- Easy-to-use and customizable settings

## Resources and APIs:
- Python 3.9.9
- Python Discord.py module
- OpenWeatherMap API 
- Discord API

## Usage
To use the Discord Weather Bot, follow these steps:

1. Invite the bot to your Discord server.
2. Configure the bot by providing necessary API keys and settings.
3. Use commands to interact with the bot and get weather information.

## Installation
To run the Discord Weather Bot locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/neelshah2409/Bot-Collection.git
```
2. Navigate to the "Discord Weather Bot" directory:
```
cd Bot-Collection/Discord%20Weather%20Bot
```
3. We are going to be using [OpenWeatherMap](https://openweathermap.org/api) API, which requires an API key. You can get one for free by simply logging in to their website.
4. Open the **main.py** file and replace your `DISCORD_BOT_TOKEN` and `OPEN_WEATHER_MAP_API_KEY`.

```py
token = 'DISCORD_BOT_TOKEN'
api_key = 'OPEN_WEATHER_MAP_API_KEY'
```
5. Install the required dependencies:
```
pip install -r requirements.txt
```
6. Configure the bot by providing the necessary API keys and settings. You can find the configuration file in the config directory.
7. Run the bot:
```
python3 bot.py
```

## Development

Want to contribute? Great!

Contributions to the Discord Weather Bot are welcome! To contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your changes.
2. Make sure your code adheres to the project's code standards.
3. Submit a pull request to the main repository.

## Contributors
<a href = "https://github.com/Tanu-N-Prabhu/Python/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo = GitHub_username/repository_name"/>
</a>

## License
The project is licensed under the [MIT License](https://github.com/neelshah2409/Bot-Collection/blob/main/LICENSE).
