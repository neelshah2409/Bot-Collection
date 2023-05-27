# **Whatsapp Web Tag-All Bot**

This Python script utilizes the Selenium library to automate the process of tagging all members of a WhatsApp group. It can be used to send a message to all members of a group at once.

## Installation

1. Make sure you have Python installed on your system.
2. Clone this repository or download the provided code.

    ```bash
    git clone https://github.com/neelshah2409/Bot-Collection.git
    ```

3. Navigate to the project directory
    
    ```bash
    cd Whatsapp-bot/Tag-all-bot
    ```
4. Install the required dependencies

    ```bash
    pip install -r requirements.txt
    ```
5. Download the [ChromeDriver](https://chromedriver.chromium.org/downloads) for your version of Chrome and place it in the project directory.

## Usage

1. Make sure you have a compatible version of Chrome installed on your system.
2. Run the script

    ```bash
    python tagall-bot.py
    ```
3.  A Chrome browser window will open with WhatsApp Web.
4.  Scan the QR code with your phone to log in to WhatsApp Web.
5.  After successful login, the script will wait for 10 seconds to load the page.
6.  Provide the name of the group you want to send the message to by modifying the group_name variable in the ```tagall-bot.py``` file.
7.  Run the script again.

## Notes

-   This script uses the Chrome WebDriver for Selenium automation. Make sure the ```chromedriver``` executable is in the project directory and matches your Chrome browser  version.
-   The script waits for 10 seconds to ensure that the WhatsApp Web page loads properly before interacting with it. You can modify this delay as needed.
-   The provided code sends the message "@everyone" to the specified group. Modify the ```message_box.send_keys()``` line in the ```tagall-bot.py``` file to change the message content.

## Contributor

-   [Anurag Anand](https://github.com/anuraganand92)