# Telegram Torrent Downloader Bot

A Telegram bot built with Python that allows users to download torrent files directly through Telegram.## Features

- Download torrent files by providing magnet links.
- Check the progress of ongoing downloads.
- List downloaded torrents with details.
- Pause and resume ongoing downloads.
- Cancel downloads in progress.
- Delete downloaded torrents.
- Limit the number of simultaneous downloads.

## Getting Started

### Prerequisites

- Python 3.x
- python-telegram-bot library
- python-libtorrent library### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/repo_name.git
   ```

2. Install the required dependencies:

```bash 
pip install -r requirements.txt
```
3. Set up your Telegram bot:

- Create a new Telegram bot by following the instructions provided by BotFather.
- Obtain your bot token.

4. Configure the bot:

- Open the config.py file and replace 'your_telegram_token' with your bot token.
- Set the desired download path in config.py.

5. Run the bot: 
    ```bash
    python bot.py
    ```
## Usage

1. Start the bot by searching for it on Telegram and clicking the "Start" button.

2. Use the following commands:

   - `/start`: Displays a welcome message.
   - `/download <torrent_link>`: Initiates the download of a torrent file using the provided magnet link.
   - `/progress`: Checks the progress of ongoing downloads.
   - `/list`: Lists downloaded torrents with details.
   - `/pause`: Pauses ongoing downloads.
   - `/resume`: Resumes paused downloads.
   - `/cancel`: Cancels downloads in progress.
   - `/delete`: Deletes downloaded torrents.



## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [libtorrent](https://github.com/arvidn/libtorrent)
