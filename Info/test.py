from riotwatcher import LolWatcher, ApiError
from Bot.runes import *
REGION = 'na1'
summoner_ = 'Xsychgames'
API_KEY = 'RGAPI-4da05ce5-bc28-4d59-aef1-1caa5d246a91'
LOL_WATCHER = LolWatcher(API_KEY)

# me = LOL_WATCHER.summoner.by_name(REGION, 'Xsychgames')
#
# personal = LOL_WATCHER.league.by_summoner(REGION, me['id'])
#
# print(personal[0]['tier'])


# versions = LOL_WATCHER.data_dragon.versions_for_region(REGION)
# champ_version = versions['n']['champion']
# current_champ_list = LOL_WATCHER.data_dragon.champions(champ_version)

# current_champ_list = main.get_champ_list()
# random_index = random.randint(0, 153)
#
# random_champion = current_champ_list['data'][random_index]

# free = LOL_WATCHER.champion.rotations(REGION)
# free1 = free['freeChampionIds']

def get_champ_list():
    versions = LOL_WATCHER.data_dragon.versions_for_region(REGION)
    champ_version = versions['n']['champion']
    current_champ_list = LOL_WATCHER.data_dragon.champions(champ_version)
    return current_champ_list

def get_champ_rotation():
    rotation_json = LOL_WATCHER.champion.rotations(REGION)
    r_ids = rotation_json['freeChampionIds']
    return r_ids

# r_ids = get_champ_rotation()
# champ_list = get_champ_list()

def get_summoner_id(summoner):
    sum_id = LOL_WATCHER.summoner.by_name(REGION, summoner)
    return sum_id

def get_summoner_mastery():
    sum_id = get_summoner_id(summoner_)
    id = sum_id['id']
    mastery = LOL_WATCHER.champion_mastery.by_summoner(REGION, id)
    return mastery

i = get_summoner_id(summoner_)
m = get_summoner_mastery()

print(i)

# for i in free1:
#     print(i)



#print(current_champ_list['data']['Aatrox']['stats'])