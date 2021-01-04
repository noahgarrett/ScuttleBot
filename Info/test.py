from riotwatcher import LolWatcher, ApiError
from Bot.runes import *
REGION = 'na1'
summoner_ = 'Xsychgames'
API_KEY = 'RGAPI-e6d4480c-96de-4ea6-a822-5974777108f5'
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

def get_match_history():
    sum_id = get_summoner_id(summoner_)
    id = sum_id['accountId']
    match_list = LOL_WATCHER.match.matchlist_by_account(REGION, id)
    return match_list

def get_recent_matches():
    match_list = get_match_history()
    i = 0
    for match in match_list['matches']:
        if i == 5:
            break
        else:
            if i == 0:
                i += 1
                match1 = match
            elif i == 1:
                i += 1
                match2 = match
            elif i == 2:
                i += 1
                match3 = match
            elif i == 3:
                i += 1
                match4 = match
            elif i == 4:
                i += 1
                match5 = match

    return recent_matches


get_recent_matches()
print(match1, match2, match3, match4, match5)

# for i in free1:
#     print(i)



#print(current_champ_list['data']['Aatrox']['stats'])