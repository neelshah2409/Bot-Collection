import tweepy
from pyrogram import Client, filters
from pyrogram.types import Message
from config import (
    bot_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    api_hash,
    api_id,
)

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# Authenticate with Telegram bot

telegram_bot = Client(bot_token, api_id=api_id, api_hash=api_hash)


# Define Telegram bot commands
@telegram_bot.on_message(filters.command("tweet"))
def tweet_command(client: Client, message: Message):
    # Extract the tweet message from the command
    tweet_message = " ".join(message.command[1:])

    # Post the tweet on Twitter
    twitter_api.update_status(tweet_message)
    message.reply("Tweet posted successfully!")


@telegram_bot.on_message(filters.command("timeline"))
def timeline_command(client: Client, message: Message):
    # Fetch the user's timeline from Twitter
    timeline = twitter_api.home_timeline(count=5)  # Fetch the 5 most recent tweets

    # Send the timeline as a message to Telegram
    timeline_text = "Recent tweets from your timeline:\n\n"
    for tweet in timeline:
        timeline_text += f"- {tweet.text}\n\n"
    message.reply(timeline_text)


@telegram_bot.on_message(filters.command("like"))
def like_command(client: Client, message: Message):
    # Extract the tweet ID from the command
    tweet_id = message.command[1]

    # Like the tweet on Twitter
    try:
        twitter_api.create_favorite(tweet_id)
        message.reply("Tweet liked successfully!")
    except tweepy.TweepError as e:
        error_message = str(e.reason) if hasattr(e, "reason") else str(e)
        message.reply(f"Failed to like the tweet: {error_message}")


# Start the Telegram bot
telegram_bot.run()
