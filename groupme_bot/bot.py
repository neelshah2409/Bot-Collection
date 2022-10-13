import os
import requests
import datetime
import random

from bs4 import BeautifulSoup
from flask import Flask, request

page = requests.get("https://nutrition.umd.edu/")
soup = BeautifulSoup(page, "html.parser")
app = Flask(__name__)

# homepage of actual URL
@app.route("/", methods=["GET"])
def home():
    return "Where my bot for Montgomery Hall lives :) - Jason, implementing SSL soon"


@app.route("/", methods=["POST"])
def receive():
    print("Incoming message:")
    data = request.get_json()
    print(data)

    # Prevent self-reply
    if data["sender_type"] != "RA BOT":

        # parse the message and act accordingly
        read(data["text"].lower())
        if data["text"].startswith("/ping"):

            send(data["name"] + " pinged me!")

    return "ok", 200


# show all menu-options
def showMenu():
    menuString = "RA BOT MENU: \n"
    menuString += "You can send the bot a command!\n"
    menuString += "Upcoming Events: /events \n"
    menuString += "Is Jason on Duty right now?: /duty? \n"
    menuString += "Pick a num between 1-10: /pick \n"
    menuString += "Flip a coin: /flip \n"
    menuString += "Phone Numbers: /numbers \n"

    return menuString


def events():
    with open("events.txt") as f:
        lines = f.readlines()
        eventString = ""
        # Event1, Hour:Min, 9-20-10
        for i in lines:
            eventString += i

        return eventString


def read(msg):
    text = msg.split(" ")

    if msg == "/menu":
        send(showMenu())
    elif msg == "/events":
        send(events())
    elif msg == "/duty?":
        # pulls data from Google Calendar API
        send("No")
    elif msg == "/pick":
        send(str(random.randint(1, 10)))
    elif msg == "/flip":
        toss = random.randint(1, 2)
        if toss == 1:
            send("tails")
        else:
            send("heads")
    elif msg == "/numbers":
        # numbers() -> not shown for sake of confidentality
        send(numbers)

    return True


def send(msg):
    url = "https://api.groupme.com/v3/bots/post"

    data = {
        "bot_id": os.getenv("GROUPME_BOT_ID"),
        "text": msg,
    }
    # sends message to GroupMe
    r = requests.post(url, json=data)