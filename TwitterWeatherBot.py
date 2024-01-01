import tweepy
import requests
import json

# Twitter API credentials
consumer_key = 'YourTwitterConsumerKey'
consumer_secret = 'YourTwitterConsumerSecret'
access_token = 'YourTwitterAccessToken'
access_token_secret = 'YourTwitterAccessTokenSecret'

# OpenWeatherMap API key
openweathermap_api_key = 'YourOpenWeatherMapApiKey'

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to get weather information
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}'
    response = requests.get(url)
    weather_data = json.loads(response.text)

    if response.status_code == 200:
        return weather_data['weather'][0]['description']
    else:
        return None

# Function to tweet weather information
def tweet_weather(city):
    weather = get_weather(city)

    if weather:
        tweet = f'The weather in {city} is {weather}! ☀️🌧️❄️'
        api.update_status(status=tweet)
        print(f'Tweet posted: {tweet}')
    else:
        print('Failed to retrieve weather information.')

if __name__ == "__main__":
    # Replace 'CityName' with the desired city
    city_name = 'CityName'
    tweet_weather(city_name)
