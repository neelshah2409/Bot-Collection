from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import os

# load token in env
from dotenv import load_dotenv

load_dotenv()

# fetch token from env
token_key = os.environ["BOT_TOKEN"]


def start(update, context):
    update.message.reply_text("Hey Yo!!! Imma gib u some memez!")


def get_help(update, context):
    update.message.reply_text(
        """

    /start -> Welcome message
    /help -> This message; shows avialable messages
    /meme -> throws some random meme

    """
    )


def handle_message(update, context):
    update.message.reply_text(
        """
        Sorry, I did not understand that command.
        Type \" /help \" to see all possible commands"""
    )


def get_meme(update, context):
    API_ENDPOINT = "https://meme-api.herokuapp.com/gimme"

    response = requests.get(url=API_ENDPOINT)

    if response.status_code == 200:
        json_data = response.json()
        meme_title = json_data["title"]
        meme_url = json_data["url"]

        context.bot.send_photo(chat_id=update.effective_chat.id, photo=meme_url)
        update.message.reply_text("Title : " + meme_title)
    else:
        update.message.reply_text("Error, something went wrong.")


if __name__ == "__main__":

    updater = Updater(token=token_key, use_context=True)
    dispatcher = updater.dispatcher

    # Command Lists
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", get_help))
    dispatcher.add_handler(CommandHandler("meme", get_meme))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()
