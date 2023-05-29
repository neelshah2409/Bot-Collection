import os
import asyncio
from discord import Intents
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv("TOKEN_KEY")
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.reactions = True
intents.message_content = True
bot = commands.Bot(command_prefix="&", intents=intents)


# @bot.command(name='test')
# async def test(ctx):
#     await ctx.send('Test successful.')


@bot.command(name="poll")
async def poll(ctx, seconds: int, question: str, *options: str):
    await ctx.send(f"Voting Started. Only {seconds} seconds left!")

    if len(options) <= 1:
        await ctx.send("You need more than one option to create a poll!")
        return
    if len(options) > 10:
        await ctx.send("You can only have up to 10 options.")
        return

    reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    description = []
    for x, option in enumerate(options):
        description += "\n {} {}".format(reactions[x], option)
    embed = discord.Embed(title=question, description="".join(description))

    react_message = await ctx.send(embed=embed)
    for reaction in reactions[: len(options)]:
        await react_message.add_reaction(reaction)
    embed.set_footer(text="Poll ID: {}".format(react_message.id))
    await react_message.edit(embed=embed)

    await asyncio.sleep(seconds)
    react_message = await ctx.channel.fetch_message(react_message.id)

    results = {}
    for reaction in react_message.reactions:
        emoji = str(reaction.emoji)
        if emoji in reactions:
            results[emoji] = reaction.count - 1

    sort_results = sorted(
        [(value, key) for (key, value) in results.items()], reverse=True
    )

    if sort_results:
        max_votes = sort_results[0][0]
        winners = [tup[1] for tup in sort_results if tup[0] == max_votes]

        if len(winners) > 1:
            await ctx.send(
                "It's a tie! The most voted options were "
                + ", ".join(winners)
                + " with "
                + str(max_votes)
                + " votes each."
            )
        else:
            await ctx.send(
                "The most voted option was "
                + winners[0]
                + " with "
                + str(max_votes)
                + " votes."
            )
    else:
        await ctx.send("No one voted!")


bot.run(token)
