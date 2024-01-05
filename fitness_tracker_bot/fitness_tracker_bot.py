from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


TELEGRAM_TOKEN = 'YourTelegramBotToken'


user_workouts = {}


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to Fitness Tracker Bot! Use /log to log your workouts.")
def log_workout(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_workouts:
        user_workouts[user_id] = []

    workout = update.message.text.replace('/log', '').strip()
    user_workouts[user_id].append(workout)

    update.message.reply_text(f"Workout logged: {workout}")


def view_workouts(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    workouts = user_workouts.get(user_id, [])

    if workouts:
        message = "Your logged workouts:\n" + "\n".join(workouts)
    else:
        message = "No workouts logged yet."

    update.message.reply_text(message)


def handle_text(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I'm a fitness tracker bot. Use /log to log your workouts.")

def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("log", log_workout))
    dp.add_handler(CommandHandler("view", view_workouts))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()