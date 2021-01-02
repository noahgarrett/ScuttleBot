import discord
from discord.ext import commands
import main
import bs4, requests
from Bot.champ_tier_list import *

class TierList(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tierlist(self, ctx, role):
        if role == 'top':
            tier_url = 'https://tierlist.gg/top-lane-tier-list'
            tier_response = requests.get(tier_url)
            tier_soup = bs4.BeautifulSoup(tier_response.text, 'lxml')

            top_s_tier = []
            for i in range(0, 10):
                tier = tier_soup.find_all('div', {'class': 'TierPage-Tier-Items'})[0].findAll('div', {
                    'class': 'TierItem-Image'})[i].find('img').attrs['alt']
                top_s_tier.append(tier)
                if tier == None:
                    break

            em = discord.Embed(
                title='Top Lane Tier List',
                color=discord.Color.green()
            )
            em.add_field(name='S-Tier Picks', value=top_s_tier)
            em.set_footer(text='Work in progress.. Join Support server for updates')
            await ctx.send(embed=em)

        elif role == 'jungle':
            pass
        elif role == 'mid':
            pass
        elif role == 'support':
            pass
        elif role == 'adc' or role == 'bot' or role == 'bottom':
            pass
        else:
            await ctx.send('Please use #help tierlist for correct syntax')
            



def setup(client):
    client.add_cog(TierList(client))