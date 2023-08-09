import telegram
from telegram.ext import Updater, CommandHandler
import instaloader

# Create an Instaloader instance
L = instaloader.Instaloader()
BOT_TOKEN=your_bot_token
# Define the function to handle the /profile command
def profile(update, context):
    # Get the username from the user's message
    username = context.args[0]

    # Load the profile of the user
    profile = instaloader.Profile.from_username(L.context, username)

    # Get the profile details
    followers = profile.followers
    following = profile.followees
    posts = profile.mediacount
    bio = profile.biography
    name = profile.full_name

    # Create the message to send back to the user
    message = f"Name: {name}\nBio: {bio}\nFollowers: {followers}\nFollowing: {following}\nPosts: {posts}"

    # Send the message back to the user
    update.message.reply_text(message)


updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Set up the handler for the /profile command
dispatcher.add_handler(CommandHandler("profile", profile))

# Start the bot
updater.start_polling()