# Telegram Python Code Execution Bot

This Telegram bot allows you to execute Python code snippets directly within a Telegram group. It provides a convenient way to run Python code and receive the output within the Telegram chat interface.

![Telegram Python Code Execution Bot](https://github.com/anupammaurya6767/Bot-Collection/blob/main/tg_bot/images/main.png)

## Setup Instructions

Follow these steps to set up and run the Telegram Python Code Execution Bot:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

``` git clone <repository_url> ```


### 2. Install Dependencies

Navigate to the root folder of the cloned repository and install the required dependencies using pip:

``` cd <repository_folder> ```

``` pip install -r requirements.txt  ```


### 3. Obtain API Credentials

To use the Telegram Bot API, you need to obtain the API credentials required for authentication. Follow the steps below:

1. Create a Telegram application by visiting the [Telegram API Development Tools](https://my.telegram.org/auth) page.
2. Log in using your Telegram account.
3. Fill in the required information to create a new application.
4. Once your application is created, you will receive an API ID and API hash. Make a note of these, as you will need them in the next step.

### 4. Configure the Bot

Open the `main.py` file in a text editor and locate the following lines:

```python
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"
```

Replace "YOUR_API_ID", "YOUR_API_HASH", and "YOUR_BOT_TOKEN" with the API credentials and bot token obtained in the previous step.

### 5. Run the Bot
Save the main.py file after making the necessary changes. In your terminal, run the following command to start the bot:
```
python3 main.py
```

### 6. Test the Bot
To test the bot, add it to a Telegram group and send the command /eval followed by the Python code you want to execute. For example:

The bot will execute the code and reply with the output within the Telegram chat.

## Screenshots
Here are a few screenshots of the Telegram Python Code Execution Bot in action:

![Telegram Python Code Execution Bot](https://github.com/anupammaurya6767/Bot-Collection/blob/main/tg_bot/images/screen.png)

### Troubleshooting
If you encounter any issues while setting up or running the bot, try the following troubleshooting steps:

Make sure you have correctly provided the API credentials and bot token in the main.py file.
Ensure that you have a stable internet connection.
Double-check that the required dependencies are installed by running pip install -r requirements.txt again.
Verify that you have the necessary permissions to add the bot to a Telegram group and execute commands.
If the issue persists, you can reach out to the developer for further assistance.

### Contributions
Contributions to the Telegram Python Code Execution Bot are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request on the GitHub repository.

### License
This project is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.
