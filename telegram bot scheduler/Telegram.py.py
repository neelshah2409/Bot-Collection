
import telebot
import sched
import time

# Create a new bot instance
bot = telebot.TeleBot('6142986288:AAH4FgY0ZHx-r4qnWl3vO5JbCRvmrJ2T1W8')

# Handle the '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "enter as /set task name(withoutgap) YYYY-DD-MM HH:MM:SS")

 # Modify this line if necessary
 
@bot.message_handler(commands=['set'])
def handle_message(message):
    o=message.text.split('/set ')[1].split(' ',1)
    j=o[1]
    p=o[0]
    s = sched.scheduler(time.time, time.sleep)
    def your_function():
        bot.reply_to(message,p)
    
    s.enterabs(time.mktime(time.strptime(j, "%Y-%m-%d %H:%M:%S")), 1, your_function)
    s.run()

# Start the bot
bot.polling()

