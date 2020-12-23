import discord
from discord.ext import commands, tasks
import main
from Bot.constants import *
from riotwatcher import LolWatcher, ApiError

class Counter(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Counter(client))