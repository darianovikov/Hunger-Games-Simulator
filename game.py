# game.py

# IMPORTS -----------------------------------------------------------
import os
import random
import math
import time
import json
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv
import tribute

# VARIABLES -------------------------------------------------------


# SETUP GAME --------------------------------------------------------

def setup_game(tributes: list):

    if os.path.isfile("gamedata.json"):
        with open('gamedata.json','w') as j:
            j.truncate()

            tributelist = {}
            i = 1
            for t in tributes:

                district = math.ceil(i / 2)
                
                tribute = {t: {
                        "name": t,
                        "district": district,
                        "status": 'alive',
                        "weapons": [],
                        "effect": 'none',
                        "death_cause": 'none'
                        }
                           }
                tributelist.update(tribute)
                i = i + 1

            players = { "tributes": tributelist }
            json.dump(players,j,indent=3)


setup_game(['jewel', 'hole', 'yarn', 'rail', 'anger', 'question',
            'fly', 'government', 'rice', 'truck', 'religion', 'mouth',
            'ant', 'cloud', 'activity', 'addition', 'railway', 'vegetable',
            'ring', 'system', 'dock', 'mother', 'manager', 'fog'])


# RUN GAME --------------------------------------------------------

def run_game():

    print("hI!!")

# RUN BLOODBATH --------------------------------------------------------

def run_bloodbath():

# RUN DAY --------------------------------------------------------

    """
    def run_day():

        if os.path.isfile("gamedata.json"):
            with open('gamedata.json','r') as j:
                data = json.load(j)
            
            for t in data["tributes"]:
                if t("status") == 'dead':
                    return
                
                else:
                    t("status") = 'dead'
    """
