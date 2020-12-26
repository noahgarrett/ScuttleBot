import discord
from discord.ext import commands, tasks
import main
from Bot.constants import *
from riotwatcher import LolWatcher, ApiError

class PlayerStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="rank", help="#rank | Retrieve a summoner's ranked stats")
    async def rank(self, ctx, summoner):
        try:
            sum_rank = await main.get_rank(summoner)
            wl_ratio = sum_rank[0]["wins"] / sum_rank[0]["losses"]
            formatted_wl = "{:.2f}".format(wl_ratio)

            if sum_rank[0]["tier"] == "IRON":
                rank_img = IRON_URL
            elif sum_rank[0]["tier"] == "BRONZE":
                rank_img = BRONZE_URL
            elif sum_rank[0]["tier"] == "SILVER":
                rank_img = SILVER_URL
            elif sum_rank[0]["tier"] == "GOLD":
                rank_img = GOLD_URL
            elif sum_rank[0]["tier"] == "PLATINUM":
                rank_img = PLATINUM_URL
            elif sum_rank[0]["tier"] == "DIAMOND":
                rank_img = DIAMOND_URL
            elif sum_rank[0]["tier"] == "MASTER":
                rank_img = MASTER_URL
            elif sum_rank[0]["tier"] == "GRANDMASTER":
                rank_img = GRANDMASTER_URL
            elif sum_rank[0]["tier"] == "CHALLENGER":
                rank_img = CHALLENGER_URL

            em = discord.Embed(
                title=f"{sum_rank[0]['summonerName']}'s Ranked Stats",
                description=f"Ranked Solo/Duo",
                color=discord.Color.red())
            em.set_thumbnail(url=rank_img)
            em.add_field(name=f'Rank', value=f'{sum_rank[0]["tier"]} {sum_rank[0]["rank"]}')
            em.add_field(name="Wins", value=f'{sum_rank[0]["wins"]}')
            em.add_field(name="Losses", value=f'{sum_rank[0]["losses"]}')
            em.add_field(name="W/L Ratio", value=f'{formatted_wl}')
            em.add_field(name="LP", value=f'{sum_rank[0]["leaguePoints"]}')
            await ctx.send(embed=em)
        except ApiError as err:
            if err.response.status_code == 404:
                await ctx.send('That player is too trash for ranked.. Sorry')
            else:
                raise

def setup(client):
    client.add_cog(PlayerStats(client))