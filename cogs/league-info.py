import discord
from discord.ext import commands, tasks
import main
from Bot.constants import *
from riotwatcher import LolWatcher, ApiError

class LolInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rotation(self, ctx):
        r_ids = await main.get_champ_rotation()
        champ_list = await main.get_champ_list()
        champions = []

        for id in r_ids:
            for champ in champ_list['data']:
                key = champ_list['data'][champ]['key']
                if key == str(id):
                    champions.append(champ)

        em = discord.Embed(
            title='Free to Play Rotation',
            color=discord.Color.green()
        )
        em.add_field(name='\u200b', value='\u200b', inline=False)

        em.add_field(name=champions[0], value='\u200b')
        em.add_field(name=champions[1], value='\u200b')
        em.add_field(name=champions[2], value='\u200b')
        em.add_field(name=champions[3], value='\u200b')
        em.add_field(name=champions[4], value='\u200b')
        em.add_field(name=champions[5], value='\u200b')
        em.add_field(name=champions[6], value='\u200b')
        em.add_field(name=champions[7], value='\u200b')
        em.add_field(name=champions[8], value='\u200b')
        em.add_field(name=champions[9], value='\u200b')
        em.add_field(name=champions[10], value='\u200b')
        em.add_field(name=champions[11], value='\u200b')
        em.add_field(name=champions[12], value='\u200b')
        em.add_field(name=champions[13], value='\u200b')
        em.add_field(name=champions[14], value='\u200b')


        await ctx.send(embed=em)



def setup(client):
    client.add_cog(LolInfo(client))