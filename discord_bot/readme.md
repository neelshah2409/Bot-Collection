# Music Bot 🎧

A Discord Music Bot Written in Python by [Aritra Belel](belelaritra)

## Access Token :

To get the access token, go to the [Bot List](https://discordapp.com/developers/applications/me) and click on the **Create Bot** button.
Then click on the **OAuth2** tab and click on the **Generate Bot** button.
Then copy the **Bot Token** and paste it in `Line No 307` of the `main.py` in the place of `YOUR_TOKEN_HERE`

## Installation

In Terminal Run this Command :

```
pip install -r requirements.txt
```

Downloads:

- Download [ffmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)

## Bot commands

The bot can be called into action using `-` which also provides a list of commands:

| Shortcut Command | Command                      | Description                       |
| ---------------- | ---------------------------- | --------------------------------- |
|                  | `-help`                      | Default Help Command              |
| `-h`             | `-command`                   | Gives All Command Lists of EDM    |
| `-j`             | `-join`                      | Connects Voice Channel            |
| `-l`             | `-leave`                     | Leaves the Voice Channel          |
| `-p`             | `-play` `<song name or url>` | Plays a Song from Youtube         |
| `-pa`            | `-pause`                     | Pauses Current song               |
| `-re`            | `-resume`                    | Resume the paused song            |
| `-st`            | `-stop`                      | Stops the song + Clears the Queue |
| `sk`             | `-skip`                      | Skips the song                    |
| `-cur`           | `-current`                   | Gives the current playing song    |
