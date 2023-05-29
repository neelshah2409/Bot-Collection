from flask import Flask, request
from twilio.rest import Client
import requests

TWILIO_ACCOUNT_SID = "ENTER YOUR TWILIO ACCOUNT SID HERE"
TWILIO_AUTH_TOKEN = "ENTER YOUR TWILIO AUTH TOKEN HERE"
API_ENDPOINT = "https://random-word-api.herokuapp.com/word?swear=0&number=1"


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

app = Flask(__name__)


def send_msg(sender_number, reciever_number, message):
    client.messages.create(
        to=reciever_number,
        from_=sender_number,
        body=message,
    )
    return ("", 200)


@app.route("/", methods=["POST"])
def Bot():
    sender_number = request.form["From"]
    reciever_number = request.form["To"]
    msg_body = request.form["Body"]

    print(msg_body)

    if msg_body == "hi":
        response = requests.get(API_ENDPOINT)

        if response.status_code == 200:
            wotd_msg = "📇 Here's your word of the day: *{}*".format(
                response.json().pop()
            )
        else:
            wotd_msg = "Oops! I found nothing you!"

        send_msg(reciever_number, sender_number, wotd_msg)

    else:
        send_msg(reciever_number, sender_number, "Sorry, what did you say?")

    return ("", 200)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
