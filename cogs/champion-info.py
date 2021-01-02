import discord
from discord.ext import commands
import main
import requests
import bs4
from Bot.runes import *
from Bot.summoner_spells import *

class ChampionInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="stats", help="#stats (champion name)") # MAKE FUCKIN PRETTY
    async def stats(self, ctx, champion, champ2=None):
        current_champ_list = await main.get_champ_list()
        champ = champion
        champFullName = champ
        if not champ2 is None:
            champ = f'{champion}{champ2}'
            champFullName = f'{champion} {champ2}'

        champion_stats = "No Champion Found"

        for key in current_champ_list['data']:
            keyUpper = key.upper()
            if keyUpper == champ.upper():
                champion_stats = current_champ_list['data'][key]['stats']
                champ = key
                break

        thumbnail_url = f'http://ddragon.leagueoflegends.com/cdn/10.25.1/img/champion/{champ}.png'

        embed = discord.Embed(title=f"Values for: {champ}",
                              description=f"{current_champ_list['data'][champ]['tags']}", color=0xee00ff)
        embed.set_thumbnail(url=f'{thumbnail_url}')
        embed.add_field(name=f'HP', value=f'{champion_stats["hp"]}', inline=True)
        embed.add_field(name=f'HP Per Level', value=f'{champion_stats["hpperlevel"]}', inline=True)
        embed.add_field(name=f'Mana', value=f'{champion_stats["mp"]}', inline=True)
        embed.add_field(name=f'Mana Per Level', value=f'{champion_stats["mpperlevel"]}', inline=True)
        embed.add_field(name=f'AD', value=f'{champion_stats["attackdamage"]}', inline=True)
        embed.add_field(name=f'AD Per Level', value=f'{champion_stats["attackdamageperlevel"]}', inline=True)
        embed.add_field(name=f'Attack Speed', value=f'{champion_stats["attackspeed"]}', inline=True)
        embed.add_field(name=f'Attack Speed Per Level', value=f'{champion_stats["attackspeedperlevel"]}', inline=True)
        embed.add_field(name=f'Move Speed', value=f'{champion_stats["movespeed"]}', inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='champion', help='#champion (champion name) (position) | View champion stats/build')
    async def champion(self, ctx, champion, role):

        current_champ_list = await main.get_champ_list()
        champ = champion

        for key in current_champ_list['data']:
            keyUpper = key.upper()
            if keyUpper == champ.upper():
                champ = key
                break

        thumbnail_url = f'http://ddragon.leagueoflegends.com/cdn/10.25.1/img/champion/{champ}.png'

        stats_url = f'https://u.gg/lol/champions/{champion}/build'
        runes_url = f'https://na.op.gg/champion/{champion}/statistics/{role}'

        response = requests.get(stats_url)
        response_ = requests.get(runes_url)

        soup = bs4.BeautifulSoup(response.text, 'lxml')
        soup_ = bs4.BeautifulSoup(response_.text, 'lxml')

        win_rate = soup_.find_all('div', {'class': 'champion-stats-trend-rate'})[0].text
        champ_rank = soup_.find_all('div', {'class': 'champion-stats-trend-rank'})[0].find('b').text
        pick_rate = soup_.find_all('div', {'class': 'champion-stats-trend-rate'})[1].text
        ban_rate = soup.find_all('div', {'class': 'ban-rate'})[0].find('div').text
        matches = soup.find_all('div', {'class': 'matches'})[0].find('div').text

        ######### Runes #########
        rune_tree = soup_.find_all('div', {'class': 'perk-page__row'})[0].find('img').attrs['src']
        tree_name = ''
        for runes in primary_rune_tree_img:
            if rune_tree == primary_rune_tree_img[runes]:
                for tree in tree_names:
                    if rune_tree == tree_names[tree]:
                        for emoji in primary_rune_tree_emoji:
                            if rune_tree == primary_rune_tree_emoji[emoji]:
                                rune_tree = emoji
                                tree_name = tree
                                break

        keystone = soup_.find_all('div', {'class': 'perk-page__item--active'})[0].find('img').attrs['src']
        keystone_name = ''
        for stone in keystones_img:
            if keystone == keystones_img[stone]:
                for k_name in keystone_names:
                    if keystone == keystone_names[k_name]:
                        for k_emoji in keystones_emoji:
                            if keystone == keystones_emoji[k_emoji]:
                                keystone = k_emoji
                                keystone_name = k_name
                                break

        rune1 = soup_.find_all('div', {'class': 'perk-page__item--active'})[1].find('img').attrs['src']
        rune1_name = ''
        for rune in rune1_img:
            if rune1 == rune1_img[rune]:
                for r1_name in rune1_names:
                    if rune1 == rune1_names[r1_name]:
                        for r1_emoji in rune1_emoji:
                            if rune1 == rune1_emoji[r1_emoji]:
                                rune1 = r1_emoji
                                rune1_name = r1_name
                                break

        rune2 = soup_.find_all('div', {'class': 'perk-page__item--active'})[2].find('img').attrs['src']
        rune2_name = ''
        for rune_ in rune2_img:
            if rune2 == rune2_img[rune_]:
                for r2_name in rune2_names:
                    if rune2 == rune2_names[r2_name]:
                        for r2_emoji in rune2_emoji:
                            if rune2 == rune2_emoji[r2_emoji]:
                                rune2 = r2_emoji
                                rune2_name = r2_name
                                break

        rune3 = soup_.find_all('div', {'class': 'perk-page__item--active'})[3].find('img').attrs['src']
        rune3_name = ''
        for rune__ in rune3_img:
            if rune3 == rune3_img[rune__]:
                for r3_name in rune3_names:
                    if rune3 == rune3_names[r3_name]:
                        for r3_emoji in rune3_emoji:
                            if rune3 == rune3_emoji[r3_emoji]:
                                rune3 = r3_emoji
                                rune3_name = r3_name
                                break

        rune_tree_2 = soup_.find_all('div', {'class': 'perk-page__item--mark'})[1].find('img').attrs['src']
        tree_name2 = ''
        for runes_ in secondary_rune_tree_img:
            if rune_tree_2 == secondary_rune_tree_img[runes_]:
                for tree_ in tree_names:
                    if rune_tree_2 == tree_names[tree_]:
                        for emoji_ in primary_rune_tree_emoji:
                            if rune_tree_2 == primary_rune_tree_emoji[emoji_]:
                                rune_tree_2 = emoji_
                                tree_name2 = tree_
                                break

        secondary1 = soup_.find_all('div', {'class': 'perk-page__item--active'})[4].find('img').attrs['src']
        secondary1_name = ''
        for second1 in second1_img:
            if secondary1 == second1_img[second1]:
                for second1_name in second1_names:
                    if secondary1 == second1_names[second1_name]:
                        for s1_emoji in second1_emoji:
                            if secondary1 == second1_emoji[s1_emoji]:
                                secondary1 = s1_emoji
                                secondary1_name = second1_name
                                break

        secondary2 = soup_.find_all('div', {'class': 'perk-page__item--active'})[5].find('img').attrs['src']
        secondary2_name = ''
        for second2 in second2_img:
            if secondary2 == second2_img[second2]:
                for second2_name in second2_names:
                    if secondary2 == second2_names[second2_name]:
                        for s2_emoji in second2_emoji:
                            if secondary2 == second2_emoji[s2_emoji]:
                                secondary2 = s2_emoji
                                secondary2_name = second2_name
                                break
        ###################

        ###### Summoner Spells ######
        summoner_spell1 = soup_.find_all('ul', {'class': 'champion-stats__list'})[0].findAll('li', {'class': 'champion-stats__list__item'})[0].find('img').attrs['src']
        summoner_spell1_name = ''
        for sum1 in summoner_spells:
            if summoner_spell1 == summoner_spells[sum1]:
                for sum1_name in summoner_spells_names:
                    if summoner_spell1 == summoner_spells_names[sum1_name]:
                        for sum1_emoji in summoner_spells_emoji:
                            if summoner_spell1 == summoner_spells_emoji[sum1_emoji]:
                                summoner_spell1 = sum1_emoji
                                summoner_spell1_name = sum1_name
                                break

        summoner_spell2 = soup_.find_all('ul', {'class': 'champion-stats__list'})[0].findAll('li', {'class': 'champion-stats__list__item'})[1].find('img').attrs['src']
        summoner_spell2_name = ''
        for sum2 in summoner_spells:
            if summoner_spell2 == summoner_spells[sum2]:
                for sum2_name in summoner_spells_names:
                    if summoner_spell2 == summoner_spells_names[sum2_name]:
                        for sum2_emoji in summoner_spells_emoji:
                            if summoner_spell2 == summoner_spells_emoji[sum2_emoji]:
                                summoner_spell2 = sum2_emoji
                                summoner_spell2_name = sum2_name
                                break
        #############################

        ###### Items ######

        ###################

        champ_name = soup_.find_all('h1', {'class': 'champion-stats-header-info__name'})[0].text
        em = discord.Embed(
            title=f"{champ_name} {role}",
            description=f"Statistics",
            color=discord.Color.red())
        em.set_thumbnail(url=thumbnail_url)
        em.add_field(name='Win-Rate', value=win_rate, inline=True)
        em.add_field(name='Champion Rank', value=f'{champ_rank}th', inline=True)

        em.add_field(name='Pick-Rate', value=pick_rate, inline=False)

        em.add_field(name='Ban-Rate', value=ban_rate, inline=True)
        em.add_field(name='Matches', value=matches, inline=True)

        em.add_field(name='\u200b', value='\u200b', inline=False)

        em.add_field(name='Spells:', value=f'{summoner_spell1} **{summoner_spell1_name}**\n'
                                           f'{summoner_spell2} **{summoner_spell2_name}**')

        em.add_field(name='\u200b', value='\u200b', inline=False)

        em.add_field(name='Runes:', value=f'{rune_tree}**{tree_name}**\n'
                                          f'\u200b\n'
                                          f'{keystone}{keystone_name}\n'
                                          f'{rune1}{rune1_name}\n'
                                          f'{rune2}{rune2_name}\n'
                                          f'{rune3}{rune3_name}\n', inline=True)
        em.add_field(name='\u200b', value='\u200b', inline=True)
        em.add_field(name='\u200b', value=f'{rune_tree_2}**{tree_name2}**\n'
                                          f'\u200b\n'
                                          f'{secondary1}{secondary1_name}\n'
                                          f'{secondary2}{secondary2_name}\n', inline=True)

        em.add_field(name='\u200b', value='\u200b', inline=False)

        em.add_field(name='Items:', value='Test')

        await ctx.send(embed=em)



def setup(client):
    client.add_cog(ChampionInfo(client))