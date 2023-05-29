from bs4 import BeautifulSoup as bs
import telebot
import time
from book import book_get

# BOT HEADERS............

# Authorize bot using bot token
bot = telebot.TeleBot("YOUR_TOKEN_HERE")
# setting the number of results to send to the user
results = 5
# setting the default number of books to scrape
mainres = 25

# ////////////////
# BOT COMMANDS............\\\

# start command
@bot.message_handler(commands=["start"])
def starting(message):
    # sends the message to the user when the user starts the bot
    text = f"📚🤖 Welcome to the Book Bot!\n\nI'm here to assist you in downloading books of your choice. Just follow our simple syntax:\n\nTo search for a book 📖, type:\n /book <book name>\nFor example:\n/book abc\n\nSend /help to get assistance. 🙌"
    bot.reply_to(message, text)


# help command
@bot.message_handler(commands=["help"])
def help(message):
    # sends the message to the user when thee user seeks help
    text = f"📚🤖 Book Bot Help\n\nHere are the available commands:\n\n/book <book_name> - Search for a book 📖 and get the download link.\n\nFeel free to explore and find your favorite books! Happy reading! 📚😊"
    bot.reply_to(message, text)


# book command
@bot.message_handler(commands=["book"])
def books_get(message):
    # getting id of the user
    id = message.from_user.id
    # getting name of the book entered
    given_name = message.text[6:]
    # please wait message
    messageId = bot.reply_to(
        message,
        "⌛️📚 Please wait... Fetching book\n\nJust a moment while I fetch the book for you. Sit tight! 😊",
    ).message_id
    chatId = message.chat.id
    # getting books scraped from the internet as a list stored in data
    data = book_get(given_name, mainres, results)
    if data == "Error: emoji":
        # send message to user if there is an emoji in the name of the book
        bot.delete_message(chatId, messageId)
        bot.reply_to(
            message,
            "⚠️ Error: Emojis Detected ⚠️\n\n🚫 We apologize, but the usage of emojis is not supported. Please refrain from using emojis in your commands or queries. 😊\n\nIf you need any assistance with searching and downloading books, feel free to ask without including any emojis. Send /help to learn more about the available commands.\n\nThank you for understanding! 🙏",
        )
    elif data == "Error: no results found":
        # sends the message to the user if there are no books found
        bot.delete_message(chatId, messageId)
        bot.reply_to(
            message,
            "⚠️📚 Error: No Results Found\n\nUnfortunately, no results were found for the book you requested. Please try searching for another book. 📖\n\nKeep exploring, and I hope you find what you're looking for! 🌟",
        )
    elif data == "Error: enter name":
        # sends the message to the user if no book name entered
        bot.delete_message(chatId, messageId)
        bot.reply_to(
            message,
            "⚠️📚 Error: Name Not Entered\n\nPlease provide the name of the book you are looking for.\n\nTo search for a book, use the following syntax:\n📖 /book <book name>\n\nFor example:\n/book abc\n\nFeel free to ask for assistance if you need further help. 🙌",
        )
    elif data == "Error: Title Too Short":
        # sends message to the user if the name of the books is too short
        bot.delete_message(chatId, messageId)
        bot.reply_to(
            message,
            "⚠️❌ Error: Title Too Short\n\nPlease provide the full title of the book to get better results.\n\nFor optimal book searching, use the following format:\n📚 /book <book name>\n\nIf you need any assistance, feel free to ask! 🤖🔍",
        )
    else:
        counter = 0
        bot.delete_message(chatId, messageId)
        # iterate through the data of books
        for i in data:
            # for each book
            if counter <= results:
                dn = f"[DOWNLOAD NOW]({i[5]})"
                caption_all = f"*Name* : {i[0]}\n*Author* : {i[1]}\n*Size* : {i[3]}\n*Format* : {i[4]}\n{dn}"
                # sends the message to user with the book
                bot.send_photo(id, i[6], caption=caption_all, parse_mode="Markdown")
                counter += 1


# running the bot and handling errors
while True:
    try:
        bot.polling(non_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(5)
        continue


# ////////////////
