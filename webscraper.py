import requests
import bs4
from Bot.runes import *


url = 'https://na.op.gg/champion/akali/statistics'
moba_url = 'https://champion.gg/champion/Nasus/Top'
tier_url = 'https://u.gg/lol/top-lane-tier-list'

# response = requests.get(url)
# moba_response = requests.get(moba_url)
tier_response = requests.get(tier_url)

# soup = bs4.BeautifulSoup(response.text, 'lxml')
# moba_soup = bs4.BeautifulSoup(response.text, 'lxml')
tier_soup = bs4.BeautifulSoup(tier_response.text, 'lxml')

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
tier = tier_soup.find_all('div', {'class': 'rt-tr-group'})
print(tier)