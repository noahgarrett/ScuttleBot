import discord
from discord.ext import commands
import main
from riotwatcher import LolWatcher, ApiError

class MatchHistory(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def matchhistory(self, ctx, summoner):
        id = 3730982180
        match_list = await main.get_match_history(summoner)
        game_id = await main.get_match_info(id)

        print(game_id)
        await ctx.send(match_list)

def setup(client):
    client.add_cog(MatchHistory(client))