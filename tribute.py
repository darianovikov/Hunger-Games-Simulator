# tribute.py

# IMPORTS -----------------------------------------------------------
import os
import random
import math
import time
import json
import discord
from discord.ext.commands import Bot
from discord.ext import commands

# GLOBALS --------------------------------------------------------

with open('gamedata.json','r') as j:
    data = json.load(j)

#disWeight = 3
districtModifier = False

# CONDITIONS --------------------------------------------------------

def update_status(tribute: str):

    # variables ------------------------------------->>
    tdata = data["tributes"][tribute]
    if districtModifier:
        dis = tdata("district")
        disMod = (13 - dis)
    else:
        disMod = 0

    # random gift calculator -------------------------->>

    giftprob = (random.randrange(0, 100) + (disMod * 3))

    if (giftprob >= 80):
        gifts = ['sword', 'bow', 'mace', 'dagger', 'axe',
                 'food', 'medicine', 'water']
        gift = random.choice(gifts)
    else:
        gift = 'none'

    # random effect calculator ------------------------>>
    effectprob = random.randrange(0, 100)
    if ((effectprob <= 5) and (gift != 'water')):
        effect = 'thirst'
    elif ((effectprob <= 10) and (gift != 'food')):
        effect = 'hunger'
    elif ((effectprob <= 12) and (gift != 'medecine')):
        effect = 'illness'
    elif (effectprob <= 13):
        effect = 'insanity'
    else:
        effect = 'none'
        
    # big update status ------------------------------->>
    #current_effect = tdata[effect]
        

    # life chance ------------------------------------->>

    effect = tdata['effect']
    match effect:
        case 'thirst':
            effectMod = -2
        case 'hunger':
            effectMod = -3
        case 'insanity':
            effectMod = -10
        case 'illness':
            effectMod = -10
        case _:
            effectMod = 0

    lifeprob = (random.randrange(0, 100) + (disMod * 2) + effectMod)
    if (lifeprob >= 30):
        status = 'alive'
        deathcause = 'none'
    else:
        status = 'dead'
        deathcause = effect
        
    print(gift + ' ' + effect + ' ' + status + ' ' + deathcause)

update_status('hole')
update_status('hole')
update_status('hole')
update_status('hole')
update_status('hole')
update_status('hole')
update_status('hole')
update_status('hole')
