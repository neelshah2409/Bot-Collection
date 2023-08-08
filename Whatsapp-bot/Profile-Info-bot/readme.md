# WhatsApp Web Get-Profile-Information Bot

Automate the process of retrieving profile information of an individual on WhatsApp using this Python script. This script utilizes the Selenium library to interact with WhatsApp Web and extract user information.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the provided code:

    ```bash
    git clone https://github.com/neelshah2409/Bot-Collection.git
    ```

3. Navigate to the project directory:

    ```bash
    cd Whatsapp-bot/Profile-Info-bot
    ```
4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
5. Download the [ChromeDriver](https://chromedriver.chromium.org/downloads) suitable for your Chrome version and place it in the project directory.

## Usage

1. Make sure you have a compatible version of Chrome installed on your system.
2. Run the script:

    ```bash
    python Whatsapp.py
    ```
3. A Chrome browser window will open, displaying WhatsApp Web.
4. Scan the QR code using your phone to log in to WhatsApp Web.
5. Upon successful login, the script will wait for 60 seconds to load the page.
6. When prompted, provide the name of the individual whose profile information you want to retrieve.
7. The script will print the retrieved information on the terminal.

## Notes

- This script uses the Chrome WebDriver for Selenium automation. Ensure that the `chromedriver` executable matches your Chrome browser version and is located in the project directory.
- The script waits for 60 seconds to ensure proper loading of the WhatsApp Web page before interaction. You can modify this delay if necessary.

## Contributor

- [Juhi Bhojani](https://github.com/Juhibhojani)
