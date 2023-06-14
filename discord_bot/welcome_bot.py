# welcome-bot
## this bot will send a welcome message and assign a role

import discord
import asyncio

intents = discord.Intents(members=True)
client = discord.Client(intents=intents)
welcomechannel = await client.fetch_channel(channel_id)


@client.event
async def on_ready():
    print("logged in as")
    print(client.user.name)
    print(client.user.id)


newUserMessage = """
Hey! Welcome to our server :)
"""


@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    try:
        await client.send_message(member, newUserMessage)
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)
    embed = discord.Embed(
        title="Welcome " + member.name + "!",
        description="We're so glad you're here!",
        color=discord.Color.green(),
    )

    role = discord.utils.get(member.server.roles, name="name-of-your-role")
    await client.add_roles(member, role)
    print("Added role '" + role.name + "' to " + member.name)


@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")
    embed = discord.Embed(
        title="😢 Goodbye " + member.name + "!", color=discord.Color.purple()
    )


client.run("token")
