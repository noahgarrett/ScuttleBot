import discord
from discord.ext import commands, tasks
import main
from Bot.constants import *
from riotwatcher import LolWatcher, ApiError
import requests
import bs4
from Bot.rune_img import *

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

        win_rate = soup.find_all('div', {'class': 'win-rate'})[0].find('div').text
        champ_rank = soup.find_all('div', {'class': 'overall-rank'})[0].find('div').text
        pick_rate = soup.find_all('div', {'class': 'pick-rate'})[0].find('div').text
        ban_rate = soup.find_all('div', {'class': 'ban-rate'})[0].find('div').text
        matches = soup.find_all('div', {'class': 'matches'})[0].find('div').text

        rune_tree = soup_.find_all('div', {'class': 'perk-page__row'})[0].find('img').attrs['src']
        tree_name = ''
        if rune_tree == precision_tree:
            rune_tree = '<:precision:792162680369971261>'
            tree_name = 'Precision'
        elif rune_tree == domination_tree:
            rune_tree = '<:domination:792414255214493716>'
            tree_name = 'Domination'
        elif rune_tree == sorcery_tree:
            rune_tree = '<:sorcery:792441210152288256>'
            tree_name = 'Sorcery'
        elif rune_tree == resolve_tree:
            rune_tree = '<:resolve:792421207949312020>'
            tree_name = 'Resolve'
        elif rune_tree == inspiration_tree:
            rune_tree = '<:inspiration:792420733887709224>'
            tree_name = 'Inspiration'
        else:
            rune_tree = 'Not Found'
            tree_name = ' 404'

        keystone = soup_.find_all('div', {'class': 'perk-page__item--active'})[0].find('img').attrs['src']
        keystone_name = ''
        if keystone == fleet:
            keystone = '<:FleetFootwork:792169831943503923>'
            keystone_name = 'Fleet Footwork'
        elif keystone == conqueror:
            keystone = '<:Conqueror:792169654340419654>'
            keystone_name = 'Conqueror'
        elif keystone == pta:
            keystone = '<:pta:792175571857571841>'
            keystone_name = 'Press The Attack'
        elif keystone == lethal_tempo:
            keystone = '<:lt:792413035187798047>'
            keystone_name = 'Lethal Tempo'
        elif keystone == hob:
            keystone = '<:hob:792415338142367774>'
            keystone_name = 'Hail of Blades'
        elif keystone == electrocute:
            keystone = '<:electrocute:792415844625547305>'
            keystone_name = 'Electrocute'
        elif keystone == predator:
            keystone = '<:predator:792417169086218280>'
            keystone_name = 'Predator'
        elif keystone == dh:
            keystone = '<:dh:792417673408413728>'
            keystone_name = 'Dark Harvest'
        elif keystone == aery:
            keystone = '<:aery:792419580969746482>'
            keystone_name = 'Summon Aery'
        elif keystone == comet:
            keystone = '<:comet1:792419590751256597>'
            keystone_name = 'Arcane Comet'
        elif keystone == phase_rush:
            keystone = '<:phaserush:792419599215624243>'
            keystone_name = 'Phase Rush'
        elif keystone == grasp:
            keystone = '<:grasp:792422018187264020>'
            keystone_name = 'Grasp of the Undying'
        elif keystone == aftershock:
            keystone = '<:aftershock:792422039952556062>'
            keystone_name = 'Aftershock'
        elif keystone == guardian:
            keystone = '<:guardian:792422039411490858>'
            keystone_name = 'Guardian'
        elif keystone == glacial:
            keystone = '<:glacial:792423350667706368>'
            keystone_name = 'Glacial Augment'
        elif keystone == spellbook:
            keystone = '<:spellbook:792423350956982302>'
            keystone_name = 'Unsealed Spellbook'
        elif keystone == omnistone:
            keystone = '<:omnistone:792423350609510449>'
            keystone_name = 'Prototype: Omnistone'
        else:
            keystone = '**Not Found**'
            keystone_name = ' 404'

        rune1 = soup_.find_all('div', {'class': 'perk-page__item--active'})[1].find('img').attrs['src']
        rune1_name = ''
        if rune1 == overheal:
            rune1 = '<:overheal:792426715120140288>'
            rune1_name = 'Overheal'
        elif rune1 == triumph:
            rune1 = '<:triumph1:792426714973208597>'
            rune1_name = 'Triumph'
        elif rune1 == pom:
            rune1 = '<:pom:792426715217002526>'
            rune1_name = 'Presence of Mind'
        elif rune1 == cheapshot:
            rune1 = '<:cheapshot:792442972620455947>'
            rune1_name = 'Cheap Shot'
        elif rune1 == tob:
            rune1 = '<:tob:792442972855074826>'
            rune1_name = 'Taste of Blood'
        elif rune1 == sudden_impact:
            rune1 = '<:suddenimpact:792442972875653140>'
            rune1_name = 'Sudden Impact'
        elif rune1 == orb:
            rune1 = '<:orb:792454318623555594>'
            rune1_name = 'Nullifying Orb'
        elif rune1 == manaflow:
            rune1 = '<:manaflow:792454318032420874>'
            rune1_name = 'Manaflow Band'
        elif rune1 == nimbus:
            rune1 = '<:nimbus:792454318191149136>'
            rune1_name = 'Nimbus Cloak'
        elif rune1 == demolish:
            rune1 = '<:demolish:792457268523696128>'
            rune1_name = 'Demolish'
        elif rune1 == font_of_life:
            rune1 = '<:fontoflife:792457268100202527>'
            rune1_name = 'Font of Life'
        elif rune1 == shield_bash:
            rune1 = '<:shieldbash:792457268637204490>'
            rune1_name = 'Shield Bash'
        elif rune1 == hexflash:
            rune1 = '<:hexflash:792458707744980993>'
            rune1_name = 'Hexflash Flashtraption'
        elif rune1 == footwear:
            rune1 = '<:footwear:792458707794788372>'
            rune1_name = 'Magical Footwear'
        elif rune1 == stopwatch:
            rune1 = '<:stopwatch1:792458707509968936>'
            rune1_name = 'Perfect Timing'
        else:
            rune1 = '**Not Found**'
            rune1_name = ' 404'

        rune2 = soup_.find_all('div', {'class': 'perk-page__item--active'})[2].find('img').attrs['src']
        rune2_name = ''
        if rune2 == alacrity:
            rune2 = '<:alacrity:792429210035159073>'
            rune2_name = 'Legend: Alacrity'
        elif rune2 == tenacity:
            rune2 = '<:tenacity:792429212383969311>'
            rune2_name = 'Legend: Tenacity'
        elif rune2 == bloodline:
            rune2 = '<:bloodline:792429210865631262>'
            rune2_name = 'Legend: Bloodline'
        elif rune2 == zombie_ward:
            rune2 = '<:zombieward:792456100011573278>'
            rune2_name = 'Zombie Ward'
        elif rune2 == ghost_poro:
            rune2 = '<:ghostporo:792456099886399488>'
            rune2_name = 'Ghost Poro'
        elif rune2 == eyeball:
            rune2 = '<:eyeball:792456099709452338>'
            rune2_name = 'Eyeball Collection'
        elif rune2 == transcendence:
            rune2 = '<:transcendence:792454318422753311>'
            rune2_name = 'Transcendence'
        elif rune2 == celarity:
            rune2 = '<:celarity:792454317877493810>'
            rune2_name = 'Celarity'
        elif rune2 == focus:
            rune2 = '<:focus:792454317571440662>'
            rune2_name = 'Absolute Focus'
        elif rune2 == conditioning:
            rune2 = '<:conditioning:792457267990495304>'
            rune2_name = 'Conditioning'
        elif rune2 == second_wind:
            rune2 = '<:secondwind:792457268624490556>'
            rune2_name = 'Second Wind'
        elif rune2 == boneplating:
            rune2 = '<:boneplating:792457267932692511>'
            rune2_name = 'Bone Plating'
        elif rune2 == future:
            rune2 = '<:future:792458707467894794>'
            rune2_name = "Future's Market"
        elif rune2 == minion:
            rune2 = '<:minion:792458707295535136>'
            rune2_name = 'Minion Dematerializer'
        elif rune2 == biscuit:
            rune2 = '<:biscuit:792458706511069254>'
            rune2_name = 'Biscuit Delivery'
        else:
            rune2 = '**Not Found**'
            rune2_name = ' 404'

        rune3 = soup_.find_all('div', {'class': 'perk-page__item--active'})[3].find('img').attrs['src']
        rune3_name = ''
        if rune3 == coup:
            rune3 = '<:coup:792430510512406619>'
            rune3_name = 'Coup de Grace'
        elif rune3 == cut_down:
            rune3 = '<:cutdown:792430510806007838>'
            rune3_name = 'Cut Down'
        elif rune3 == last_stand:
            rune3 = '<:laststand:792430510390509570>'
            rune3_name = 'Last Stand'
        elif rune3 == ravenous:
            rune3 = '<:ravenous:792455662692073472>'
            rune3_name = 'Ravenous Hunter'
        elif rune3 == ingenious:
            rune3 = '<:ingenious:792455662604648448>'
            rune3_name = 'Ingenious Hunter'
        elif rune3 == relentless:
            rune3 = '<:relentless:792455662595866654>'
            rune3_name = 'Relentless Hunter'
        elif rune3 == ultimate:
            rune3 = '<:ultimate:792455662659567647>'
            rune3_name = 'Ultimate Hunter'
        elif rune3 == scorch:
            rune3 = '<:scorch:792454318317633586>'
            rune3_name = 'Scorch'
        elif rune3 == water_walking:
            rune3 = '<:waterwalking:792454318028619814>'
            rune3_name = 'Waterwalking'
        elif rune3 == gathering_storm:
            rune3 = '<:gatheringstorm:792454317915373568>'
            rune3_name = 'Gathering Storm'
        elif rune3 == overgrowth:
            rune3 = '<:overgrowth:792457268293664779>'
            rune3_name = 'Overgrowth'
        elif rune3 == revitalize:
            rune3 = '<:revitalize:792457268507312148>'
            rune3_name = 'Revitalize'
        elif rune3 == unflinching:
            rune3 = '<:unflinching:792457268499054631>'
            rune3_name = 'Unflinching'
        elif rune3 == cosmic:
            rune3 = '<:cosmic:792458706646073384>'
            rune3_name = 'Cosmic Insight'
        elif rune3 == approach_velocity:
            rune3 = '<:approachvelocity:792458706468995103>'
            rune3_name = 'Approach Velocity'
        elif rune3 == timewarp:
            rune3 = '<:timewarp:792458707023691776>'
            rune3_name = 'Time Warp Tonic'
        else:
            rune3 = '**Not Found**'
            rune3_name = ' 404'

        rune_tree_2 = soup_.find_all('div', {'class': 'perk-page__item--mark'})[1].find('img').attrs['src']
        tree_name2 = ''
        if rune_tree_2 == precision_tree:
            rune_tree_2 = '<:precision:792162680369971261>'
            tree_name2 = 'Precision'
        elif rune_tree_2 == domination_tree:
            rune_tree_2 = '<:domination:792414255214493716>'
            tree_name2 = 'Domination'
        elif rune_tree_2 == sorcery_tree:
            rune_tree_2 = '<:sorcery:792441210152288256>'
            tree_name2 = 'Sorcery'
        elif rune_tree_2 == resolve_tree:
            rune_tree_2 = '<:resolve:792421207949312020>'
            tree_name2 = 'Resolve'
        elif rune_tree_2 == inspiration_tree:
            rune_tree_2 = '<:inspiration:792420733887709224>'
            tree_name2 = 'Inspiration'
        else:
            rune_tree_2 = 'Not Found'
            tree_name2 = ' 404'

        secondary1 = soup_.find_all('div', {'class': 'perk-page__item--active'})[4].find('img').attrs['src']
        secondary1_name = ''
        if secondary1 == overheal:
            secondary1 = '<:overheal:792426715120140288>'
            secondary1_name = 'Overheal'
        elif secondary1 == triumph:
            secondary1 = '<:triumph1:792426714973208597>'
            secondary1_name = 'Triumph'
        elif secondary1 == pom:
            secondary1 = '<:pom:792426715217002526>'
            secondary1_name = 'Presence of Mind'
        elif secondary1 == cheapshot:
            secondary1 = '<:cheapshot:792442972620455947>'
            secondary1_name = 'Cheap Shot'
        elif secondary1 == tob:
            secondary1 = '<:tob:792442972855074826>'
            secondary1_name = 'Taste of Blood'
        elif secondary1 == sudden_impact:
            secondary1 = '<:suddenimpact:792442972875653140>'
            secondary1_name = 'Sudden Impact'
        elif secondary1 == orb:
            secondary1 = '<:orb:792454318623555594>'
            secondary1_name = 'Nullifying Orb'
        elif secondary1 == manaflow:
            secondary1 = '<:manaflow:792454318032420874>'
            secondary1_name = 'Manaflow Band'
        elif secondary1 == nimbus:
            secondary1 = '<:nimbus:792454318191149136>'
            secondary1_name = 'Nimbus Cloak'
        elif secondary1 == demolish:
            secondary1 = '<:demolish:792457268523696128>'
            secondary1_name = 'Demolish'
        elif secondary1 == font_of_life:
            secondary1 = '<:fontoflife:792457268100202527>'
            secondary1_name = 'Font of Life'
        elif secondary1 == shield_bash:
            secondary1 = '<:shieldbash:792457268637204490>'
            secondary1_name = 'Shield Bash'
        elif secondary1 == hexflash:
            secondary1 = '<:hexflash:792458707744980993>'
            secondary1_name = 'Hexflash Flashtraption'
        elif secondary1 == footwear:
            secondary1 = '<:footwear:792458707794788372>'
            secondary1_name = 'Magical Footwear'
        elif secondary1 == stopwatch:
            secondary1 = '<:stopwatch1:792458707509968936>'
            secondary1_name = 'Perfect Timing'
        elif secondary1 == alacrity:
            secondary1 = '<:alacrity:792429210035159073>'
            secondary1_name = 'Legend: Alacrity'
        elif secondary1 == tenacity:
            secondary1 = '<:tenacity:792429212383969311>'
            secondary1_name = 'Legend: Tenacity'
        elif secondary1 == bloodline:
            secondary1 = '<:bloodline:792429210865631262>'
            secondary1_name = 'Legend: Bloodline'
        elif secondary1 == zombie_ward:
            secondary1 = '<:zombieward:792456100011573278>'
            secondary1_name = 'Zombie Ward'
        elif secondary1 == ghost_poro:
            secondary1 = '<:ghostporo:792456099886399488>'
            secondary1_name = 'Ghost Poro'
        elif secondary1 == eyeball:
            secondary1 = '<:eyeball:792456099709452338>'
            secondary1_name = 'Eyeball Collection'
        elif secondary1 == transcendence:
            secondary1 = '<:transcendence:792454318422753311>'
            secondary1_name = 'Transcendence'
        elif secondary1 == celarity:
            secondary1 = '<:celarity:792454317877493810>'
            secondary1_name = 'Celarity'
        elif secondary1 == focus:
            secondary1 = '<:focus:792454317571440662>'
            secondary1_name = 'Absolute Focus'
        elif secondary1 == conditioning:
            secondary1 = '<:conditioning:792457267990495304>'
            secondary1_name = 'Conditioning'
        elif secondary1 == second_wind:
            secondary1 = '<:secondwind:792457268624490556>'
            secondary1_name = 'Second Wind'
        elif secondary1 == boneplating:
            secondary1 = '<:boneplating:792457267932692511>'
            secondary1_name = 'Bone Plating'
        elif secondary1 == future:
            secondary1 = '<:future:792458707467894794>'
            secondary1_name = "Future's Market"
        elif secondary1 == minion:
            secondary1 = '<:minion:792458707295535136>'
            secondary1_name = 'Minion Dematerializer'
        elif secondary1 == biscuit:
            secondary1 = '<:biscuit:792458706511069254>'
            secondary1_name = 'Biscuit Delivery'
        elif secondary1 == coup:
            secondary1 = '<:coup:792430510512406619>'
            secondary1_name = 'Coup de Grace'
        elif secondary1 == cut_down:
            secondary1 = '<:cutdown:792430510806007838>'
            secondary1_name = 'Cut Down'
        elif secondary1 == last_stand:
            secondary1 = '<:laststand:792430510390509570>'
            secondary1_name = 'Last Stand'
        elif secondary1 == ravenous:
            secondary1 = '<:ravenous:792455662692073472>'
            secondary1_name = 'Ravenous Hunter'
        elif secondary1 == ingenious:
            secondary1 = '<:ingenious:792455662604648448>'
            secondary1_name = 'Ingenious Hunter'
        elif secondary1 == relentless:
            secondary1 = '<:relentless:792455662595866654>'
            secondary1_name = 'Relentless Hunter'
        elif secondary1 == ultimate:
            secondary1 = '<:ultimate:792455662659567647>'
            secondary1_name = 'Ultimate Hunter'
        elif secondary1 == scorch:
            secondary1 = '<:scorch:792454318317633586>'
            secondary1_name = 'Scorch'
        elif secondary1 == water_walking:
            secondary1 = '<:waterwalking:792454318028619814>'
            secondary1_name = 'Waterwalking'
        elif secondary1 == gathering_storm:
            secondary1 = '<:gatheringstorm:792454317915373568>'
            secondary1_name = 'Gathering Storm'
        elif secondary1 == overgrowth:
            secondary1 = '<:overgrowth:792457268293664779>'
            secondary1_name = 'Overgrowth'
        elif secondary1 == revitalize:
            secondary1 = '<:revitalize:792457268507312148>'
            secondary1_name = 'Revitalize'
        elif secondary1 == unflinching:
            secondary1 = '<:unflinching:792457268499054631>'
            secondary1_name = 'Unflinching'
        elif secondary1 == cosmic:
            secondary1 = '<:cosmic:792458706646073384>'
            secondary1_name = 'Cosmic Insight'
        elif secondary1 == approach_velocity:
            secondary1 = '<:approachvelocity:792458706468995103>'
            secondary1_name = 'Approach Velocity'
        elif secondary1 == timewarp:
            secondary1 = '<:timewarp:792458707023691776>'
            secondary1_name = 'Time Warp Tonic'
        else:
            rune_tree_2 = 'Not Found'
            tree_name2 = ' 404'

        secondary2 = soup_.find_all('div', {'class': 'perk-page__item--active'})[5].find('img').attrs['src']
        secondary2_name = ''
        if secondary2 == overheal:
            secondary2 = '<:overheal:792426715120140288>'
            secondary2_name = 'Overheal'
        elif secondary2 == triumph:
            secondary2 = '<:triumph1:792426714973208597>'
            secondary2_name = 'Triumph'
        elif secondary2 == pom:
            secondary2 = '<:pom:792426715217002526>'
            secondary2_name = 'Presence of Mind'
        elif secondary2 == cheapshot:
            secondary2 = '<:cheapshot:792442972620455947>'
            secondary2_name = 'Cheap Shot'
        elif secondary2 == tob:
            secondary2 = '<:tob:792442972855074826>'
            secondary2_name = 'Taste of Blood'
        elif secondary2 == sudden_impact:
            secondary2 = '<:suddenimpact:792442972875653140>'
            secondary2_name = 'Sudden Impact'
        elif secondary2 == orb:
            secondary2 = '<:orb:792454318623555594>'
            secondary2_name = 'Nullifying Orb'
        elif secondary2 == manaflow:
            secondary2 = '<:manaflow:792454318032420874>'
            secondary2_name = 'Manaflow Band'
        elif secondary2 == nimbus:
            secondary2 = '<:nimbus:792454318191149136>'
            secondary2_name = 'Nimbus Cloak'
        elif secondary2 == demolish:
            secondary2 = '<:demolish:792457268523696128>'
            secondary2_name = 'Demolish'
        elif secondary2 == font_of_life:
            secondary2 = '<:fontoflife:792457268100202527>'
            secondary2_name = 'Font of Life'
        elif secondary2 == shield_bash:
            secondary2 = '<:shieldbash:792457268637204490>'
            secondary2_name = 'Shield Bash'
        elif secondary2 == hexflash:
            secondary2 = '<:hexflash:792458707744980993>'
            secondary2_name = 'Hexflash Flashtraption'
        elif secondary2 == footwear:
            secondary2 = '<:footwear:792458707794788372>'
            secondary2_name = 'Magical Footwear'
        elif secondary2 == stopwatch:
            secondary2 = '<:stopwatch1:792458707509968936>'
            secondary2_name = 'Perfect Timing'
        elif secondary2 == alacrity:
            secondary2 = '<:alacrity:792429210035159073>'
            secondary2_name = 'Legend: Alacrity'
        elif secondary2 == tenacity:
            secondary2 = '<:tenacity:792429212383969311>'
            secondary2_name = 'Legend: Tenacity'
        elif secondary2 == bloodline:
            secondary2 = '<:bloodline:792429210865631262>'
            secondary2_name = 'Legend: Bloodline'
        elif secondary2 == zombie_ward:
            secondary2 = '<:zombieward:792456100011573278>'
            secondary2_name = 'Zombie Ward'
        elif secondary2 == ghost_poro:
            secondary2 = '<:ghostporo:792456099886399488>'
            secondary2_name = 'Ghost Poro'
        elif secondary2 == eyeball:
            secondary2 = '<:eyeball:792456099709452338>'
            secondary2_name = 'Eyeball Collection'
        elif secondary2 == transcendence:
            secondary2 = '<:transcendence:792454318422753311>'
            secondary2_name = 'Transcendence'
        elif secondary2 == celarity:
            secondary2 = '<:celarity:792454317877493810>'
            secondary2_name = 'Celarity'
        elif secondary2 == focus:
            secondary2 = '<:focus:792454317571440662>'
            secondary2_name = 'Absolute Focus'
        elif secondary2 == conditioning:
            secondary2 = '<:conditioning:792457267990495304>'
            secondary2_name = 'Conditioning'
        elif secondary2 == second_wind:
            secondary2 = '<:secondwind:792457268624490556>'
            secondary2_name = 'Second Wind'
        elif secondary2 == boneplating:
            secondary2 = '<:boneplating:792457267932692511>'
            secondary2_name = 'Bone Plating'
        elif secondary2 == future:
            secondary2 = '<:future:792458707467894794>'
            secondary2_name = "Future's Market"
        elif secondary2 == minion:
            secondary2 = '<:minion:792458707295535136>'
            secondary2_name = 'Minion Dematerializer'
        elif secondary2 == biscuit:
            secondary2 = '<:biscuit:792458706511069254>'
            secondary2_name = 'Biscuit Delivery'
        elif secondary2 == coup:
            secondary2 = '<:coup:792430510512406619>'
            secondary2_name = 'Coup de Grace'
        elif secondary2 == cut_down:
            secondary2 = '<:cutdown:792430510806007838>'
            secondary2_name = 'Cut Down'
        elif secondary2 == last_stand:
            secondary2 = '<:laststand:792430510390509570>'
            secondary2_name = 'Last Stand'
        elif secondary2 == ravenous:
            secondary2 = '<:ravenous:792455662692073472>'
            secondary2_name = 'Ravenous Hunter'
        elif secondary2 == ingenious:
            secondary2 = '<:ingenious:792455662604648448>'
            secondary2_name = 'Ingenious Hunter'
        elif secondary2 == relentless:
            secondary2 = '<:relentless:792455662595866654>'
            secondary2_name = 'Relentless Hunter'
        elif secondary2 == ultimate:
            secondary2 = '<:ultimate:792455662659567647>'
            secondary2_name = 'Ultimate Hunter'
        elif secondary2 == scorch:
            secondary2 = '<:scorch:792454318317633586>'
            secondary2_name = 'Scorch'
        elif secondary2 == water_walking:
            secondary2 = '<:waterwalking:792454318028619814>'
            secondary2_name = 'Waterwalking'
        elif secondary2 == gathering_storm:
            secondary2 = '<:gatheringstorm:792454317915373568>'
            secondary2_name = 'Gathering Storm'
        elif secondary2 == overgrowth:
            secondary2 = '<:overgrowth:792457268293664779>'
            secondary2_name = 'Overgrowth'
        elif secondary2 == revitalize:
            secondary2 = '<:revitalize:792457268507312148>'
            secondary2_name = 'Revitalize'
        elif secondary2 == unflinching:
            secondary2 = '<:unflinching:792457268499054631>'
            secondary2_name = 'Unflinching'
        elif secondary2 == cosmic:
            secondary2 = '<:cosmic:792458706646073384>'
            secondary2_name = 'Cosmic Insight'
        elif secondary2 == approach_velocity:
            secondary2 = '<:approachvelocity:792458706468995103>'
            secondary2_name = 'Approach Velocity'
        elif secondary2 == timewarp:
            secondary2 = '<:timewarp:792458707023691776>'
            secondary2_name = 'Time Warp Tonic'
        else:
            rune_tree_2 = 'Not Found'
            tree_name2 = ' 404'

        em = discord.Embed(
            title=f"{champ} {role}",
            description=f"Statistics",
            color=discord.Color.red())
        em.set_thumbnail(url=thumbnail_url)
        em.add_field(name='Win-Rate', value=win_rate, inline=True)
        em.add_field(name='Champion Rank', value=champ_rank, inline=True)

        em.add_field(name='Pick-Rate', value=pick_rate, inline=False)

        em.add_field(name='Ban-Rate', value=ban_rate, inline=True)
        em.add_field(name='Matches', value=matches, inline=True)

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


        await ctx.send(embed=em)



def setup(client):
    client.add_cog(ChampionInfo(client))