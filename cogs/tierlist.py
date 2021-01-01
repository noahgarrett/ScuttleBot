import discord
from discord.ext import commands
import main
from Bot.champ_tier_list import *

class TierList(commands.Cog):
    def __init__(self, client):
        self.client = client

    # @commands.command()
    # async def tierlist(self, ctx, role):
    #     if role == 'top':
    #         em = discord.Embed(
    #             title='Top Lane Tier List',
    #             description='Champions are not listed in a particular order',
    #             color=discord.Color.blurple()
    #         )
            



def setup(client):
    client.add_cog(TierList(client))