from riotwatcher import LolWatcher, ApiError
from Bot.runes import *
REGION = 'na1'
summoner_ = 'Xsychgames'
API_KEY = 'RGAPI-2a69c73a-5965-47e1-ac3c-92df1b9e5fdf'
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

r_ids = get_champ_rotation()
champ_list = get_champ_list()


for id in r_ids:
    for champ in champ_list['data']:
        key = champ_list['data'][champ]['key']
        if key == str(id):
            print(champ)
        # print(champ_list['data'][champ]['key'])

# for i in free1:
#     print(i)



#print(current_champ_list['data']['Aatrox']['stats'])