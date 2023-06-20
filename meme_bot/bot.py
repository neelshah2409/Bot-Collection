from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch token from environment variable
token_key = os.environ["BOT_TOKEN"]


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hey Yo!!! Imma give you some memez!")


def get_help(update: Update, context: CallbackContext):
    help_message = """
    /start -> Welcome message
    /help -> Show available commands
    /meme -> Get a random meme
    """
    update.message.reply_text(help_message)


def handle_message(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, I did not understand that command. Type \"/help\" to see all possible commands.")


def get_meme(update: Update, context: CallbackContext):
    API_ENDPOINT = "https://meme-api.herokuapp.com/gimme"

    response = requests.get(url=API_ENDPOINT)

    if response.status_code == 200:
        json_data = response.json()
        meme_title = json_data["title"]
        meme_url = json_data["url"]

        context.bot.send_photo(chat_id=update.effective_chat.id, photo=meme_url, caption=f"Title: {meme_title}")
    else:
        update.message.reply_text("Error: Something went wrong.")


def main():
    updater = Updater(token=token_key, use_context=True)
    dispatcher = updater.dispatcher

    # Command Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", get_help))
    dispatcher.add_handler(CommandHandler("meme", get_meme))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
    '''
Changes made in the code:

Added type hints to function arguments for better code readability.
Imported the necessary classes (Update, ParseMode) from the telegram module.
Utilized the CallbackContext in the function signatures to adhere to the latest python-telegram-bot library conventions.
Modified the help message formatting for better readability.
Modified the error message to be more descriptive.
Created a main function to start the bot.
Improved the MessageHandler filter to exclude commands from being handled as regular text.
Remember to replace "BOT_TOKEN" with your actual bot token before running the code.
'''





Regenerate response