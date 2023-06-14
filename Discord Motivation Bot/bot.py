import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("Bot is ready.")


@client.command()
async def motivate(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = response.json()
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    await ctx.send(quote)


client.run("your_token_here")
