# hunger-games.py

# IMPORTS -----------------------------------------------------------
import os
import random
import math
import time
import json
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import dotenv
import game

#SETUP ----------------------------------------------------------------
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='hg!' , intents = discord.Intents.all())

#ONREADY --------------------------------------------------------------
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


#MESSAGE --------------------------------------------------------------
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    elif message.content == 'qu!time':

        timecode = math.floor( time.time())
        unixtime = '<t:' + str(timecode) + ':t>'
        await message.channel.send(unixtime)
        
    await client.process_commands(message)


#COMMAND: SETUP-GAME ------------------------------------------------------
@client.command(name='setup-game')
async def setup_game(ctx, player1: str, player2: str, player3: str, player4: str, player5: str, player6: str,
                     player7: str, player8: str, player9: str, player10: str, player11: str, player12: str,
                     player13: str, player14: str, player15: str, player16: str, player17: str, player18: str,
                     player19: str, player20: str, player21: str, player22: str, player23: str, player24: str):

        try:
            tributes = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12,
                        player13, player14, player15, player16, player17, player18, player19, player20, player21, player22, player23, player24]
            
            game.setup_game(tributes)
            await ctx.channel.send("Setup succesful. May the odds be ever in your favor!")
            
        except:
            await ctx.channel.send("Please try setting up again.")


#COMMAND: HERE ------------------------------------------------------
@client.command(name='here')
async def here(ctx):

        await ctx.channel.send("Here!")


#RUN---------------------------------------------------------------------
client.run(TOKEN)
