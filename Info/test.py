from riotwatcher import LolWatcher, ApiError
from Bot.runes import *
import main
REGION = 'na1'
summoner_ = 'Xsychgames'
API_KEY = 'RGAPI-fb223604-73fb-4af6-bdaf-6e4070bc2bf3'
LOL_WATCHER = LolWatcher(API_KEY)

# me = LOL_WATCHER.summoner.by_name(REGION, 'Xsychgames')
#
# personal = LOL_WATCHER.league.by_summoner(REGION, me['id'])
#
# print(personal[0]['tier'])


# versions = LOL_WATCHER.data_dragon.versions_for_region(REGION)
# champ_version = versions['n']['champion']
# current_champ_list = LOL_WATCHER.data_dragon.champions(champ_version)

current_champ_list = main.get_champ_list()
random_index = random.randint(0, 153)

random_champion = current_champ_list['data'][random_index]

print(random_champion)


#print(current_champ_list['data']['Aatrox']['stats'])