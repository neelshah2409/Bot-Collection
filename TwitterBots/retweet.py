import tweepy
from time import sleep
from keys import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Twitter bot which retweets, likes tweets, and follows users")
print("Bot Configuration:")
print("Like Tweets:", LIKE)
print("Follow users:", FOLLOW)

for tweet in tweepy.Cursor(api.search_tweets, q=QUERY).items():
    try:
        print("\nTweet by: @" + tweet.user.screen_name)

        if LIKE:
            tweet.favorite()
            print("Liked the tweet!")

        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print("Followed the account!")

        tweet.retweet()
        print("Retweeted the tweet!")

        sleep(SLEEP_TIME)

    except tweepy.TwitterError as e:
        print(e.reason)

    except StopIteration:
        break
