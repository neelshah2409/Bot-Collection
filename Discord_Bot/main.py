import os
import re
import json
import nacl
import asyncio
import discord
import youtube_dl
import validators
from queue import Queue
from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube_search import YoutubeSearch

client = commands.Bot(command_prefix="-")
songlist = Queue(maxsize=10)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    activity = discord.Activity(type=discord.ActivityType.playing, name="-commands")
    await client.change_presence(status=discord.Status.online, activity=activity)


@client.command(aliases=["j"])
async def join(ctx):
    if not ctx.author.voice:
        return await ctx.send("You are not in a voice channel.")
    channel = ctx.message.author.voice.channel
    voice = ctx.voice_client
    if voice and voice.is_connected():
        await voice.move_to(channel)
        embedVar = discord.Embed(
            title=f"Moved to {channel}",
            description="To Leave Voice Channel Enter : -l",
            color=0xFFFB00,
        )
        await ctx.channel.send(embed=embedVar)
    else:
        voice = await channel.connect()
        embedVar = discord.Embed(
            title=f"Connected to {channel}",
            description="To Leave Voice Channel Enter : -l",
            color=0xFFFB00,
        )
        await ctx.channel.send(embed=embedVar)


@client.command(aliases=["l"])
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if (
        ctx.author.voice.channel
        and ctx.author.voice.channel == ctx.voice_client.channel
    ):
        await ctx.voice_client.disconnect()
        channel = ctx.message.author.voice.channel
        embedVar = discord.Embed(
            title=f"Disconnected to {channel}",
            description="To Join Voice Channel Enter : -j",
            color=0xFFFB00,
        )
        await ctx.channel.send(embed=embedVar)
    else:
        embedVar = discord.Embed(
            title="You have to be connected to the same voice channel to disconnect me.",
            description="To Join Voice Channel Enter : -j",
            color=0xFFFB00,
        )
        await ctx.channel.send(embed=embedVar)


# Play
def playmusic(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        return

    if voice.is_playing() == False and songlist.empty() == False:
        url = songlist.get()
        global previous
        previous = str(url)
        # Quality
        ydl_opts = {
            "format": "beataudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        ytdl = youtube_dl.YoutubeDL(ydl_opts)
        info = ytdl.extract_info(url, download=False)
        asrc = discord.FFmpegOpusAudio(
            info["formats"][0]["url"],
            before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        )
        voice.play(asrc, after=lambda e: playmusic(ctx))


@client.command(aliases=["p"])
async def play(ctx, *, search: str):
    valid = validators.url(search)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # If Valid URL
    if valid == True:
        url = search
        # Json
        yt = YoutubeSearch(url, max_results=1).to_json()
        yt_id = str(json.loads(yt)["videos"][0]["id"])
    # If Song Name (Invalid URL)
    else:
        newsearch = search.replace(" ", "")
        # Json
        yt = YoutubeSearch(newsearch, max_results=1).to_json()
        yt_id = str(json.loads(yt)["videos"][0]["id"])
        # Creating URL
        url = "https://www.youtube.com/watch?v=" + yt_id

    # Getting Details From JSON
    title = json.loads(yt)["videos"][0]["title"]
    duration = json.loads(yt)["videos"][0]["duration"]
    channel = json.loads(yt)["videos"][0]["channel"]

    # Quality
    ydl_opts = {
        "format": "beataudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    # If Already Playing
    if songlist.full() == True:
        await ctx.send("Already 10 Songs are in Queue")
        embedVar = discord.Embed(
            title=title, description="Already 10 Songs are in Queue", color=0xF00000
        )
        embedVar.set_thumbnail(url=json.loads(yt)["videos"][0]["thumbnails"][0])
        embedVar.add_field(name="Url", value=url, inline=False)
        # embedVar.add_field(
        #     name="Channel", value=" ".join(re.findall("[A-Z][a-z]*", channel)), inline=False
        # )
        #     embedVar.add_field(name="Song Duration", value=duration, inline=False)
        await ctx.channel.send(embed=embedVar)
    elif voice.is_playing():
        songlist.put(url)
        # await ctx.send("Added to Queue")
        embedVar = discord.Embed(
            title=title, description="Added to Queue", color=0xE49625
        )
        embedVar.set_thumbnail(url=json.loads(yt)["videos"][0]["thumbnails"][0])
        embedVar.add_field(name="Url", value=url, inline=False)
        embedVar.add_field(
            name="Channel",
            value=" ".join(re.findall("[A-Z][a-z]*", channel)),
            inline=False,
        )
        embedVar.add_field(name="Song Duration", value=duration, inline=False)
        await ctx.channel.send(embed=embedVar)
    elif songlist.empty() == False:
        songlist.put(url)
        await ctx.send("Added to Queue")
        embedVar = discord.Embed(
            title=title, description="Added to Queue", color=0x0FFFFF
        )
        embedVar.add_field(name="Url", value=url, inline=False)
        embedVar.set_thumbnail(url=json.loads(yt)["videos"][0]["thumbnails"][0])
        embedVar.add_field(
            name="Channel",
            value=" ".join(re.findall("[A-Z][a-z]*", channel)),
            inline=False,
        )
        embedVar.add_field(name="Song Duration", value=duration, inline=False)
        await ctx.channel.send(embed=embedVar)
    elif songlist.empty() == True:
        songlist.put(url)
        embedVar = discord.Embed(title=title, description=url, color=0x00FF00)
        embedVar.set_thumbnail(url=json.loads(yt)["videos"][0]["thumbnails"][0])
        embedVar.add_field(
            name="Channel",
            value=" ".join(re.findall("[A-Z][a-z]*", channel)),
            inline=False,
        )
        embedVar.add_field(name="Song Duration", value=duration, inline=False)
        await ctx.channel.send(embed=embedVar)
    playmusic(ctx)


@client.command(aliases=["sk", "next"])
async def skip(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    playmusic(ctx)

    embedVar = discord.Embed(
        title="Music Skipped",
        description="To Add In Queue Enter : -p _<url>_\n",
        color=0xFFFB00,
    )
    await ctx.channel.send(embed=embedVar)


@client.command(aliases=["st"])
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    embedVar = discord.Embed(
        title="Music Stopped + Queue Cleared",
        description="To Play Music Enter : -p _<url>_\n",
        color=0xFFFB00,
    )
    await ctx.channel.send(embed=embedVar)
    while songlist.empty != True:
        temp = songlist.get()
    return


@client.command(aliases=["pa"])
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        embedVar = discord.Embed(
            title="Music Paused",
            description="To Resume Enter : -re\n",
            color=0xFFFB00,
        )
        await ctx.channel.send(embed=embedVar)

    else:
        embedVar = discord.Embed(
            title="Currently No Audio Is Playing.",
            description="To Play Music Enter : -p _<url>_\n",
            color=0xFFFB00,
        )
        await ctx.channel.send(embed=embedVar)


@client.command(aliases=["re"])
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        embedVar = discord.Embed(
            title="Music Resumed",
            description="To Pause Enter : -pa\n",
            color=0xFFFB00,
        )
        await ctx.channel.send(embed=embedVar)
    else:
        embedVar = discord.Embed(
            title="Currently No Audio Is Paused.",
            description="To Play Music Enter : -p _<url>_\n",
            color=0xFFFB00,
        )
        await ctx.channel.send(embed=embedVar)


@client.command(aliases=["c", "cur", "curr", "now"])
async def current(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    url = previous
    yt = YoutubeSearch(url, max_results=1).to_json()
    yt_id = str(json.loads(yt)["videos"][0]["id"])
    title = json.loads(yt)["videos"][0]["title"]
    duration = json.loads(yt)["videos"][0]["duration"]
    embedVar = discord.Embed(title="Now Playing", description=title, color=0x0083FF)
    embedVar.add_field(name="Song Duration", value=duration, inline=False)
    embedVar.set_thumbnail(url=json.loads(yt)["videos"][0]["thumbnails"][0])
    await ctx.channel.send(embed=embedVar)


@client.command(aliases=["command", "com", "h"])
async def commands(ctx):
    embedVar = discord.Embed(
        title="Music Bot Command Lists :",
        description="Built by: https://github.com/belelaritra\n",
        color=0xFFFB00,
    )
    embedVar.add_field(
        name="-join || -j", value="Connnects Voice Channel", inline=False
    )
    embedVar.add_field(
        name="-play _<url or song name>_ || -p _<url or song name>_ ",
        value="Plays a Song",
        inline=False,
    )
    embedVar.add_field(name="-pause || -pa", value="Pauses Current Song", inline=False)
    embedVar.add_field(
        name="-resume || -re", value="Resumes a Paused Song", inline=False
    )
    embedVar.add_field(name="-skip || -sk", value="Skips Current Song", inline=False)
    embedVar.add_field(name="-stop || -st", value="Stops Current Song", inline=False)
    embedVar.add_field(name="-current || -c", value="Current Song", inline=False)
    embedVar.add_field(
        name="-leave || -l", value="To Leave Voice Channel", inline=False
    )
    await ctx.channel.send(embed=embedVar)


client.run(os.environ["YOUR_TOKEN_HERE"])
