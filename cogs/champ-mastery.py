import discord
from discord.ext import commands
import main
from riotwatcher import LolWatcher, ApiError

class ChampMastery(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mastery(self, ctx, name):
        REGION = 'na1'
        LOL_WATCHER = LolWatcher(main.API_KEY)
        sum_id = await main.get_summoner_id(name)

        sum_name = sum_id['name']
        id = sum_id['id']

        mastery = await main.get_summoner_mastery(REGION, id)

        champ1 = mastery[0]['championId']
        champ1_level = mastery[0]['championLevel']
        champ1_points = mastery[0]['championPoints']

        champ2 = mastery[1]['championId']
        champ2_level = mastery[1]['championLevel']
        champ2_points = mastery[1]['championPoints']

        champ3 = mastery[2]['championId']
        champ3_level = mastery[2]['championLevel']
        champ3_points = mastery[2]['championPoints']

        champ_list = await main.get_champ_list()
        for champion in champ_list['data']:
            for key in champ_list['data'][champion]:
                if key == 'key':
                    if str(champ1) == champ_list['data'][champion]['key']:
                        champ1 = champion
                        break
                    elif str(champ2) == champ_list['data'][champion]['key']:
                        champ2 = champion
                        break
                    elif str(champ3) == champ_list['data'][champion]['key']:
                        champ3 = champion
                        break
                    break

        thumbnail_url = f'http://ddragon.leagueoflegends.com/cdn/10.25.1/img/champion/{champ1}.png'

        em = discord.Embed(
            title=f'Mastery Info for {sum_name}',
            description='Top 3 Champions',
            color=discord.Color.green()
        )
        em.set_thumbnail(url=thumbnail_url)

        em.add_field(name=f'{str(champ1)}', value=f'Level: {champ1_level}\n'
                                          f'Points: {champ1_points}', inline=True)
        em.add_field(name=f'{champ2}', value=f'Level: {champ2_level}\n'
                                             f'Points: {champ2_points}', inline=True)
        em.add_field(name=f'{champ3}', value=f'Level: {champ3_level}\n'
                                             f'Points: {champ3_points}', inline=True)
        em.set_footer(text='Development still in progress..')

        await ctx.send(embed=em)





def setup(client):
    client.add_cog(ChampMastery(client))