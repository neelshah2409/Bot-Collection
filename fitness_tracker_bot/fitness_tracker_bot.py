from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


TELEGRAM_TOKEN = 'YourTelegramBotToken'


user_workouts = {}


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to Fitness Tracker Bot! Use /log to log your workouts.")
