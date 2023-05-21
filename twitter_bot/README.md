# Telegram Twitter Bot

This is a Telegram bot that allows you to access your Twitter account and perform various actions using the Pyrogram library.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/telegram-twitter-bot.git
```
2. Navigate to the project directory:
  ```
  cd telegram-twitter-bot
  ```
3. Install the required dependencies using pip:
  ```
  pip install -r requirements.txt
  ```

## Configuration
1. Create a new Twitter application by following the Twitter Developer Documentation.
2. Obtain your Twitter API credentials: consumer key, consumer secret, access token, and access token secret.
3. Open the config.py file and update the following lines with your Twitter API credentials:

```python
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
api_id = "your api id get it from https://my.telegram.org/apps"
api_hash = "your api hash get it from https://my.telegram.org/apps"
```
Note: Make sure to use Twitter API v2 credentials for proper functionality.

## Usage
1. Run the Python script:
   ```
   python bot.py
   ```
2. Start a conversation with your Telegram bot.
3. Use the provided commands to interact with your Twitter account:
   /timeline - View your Twitter timeline.
   /tweet <text> - Post a new tweet.
   /like <tweet_id> - Like a tweet by its ID.
