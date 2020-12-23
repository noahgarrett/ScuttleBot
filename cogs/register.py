import discord
from discord.ext import commands, tasks
import main

class Register(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="register", help="#register (SummonerName) NO SPACES")
    async def register(self, ctx, name):
        user = ctx.author
        users = await main.get_summoner_data()

        is_registered = False

        for i in users:
            if i == str(user.id):
                is_registered = True
                break

        if is_registered:
            await ctx.send(f'You are already registered as {name}')
        elif not is_registered:
            await main.register_summoner_data(ctx.author, name)
            await ctx.send(f'**{name}** has now been registered')

    
def setup(client):
    client.add_cog(Register(client))