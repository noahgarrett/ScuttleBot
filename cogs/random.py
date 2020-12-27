import discord
from discord.ext import commands, tasks
import main
import json
import random
class Random(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="rchamp", help="#rchamp | Get Random Champion and role")
    async def rchamp(self, ctx):
        role_list = ['Top', 'Jungle', 'Mid', 'Support', 'ADC']

        champion_json = await main.get_champ_list()
        list_of_champions = self.get_list_of_champions(champion_json)
        randomChamp = random.choice(list_of_champions)
        randomRole = random.choice(role_list)

        thumbnail_url = f'http://ddragon.leagueoflegends.com/cdn/10.25.1/img/champion/{randomChamp}.png'

        em = discord.Embed(
            title=f"ScuttleBot's Champion Pick",
            description=f"Throwing ranked games = wins",
            color=discord.Color.dark_magenta()
        )
        em.set_thumbnail(url=f'{thumbnail_url}')
        em.add_field(name='Champion:', value=randomChamp, inline=True)
        em.add_field(name='Role:', value=randomRole, inline=True)

        await ctx.send(embed=em)

    def get_list_of_champions(self, champion_json):
        champion_dict = dict(champion_json)
        champion_data = dict(champion_dict['data'])
        listOfChampions = list(champion_data.keys())
        return listOfChampions

def setup(client):
    client.add_cog(Random(client))