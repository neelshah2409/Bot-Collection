import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import libtorrent as lt

# Telegram bot token (replace with your own token)
TOKEN = "your_telegram_token"

# Path to the directory where downloaded torrents will be saved
DOWNLOAD_PATH = "path_to_download_directory"

# Initialize the Telegram bot
bot = telegram.Bot(token=TOKEN)

# Function to handle the '/start' command
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Welcome to the Torrent Downloader Bot!"
    )


# Function to handle torrent download command
def download_torrent(update, context):
    # Get the user's message
    message = update.message.text

    # Extract the torrent link
    torrent_link = message.split(" ")[1]

    # Create a session for torrent downloading
    ses = lt.session()

    # Set download directory
    ses.set_download_settings({"save_path": DOWNLOAD_PATH})

    # Add the torrent to the session
    handle = lt.add_magnet_uri(ses, torrent_link)

    # Start downloading the torrent
    ses.start_dht()
    ses.start_lsd()
    ses.start_upnp()
    ses.start_natpmp()

    # Check if the torrent has been successfully added
    if handle.is_valid():
        # Set download location for the torrent
        handle.set_download_mode(lt.torrent_handle.download_mode_t(1))

        # Download the torrent
        while not handle.is_seed():
            update.message.reply_text("Downloading the torrent...")
            lt.sleep(1)

        update.message.reply_text("Torrent downloaded successfully!")
    else:
        update.message.reply_text("Invalid torrent link.")


# Function to handle any other messages
def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I don't understand that command."
    )


# Main function to run the Telegram bot
def main():
    # Create an instance of the Updater class
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download_torrent))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl+C is pressed
    updater.idle()


if __name__ == "__main__":
    main()
