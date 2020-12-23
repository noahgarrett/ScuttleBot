import discord
from discord.ext import commands, tasks
import main

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game("#help"))
        print("Bot is online.")
        print(f'Discord.PY Version: {discord.__version__}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use #help for the correct arguments')

def setup(client):
    client.add_cog(Events(client))