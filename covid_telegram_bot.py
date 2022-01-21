from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import requests


# A simple telegram bot that provides users with up-to-date COVID-19 statistics

token_key =  # Token to access Telegram HTTP API can be retreived from FatherBot upon creation of the bot



def start(update, context):
    update.message.reply_text('Hello! This bot will provide real time COVID-19 stats!')

def help(update,context):
    update.message.reply_text("""
    /start -> Welcome message
    /help -> This message; shows avialable messages
    /stats -> displays COVID-19 stats
    
    """

    )
def handle_message(update, context):
    update.message.reply_text("Sorry, I did not understand that command. Type \" \help \" to see all possible commands")

def stats(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code== 200):
        data = response.json()
        date = data['Date'][:10]
        stats = f"Covid 19 Summary (as of {date}): "
        
        for x, y in data['Global'].items():
            if x not in ['NewConfirmed', 'NewDeaths', 'NewRecovered']:
                stats += "\n" + 'Total ' + x[5::].lower() + " : " + str(y) 
        
        print(stats)
        context.bot.send_message(chat_id=update.effective_chat.id, text=stats)
        update.message.reply_text(stats)
    else:
        update.message.reply_text("Error, something went wrong.")


updater = Updater(token= token_key, use_context=True) 
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.text), handle_message)
dispatcher.add_handler(CommandHandler('stats', stats))

updater.start_polling()
updater.idle()