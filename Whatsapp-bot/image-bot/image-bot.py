# import the necessary modules
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# create an instance of the Flask class
app = Flask(__name__)

# create an instance of the Client class
client = Client()

# create a function that will generate the image
def generate_image(text):
    # create an instance of the Image class
    image = Image.new("RGB", (500, 500), color=(73, 109, 137))

    # create an instance of the Draw class
    draw = ImageDraw.Draw(image)

    # create an instance of the ImageFont class
    font = ImageFont.truetype("Roboto-Bold.ttf", size=20)

    # wrap the text to fit the image
    text = textwrap.wrap(text, width=20)

    # create a variable to store the y position of the text
    y_text = 10

    # loop through the text
    for line in text:
        # draw the text on the image
        draw.text((10, y_text), line, font=font, fill=(255, 255, 0))

        # increment the y position of the text
        y_text += 20

    # save the image
    image.save("image.png")


# create a function that will send the image to the user
def send_image(number):
    # get the path to the image
    image_path = os.path.abspath("image.png")

    # send the image to the user
    client.messages.create(
        from_="whatsapp:+14155238886",
        to=number,
        media_url="https://demo.twilio.com/owl.png",
    )


# create a function that will handle the incoming messages
@app.route("/bot", methods=["POST"])
def bot():
    # get the message from the user
    incoming_message = request.values.get("Body", "").lower()

    # create an instance of the MessagingResponse class
    response = MessagingResponse()

    # check if the user has sent a message
    if incoming_message != "":
        # generate the image
        generate_image(incoming_message)

        # send the image to the user
        send_image(request.values.get("From", ""))

    # return the response
    return str(response)


# create a function that will handle the incoming calls
@app.route("/bot", methods=["GET"])
def bot_call():
    # create an instance of the MessagingResponse class
    response = MessagingResponse()

    # return the response
    return str(response)


# run the app
if __name__ == "__main__":
    app.run(debug=True)
