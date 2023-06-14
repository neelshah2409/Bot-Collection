import discord
import requests
import json
from weather import *

token = "DISCORD_BOT_TOKEN"
api_key = "OPEN_WEATHER_MAP_API_KEY"
client = discord.Client()
command_prefix = "!w"


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="!w [location]"
        )
    )


@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        if len(message.content.replace(command_prefix, "")) >= 1:
            location = message.content.replace(command_prefix, "").lower()
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"
            try:
                data = parse_data(json.loads(requests.get(url).content)["main"])
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))


print("Bot has started running")
client.run(token)
