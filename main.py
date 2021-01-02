import discord
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
from riotwatcher import LolWatcher, ApiError
import os, json

API_KEY = 'RGAPI-4da05ce5-bc28-4d59-aef1-1caa5d246a91'
REGION = 'na1'
LOL_WATCHER = LolWatcher(API_KEY)

client = commands.Bot(command_prefix= '#')
client.remove_command('help')
token = 'NzkxMzM2MTk0MjMwODQ1NDkw.X-NrQw.tOvPuEh5k6mW6ltEgTsiBPaOhvA'

## Cog Setup ##
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded: {filename[:-3]}')

## Bot Specific Commands ##
@client.command()
async def servercount(ctx):
    await ctx.send(f'I am currently in **{len(client.guilds)}** servers')

@client.command()
async def vote(ctx):
    em = discord.Embed(
        title='Please support Scuttlebot on top.gg by voting!',
        color=discord.Color.purple()
    )
    em.add_field(name='Click here to vote', value='[Vote for ScuttleBot](https://top.gg/bot/791336194230845490/vote)')
    await ctx.send(embed=em)

## Helper Functions ##
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

async def get_champ_rotation():
    rotation_json = LOL_WATCHER.champion.rotations(REGION)
    r_ids = rotation_json['freeChampionIds']
    return r_ids

## Help Command ##
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title='ScuttleBot v1.0.0',
        description='Use #help <command> for extended information on a command',
        color=discord.Color.orange()
    )
    em.add_field(name='Champion Info', value='`champion\n` `stats`', inline=True)
    em.add_field(name='Player Info', value='`rank`', inline=True)
    em.add_field(name='Champion Selecter', value='`rchamp`', inline=True)
    em.add_field(name='League Info', value='`rotation\n` `tierlist`', inline=True)
    em.add_field(name='\u200b', value='\u200b', inline=True)
    em.add_field(name='Bot Info', value=f'`servercount\n` `vote`', inline=True)

    em.add_field(name='\u200b', value='\u200b', inline=False)

    em.add_field(name='Invite Me!', value='[Invite](https://discord.com/oauth2/authorize?client_id=791336194230845490&scope=bot&permissions=347201)',
                 inline=True)
    em.add_field(name='Please vote!', value='[Vote for ScuttleBot](https://top.gg/bot/791336194230845490/vote)')
    em.add_field(name='Join My Support Server', value='[The River](https://discord.gg/VMwphqfmQk)', inline=True)

    await ctx.send(embed=em)

@help.command()
async def champion(ctx):
    em = discord.Embed(
        title='#champion',
        description="Displays a champion's win-rate, ban-rate, etc. for the current patch\n"
                    "Displays a champion's optimal runes for the current patch",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`#champion <championName> <role>`')
    em.add_field(name='Note', value='`<championName> Please input name w/o spaces`', inline=False)
    await ctx.send(embed=em)

@help.command()
async def stats(ctx):
    em = discord.Embed(
        title='#stats',
        description="Displays a champion's in depth statistics",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`#stats <championName>`')
    em.add_field(name='Note', value='`<championName> Please input name w/o spaces`', inline=False)
    await ctx.send(embed=em)

@help.command()
async def rank(ctx):
    em = discord.Embed(
        title='#rank',
        description="Displays a provided summoner's ranked statistics",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`#rank <summonerName>`')
    em.add_field(name='Note', value='`<summonerName> Please input name w/o spaces`', inline=False)
    await ctx.send(embed=em)

@help.command()
async def rchamp(ctx):
    em = discord.Embed(
        title='#rchamp',
        description="Provides a random champion + a random role",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`#rchamp`')
    await ctx.send(embed=em)

@help.command()
async def rotation(ctx):
    em = discord.Embed(
        title='#rotation',
        description="Displays the current Free Champion Rotation",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`#rotation`')
    await ctx.send(embed=em)

@help.command()
async def servercount(ctx):
    em = discord.Embed(
        title='#servercount',
        description="Displays the current number of servers ScuttleBot is in",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`#servercount`')
    await ctx.send(embed=em)

@help.command()
async def vote(ctx):
    em = discord.Embed(
        title='#vote',
        description="Displays the top.gg vote link",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`#vote`')
    await ctx.send(embed=em)

@help.command()
async def tierlist(ctx):
    em = discord.Embed(
        title='#tierlist',
        description="Displays the current tier list for a given role",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`#tierlist <role>`')
    em.set_footer(text='role = top, jungle, mid, support, adc')
    await ctx.send(embed=em)

## Ping Command ##
@client.command()
async def ping(ctx):
    await ctx.send(f"My latency is: {round(client.latency * 1000)}ms")

## Runs Bot ##
client.run(token)
# client.run(os.environ['token'])