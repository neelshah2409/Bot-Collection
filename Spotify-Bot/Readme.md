# Spotify Bot to Find Similar Songs
- This is a spotify bot which can suggest songs mathcing a users taste.
- The user can search for a song he likes, the bot then sends relevant information about that song and asks for the category in which the user wants to search for similar songs.
- The bot currently uses a naive method of finding similar songs, this can be changed to use Spotify's own recommendations API or improved further.

## Requirements and Running the Project
- The project is written in python.
- Recommended to use Python 3.8 or above
- The required libraries can be installed by running:
```bash
pip install discord
pip install spotipy
pip install dotenv
```
- After installing the libraries, developers should set up a `.env` file in the project root with the following:
```
TOKEN=YOUR_DISCORD_BOT_TOKEN
SPOTIPY_CLIENT_ID=YOUR_SPOTIFY_APP_CLIENT_ID
SPOTIPY_CLIENT_SECRET=YOUR_SPOTIFY_CLIENT_SECRET
```
- Before running the bot, make sure you have created a bot on the discord developer portal and set up an application on Spotify's developer portal (This is where you will get the env variables).
- You can now run the `bot.py` file by running the following command in the project root:
```bash
python3 bot.py
```

## Commands
| Command | Description |
|---------|-------------|
| `!=ping` | Fetches the bot's latency. |
| `!=how` | Fetches the usage instructions for the bot. |
| `!=hello` | Returns a greeting from the bot. |
| `!=song <song_name>` | Will search for details of `song_name`, like artist, album, popularity, etc. |
| `!=category <category_name>` | Selects the category/playlist to search for similar songs in. See `!=how` for more details. |
| `!=suggest <num_to_suggest>` | Tries to find upto `num_to_suggest` songs matching a song specified by the user earlier through `!=song <song_name>`. |


## Author

- [@Vidhish-Trivedi](https://github.com/Vidhish-Trivedi)
