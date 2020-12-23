import discord
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
from riotwatcher import LolWatcher, ApiError
import os, json

API_KEY = 'RGAPI-fb223604-73fb-4af6-bdaf-6e4070bc2bf3'
REGION = 'na1'
LOL_WATCHER = LolWatcher(API_KEY)

client = commands.Bot(command_prefix= '#')
token = 'NzkxMzM2MTk0MjMwODQ1NDkw.X-NrQw._feoUK6vWreJHrcHAN_p4MEMP3g'

## Cog Setup ##
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded: {filename[:-3]}')

## Helper Functions ##
async def get_summoner_data():
    with open('database.json', 'r') as f:
        users = json.load(f)
    return users

async def register_summoner_data(user, name):
    users = await get_summoner_data()

    users[str(user.id)] = {}
    users[str(user.id)]['name'] = name
        
    with open('database.json', 'w') as f:
        json.dump(users, f, indent=4)

async def get_summoner_id(summoner):
    sum_id = LOL_WATCHER.summoner.by_name(REGION, summoner)
    return sum_id

async def get_rank(summoner):
    sum_id = await get_summoner_id(summoner)
    sum_rank = LOL_WATCHER.league.by_summoner(REGION, sum_id['id'])
    return sum_rank

async def get_champ_list():
    versions = LOL_WATCHER.data_dragon.versions_for_region(REGION)
    champ_version = versions['n']['champion']
    current_champ_list = LOL_WATCHER.data_dragon.champions(champ_version)
    return current_champ_list

async def remove_space(arg):
    new_arg = arg.find(" ")
    return new_arg

## Runs Bot ##
client.run(token)