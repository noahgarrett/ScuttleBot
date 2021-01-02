import requests
import bs4
from Bot.runes import *


url = 'https://na.op.gg/champion/akali/statistics/mid'
moba_url = 'https://champion.gg/champion/Nasus/Top'
tier_url = 'https://tierlist.gg/jungle-tier-list'

response = requests.get(url)
# moba_response = requests.get(moba_url)
# tier_response = requests.get(tier_url)

soup = bs4.BeautifulSoup(response.text, 'lxml')
# moba_soup = bs4.BeautifulSoup(response.text, 'lxml')
# tier_soup = bs4.BeautifulSoup(tier_response.text, 'lxml')

# rune_tree = soup.find_all('div', {'class': 'perk-page__row'})[0].find('img').attrs['src']
# keystone = soup.find_all('div', {'class': 'perk-page__item--active'})[0].find('img').attrs['src']
# rune1 = soup.find_all('div', {'class': 'perk-page__item--active'})[1].find('img').attrs['src']
# secondary = soup.find_all('div', {'class': 'perk-page__item--active'})[5].find('img').attrs['src']
# rune_tree_2 = soup.find_all('div', {'class': 'perk-page__item--mark'})[1].find('img').attrs['src']
# win_rate = soup.find_all('div', {'class': 'champion-stats-trend-rate'})[0].text
#
# champ_name = soup.find_all('h1', {'class': 'champion-stats-header-info__name'})[0].text

# .findAll[2] gets potion
# item = soup.find_all('ul', {'class': 'champion-stats__list'})[3].findAll('li')[2].find('img').attrs['src']

# Tier list
# tier = tier_soup.find_all('div', {'class': 'TierPage-Tier-Items'})[0].findAll('div', {'class': 'TierItem-Image'})[0].find('img').attrs['data-src']

# jungle_s_tier = []
# for i in range(0, 10):
#     try:
#         tier = tier_soup.find_all('div', {'class': 'TierPage-Tier-Items'})[0].findAll('div', {'class': 'TierItem-Image'})[i].find('img').attrs['alt']
#         jungle_s_tier.append(tier)
#         print(jungle_s_tier)
#     except:
#         break

# tier = tier_soup.find_all('a', {'class': 'TierItem'})[6].findAll('div', {'class': 'TierItem-Image'})[0].find('img').attrs['alt']
# print(tier)
# print(jungle_s_tier)

summoner_spell1 = soup.find_all('ul', {'class': 'champion-stats__list'})[0].findAll('li', {'class': 'champion-stats__list__item'})[0].find('img').attrs['src']

print(summoner_spell1)

# tier = tier_soup.find_all('div', {'class': 'TierPage-Tier-Items'})[0].findAll('div', {
#             'class': 'TierItem-Image'})[0].find('img').attrs['alt']
#
# print(tier)
