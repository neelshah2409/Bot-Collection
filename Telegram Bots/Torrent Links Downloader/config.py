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
        chat_id=update.effective_chat.id, text="Welcome to the Torrent Downloader Bot!\n\nAvailable Commands:\n/download <torrent_link> - Download a torrent\n/list - List downloaded torrents\n/pause - Pause ongoing download\n/resume - Resume paused download\n/delete <torrent_number> - Delete a downloaded torrent"
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

# Function to list downloaded torrents
def list_torrents(update, context):
    files = os.listdir(DOWNLOAD_PATH)
    if files:
        file_list = "\n".join(files)
        update.message.reply_text(f"Downloaded Torrents:\n{file_list}")
    else:
        update.message.reply_text("No torrents downloaded.")

# Function to pause ongoing download
def pause_download(update, context):
    # Implement pausing logic using the handle of the active download
    update.message.reply_text("Pausing the download...")

# Function to resume paused download
def resume_download(update, context):
    # Implement resuming logic using the handle of the paused download
    update.message.reply_text("Resuming the download...")

# Function to delete a downloaded torrent
def delete_torrent(update, context):
    # Get the user's message
    message = update.message.text

    # Extract the torrent number
    torrent_number = int(message.split(" ")[1]) - 1

    files = os.listdir(DOWNLOAD_PATH)
    if torrent_number < 0 or torrent_number >= len(files):
        update.message.reply_text("Invalid torrent number.")
    else:
        file_to_delete = files[torrent_number]
        file_path = os.path.join(DOWNLOAD_PATH, file_to_delete)
        os.remove(file_path)
        update.message.reply_text(f"Torrent '{file_to_delete}' deleted successfully.")

# Function to handle any other messages
def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I don't understand that command."
    )

# Main function to run the Telegram bot
def main
