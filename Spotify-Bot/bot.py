# Importing required libraries.
import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# Loading environment variables.
load_dotenv()
TOKEN = os.getenv('TOKEN')
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

# Creating a Spotify object and authenticating client.
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

# Setting defaults.
song_name = None
search_in = None
num_to_suggest = None
my_song_name = None
my_song_pop = None
my_artist_uri = None
my_artist_info = None
my_artist_name = None
my_artist_pop = None
my_artist_genres = None
my_album_name = None
dash = "-"
usage = "How To Use"

# Setting client prefix and intents.
client = commands.Bot(command_prefix="!=", intents=discord.Intents.all())

@client.event
async def on_ready():
    '''
    Notify on_ready.
    '''
    print("Success: Bot is connected to Discord.")

# !=ping
@client.command()
async def ping(ctx):
    '''
    Ping bot to check latency.
    '''
    bot_latency = round(client.latency * 1000)
    await ctx.send(f"Latency is: {bot_latency} ms.")

# !=how
@client.command()
async def how(ctx):
    '''
    Usage instructions for the bot.
    '''
    await ctx.send(f"{usage:-^50}\n1.) !=hello ---> Say hello to me!\n2.) !=song [song_name] ---> Type in a song you like.\n3.) !=category [category] Type in a category to search in.\n\tThe categories available are:\n\ta.) top 50\n\tb.) india\n\tc.) usa\n\td.) uk\n\te.) pop\n\tf.) rock\n\t(These are case-sensitive)\n4.) !=suggest [number_of songs] ---> Now type in the number of songs you want to find that match your taste.\n{dash:-^50}")

# !=hello
@client.command()
async def hello(ctx):
    '''
    Greet the bot.
    '''
    await ctx.send("Hello there! Tell me a song you like.")

# !=song [song_name]
@client.command()
async def song(ctx, *, song_name_arg):
    '''
    Search details of a song.
    '''
    global song_name, search_in, my_song_name, my_song_pop, my_artist_uri, my_artist_info, my_artist_name, my_artist_pop, my_artist_genres, my_album_name
    song_name = song_name_arg
    await ctx.send(f"So you like {song_name},\nLet me see what I can find out about it......")

    # 'results' contains best match to song_name when searched on spotify. [limit = 1]
    # If limit > 1, the data used to identify taste in music would be of the last song from results,
    # That would not be the best match.
    results = sp.search(q='track: ' + song_name,
                        limit=1, offset=0, type='track')
    tracks = results['tracks']['items']
    # However, in this situation, 'tracks' stores data of just one song.

    j = 1
    dict_info = {}
    for track in tracks:
        my_song_name = track['name']
        my_song_pop = track['popularity']

        my_artist_uri = track['artists'][0]['uri']
        my_artist_info = sp.artist(my_artist_uri)
        my_artist_name = track['artists'][0]['name']
        my_artist_pop = my_artist_info['popularity']
        my_artist_genres = my_artist_info['genres']

        my_album_name = track['album']['name']

        sub_dict_info = {"Song Name": my_song_name, "Song Popularity": my_song_pop, "Album": my_album_name,
                            "Artist Name": my_artist_name, "Artist Popularity": my_artist_pop, "Genres": my_artist_genres}
        dict_info[j] = sub_dict_info

        phrase = "You Like"
        to_send_song_details = f"{phrase:-^50}\n"

        for key in dict_info:
            for k1 in dict_info[key]:
                to_send_song_details += "\n"
                to_send_song_details += f"{k1} --> {dict_info[key][k1]}"

        to_send_song_details += f"\n{dash:-^50}"
        await ctx.send(to_send_song_details)

    await ctx.send("Now that that's done, would you like to look for new songs matching your taste?")

# !=category [search_category]
@client.command()
async def category(ctx, *, search_in_arg):
    '''
    Specify playlist/category to search for similar songs in.
    '''
    global search_in
    search_in = search_in_arg
    await ctx.send(f"How many songs would you like me to try and find for you in {search_in}?")

# !=suggest [num_songs]
@client.command()
async def suggest(ctx, *, num_to_suggest):
    '''
    Specify number os similar songs to look for.
    '''
    num_to_suggest = int(num_to_suggest)
    global song_name, search_in, my_song_name, my_song_pop, my_artist_uri, my_artist_info, my_artist_name, my_artist_pop, my_artist_genres, my_album_name
    await ctx.send(f"Alright! Finding {num_to_suggest} songs for you in {search_in}.......\n{dash:-^50}")

    search_in = search_in.lower()
    # by default search in usa.
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLp5XoPON0wI?si=acd09085445043b7"
    if search_in == "top 50":
        # global top 50 daily.
        playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=7f5d604a0cc24db0"
    elif search_in == "india":
        playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMWDif5SCBJq?si=86ea3467052645fa"
    elif search_in == "uk":
        playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMwmF30ppw50?si=661f0af6c2d844a0"
    elif search_in == "usa":
        playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLp5XoPON0wI?si=acd09085445043b7"
    elif search_in == "pop":
        playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DXbYM3nMM0oPk?si=05e5f56ccba64ff6"
    elif search_in == "rock":
        playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U?si=9636ce06dcb94aae"

    playlist_URI = playlist_link.split("/")[-1].split("?")[0]

    # A very naive method for checking similarity.
    i = 1
    for track in sp.playlist_tracks(playlist_URI)["items"]:
        if(i <= num_to_suggest):
            track_name = track["track"]["name"]
            artist_uri = track["track"]["artists"][0]["uri"]
            artist_info = sp.artist(artist_uri)
            artist_name = track["track"]["artists"][0]["name"]
            artist_genres = artist_info["genres"]
            album = track["track"]["album"]["name"]

            if len(artist_genres) != 0:
                if track_name != my_song_name:
                    flag_match = False
                    for i1 in my_artist_genres:
                        for i2 in artist_genres:
                            if i1 == i2:
                                flag_match = True
                    if flag_match == True:
                        await ctx.send(f"{i}.) Listen to: {track_name} by {artist_name}, from {album}.\n")
                        i += 1
            else:
                if (artist_name == my_artist_name) and (track_name != my_song_name):
                    await ctx.send(f"{i}.) Listen to: {track_name} by the same artist, {artist_name}.\n")
                    i += 1
                elif (album == my_album_name) and (track_name != my_song_name):
                    await ctx.send(f"{i}.) Listen to: {track_name} from the same album, {my_album_name}.\n")
                    i += 1
            
    await ctx.send(f"{dash:-^50}: found {i - 1} song(s)")

client.run(TOKEN)
