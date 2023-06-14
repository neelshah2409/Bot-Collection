import discord

color = 0x0099FF
key_features = {
    "temp": "Temperature",
    "feels_like": "Feels Like",
    "temp_min": "Minimum Temperature",
    "temp_max": "Maximum Temperature",
}


def parse_data(data):
    del data["humidity"]
    del data["pressure"]
    return data


def weather_message(data, location):
    location = location.title()
    message = discord.Embed(title=f"Weather in {location}", color=color)
    for key in data:
        message.add_field(name=key_features[key], value=str(data[key]), inline=False)
    return message


def error_message(location):
    location = location.title()
    return discord.Embed(
        title="Error",
        description=f"There was an error retrieving weather data for {location}",
        color=color,
    )
