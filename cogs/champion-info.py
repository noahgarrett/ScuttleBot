import discord
from discord.ext import commands, tasks
import main
from Bot.constants import *
from riotwatcher import LolWatcher, ApiError

class ChampionInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="champ", help="#champ (champion name)") # MAKE FUCKIN PRETTY
    async def champ(self, ctx, champion, champ2=None):
        current_champ_list = await main.get_champ_list()
        champ = champion
        champFullName = champ
        if not champ2 is None:
            champ = f'{champion}{champ2}'
            champFullName = f'{champion} {champ2}'

        champion_stats = "No Champion Found"

        for key in current_champ_list['data']:
            keyUpper = key.upper()
            if keyUpper == champ.upper():
                champion_stats = current_champ_list['data'][key]['stats']
                champ = key
                break

        thumbnail_url = f'http://ddragon.leagueoflegends.com/cdn/10.25.1/img/champion/{champ}.png'

        em = discord.Embed(
            title=f"{champFullName}'s Stats",
            description=f"{current_champ_list['data'][champ]['tags']}",
            color=discord.Color.purple())
        em.set_thumbnail(url=f'{thumbnail_url}')
        em.add_field(name=f'HP', value=f'{champion_stats["hp"]}')
        em.add_field(name=f'HP Per Level', value=f'{champion_stats["hpperlevel"]}')
        em.add_field(name=f'Mana', value=f'{champion_stats["mp"]}')
        await ctx.send(embed=em)

        # await ctx.send(champion_stats)

def setup(client):
    client.add_cog(ChampionInfo(client))