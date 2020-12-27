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
        champion_json = await main.get_champ_list()
        list_of_champions = self.get_list_of_champions(champion_json)
        randomChamp = random.choice(list_of_champions)

        e = discord.Embed()


        # await ctx.send(randomChamp)

    def get_list_of_champions(self, champion_json):
        champion_dict = dict(champion_json)
        champion_data = dict(champion_dict['data'])
        listOfChampions = list(champion_data.keys())
        return listOfChampions

def setup(client):
    client.add_cog(Random(client))