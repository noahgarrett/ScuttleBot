import discord
from discord.ext import commands
import main
from riotwatcher import LolWatcher, ApiError

class MatchHistory(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(MatchHistory(client))