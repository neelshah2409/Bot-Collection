from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import time
time.clock = time.time

engine = pp.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Chatbot")
conversation = [
    'hello',
    'Hi!'
    'What is your name?',
    'My name is TheBot, I am created by Disha Modi',
    'How are you',
    'I am fine',
    'Where do you live?',
    'I live in Nadiad',
    'Using which language you are built',
    'I am built using Python',
    'What is your fav book?',
    'My fav book is Rich Dad, Poor Dad'
]

trainer = ListTrainer(bot);
trainer.train(conversation)

main = Tk()

main.geometry("500x650")
main.title("My New ChatBot")
img = PhotoImage(file = "bot.png")
photoL = Label(main,image = img)
photoL.pack(pady=5)


def take_query():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Bot is listening, Try to speak")
    with s.Microphone() as m:
        try :
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            textF.delete(0, END)
            textF.insert(0, query)
            msgs.yview(END)
        except Exception as e:
            print(e)

def ask_from_bot():
    print("Button Clicked")
    query = textF.get()         #Getting value from Text Field
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"You : "+query)
    msgs.insert(END,"Bot : "+str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame,width=80,height=20,yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill = Y)
msgs.pack(side=LEFT,fill = BOTH,pady=10)

frame.pack()

#Creating Text field
textF = Entry(main,font=("Comic Sans",20))
textF.pack(fill=X,pady=10)

btn = Button(main,text="Ask from Bot",font=("Comic Sans",20),command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

#Going to bind main window with event(click on enter key)
main.bind('<Return>',enter_function)

def repeatL():
    while True:
        take_query()


t = threading.Thread(target=repeatL)
t.start()

main.mainloop()
