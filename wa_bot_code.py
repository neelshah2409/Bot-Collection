## google wa bot from gfg.
## link 'https://www.geeksforgeeks.org/building-whatsapp-bot-on-python/'
## using google library from gfg for google search
## link 'https://www.geeksforgeeks.org/performing-google-search-using-python-code/'
## uses twilio free trial whatsapp api
## uses ngrok to host commands on public server to connect with twilio
## uses python 3.9 or above
## pip3 install twilio flask request

from flask import Flask
from googlesearch import search
from flask import request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route("/", methods=["POST"])

# chatbot logic
def bot():

    # user input
    user_msg = request.values.get("Body", "").lower()

    # creating object of MessagingResponse
    response = MessagingResponse()

    # User Query
    q = user_msg + "geeksforgeeks.org"

    # list to store urls
    result = []

    # searching and storing urls
    for i in search(q, tld="co.in", num=1, stop=6, pause=2):
        result.append(i)

    # displaying result
    msg = response.message(f"--- Result for '{user_msg}' are ---")

    msg = response.message(result[0])
    msg = response.message(result[1])
    msg = response.message(result[2])
    msg = response.message(result[3])
    msg = response.message(result[4])

    return str(response)


if __name__ == "__main__":
    app.run()
