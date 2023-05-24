# Whatsapp Image Bot

This is a Flask-based application that generates an image based on the incoming message received via Twilio's WhatsApp API. The generated image contains the text sent by the user. The image is then sent back to the user as a response.

## Prerequisites

- Python 3.7 or higher
- Twilio account credentials (account SID and auth token)
- Twilio phone number with WhatsApp capabilities
- Roboto-Bold.ttf font file (should be placed in the same directory as the script)

## Installation

1. Clone the repository or download the code files.

2. Install the required Python packages by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Open the `image-bot.py` file in a text editor.

2. Replace the placeholder values with your Twilio account credentials:

    ```bash
    client = Client("<YOUR_ACCOUNT_SID>", "<YOUR_AUTH_TOKEN>")
    ```

3. Replace the `FROM_PHONE_NUMBER` placeholder with your Twilio phone number:

    ```bash
    from_ = 'whatsapp:<FROM_PHONE_NUMBER>'
    ```

## Usage

1. Run the Flask application by executing the following command:

    ```bash
    python image-bot.py
    ```

2. The application will start running locally on `http://localhost:5000`.

3. In your Twilio account, configure the incoming webhook for your WhatsApp number to point to `http://localhost:5000/bot`.

4. Send a WhatsApp message to your Twilio phone number, and the bot will generate an image based on the message and send it back as a response.


Note: Make sure you have an internet connection and the required font file (`Roboto-Bold.ttf`) in the same directory as the script.





