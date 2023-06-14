from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import os

# load token in env
from dotenv import load_dotenv

load_dotenv()

# fetch token from env
token_key = os.environ["BOT_TOKEN"]


def start(update, context):
    update.message.reply_text("Hello! This bot will provide real time COVID-19 stats!")


def get_help(update, context):
    update.message.reply_text(
        """
    /start -> Welcome message
    /help -> This message; shows avialable messages
    /stats -> displays COVID-19 global stats
    /stats [country] -> displays COVID-19 stats for a specific country
    
    """
    )


def handle_message(update, context):
    update.message.reply_text(
        'Sorry, I did not understand that command. Type " /help " to see all possible commands'
    )


def stats(update, context):
    response = requests.get("https://api.covid19api.com/summary")

    if response.status_code == 200:
        data = response.json()
        date = data["Date"][:10]
        stats = f"Covid 19 Summary (as of {date}): "
        blacklist = ["ID", "Slug", "CountryCode", "Date", "Premium"]

        command = update.message.text.strip()

        if command == "/stats":
            for x, y in data["Global"].items():
                if x not in blacklist:
                    stats += "\n" + x + " : " + str(y)

            update.message.reply_text(stats)
        else:
            country = command.split(" ")[1].lower()
            found = 0
            # print(country)

            for country_data in data["Countries"]:
                if country_data["Slug"] == country.lower():
                    for x, y in country_data.items():
                        if x not in blacklist:
                            stats += "\n" + x + " : " + str(y)
                    found = 1
                    break

            if found:
                update.message.reply_text(stats)
            else:
                update.message.reply_text(
                    "Error, Country not found! Check the spelling or try full name."
                )

        # print(stats)
    else:
        update.message.reply_text("Error, something went wrong.")


if __name__ == "__main__":

    updater = Updater(token=token_key, use_context=True)
    dispatcher = updater.dispatcher

    # Command Lists
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", get_help))
    dispatcher.add_handler(CommandHandler("stats", stats))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()
