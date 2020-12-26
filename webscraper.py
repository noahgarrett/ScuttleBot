import requests
import bs4
from Bot.runes import *


url = 'https://na.op.gg/champion/nasus/statistics'

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'lxml')

rune_tree = soup.find_all('div', {'class': 'perk-page__row'})[0].find('img').attrs['src']
keystone = soup.find_all('div', {'class': 'perk-page__item--active'})[0].find('img').attrs['src']
rune1 = soup.find_all('div', {'class': 'perk-page__item--active'})[1].find('img').attrs['src']
secondary = soup.find_all('div', {'class': 'perk-page__item--active'})[5].find('img').attrs['src']
rune_tree_2 = soup.find_all('div', {'class': 'perk-page__item--mark'})[1].find('img').attrs['src']
win_rate = soup.find_all('div', {'class': 'champion-stats-trend-rate'})[0].text

for runes in primary_rune_tree_img:
    if rune_tree == primary_rune_tree_img[runes]:
        for tree in tree_names:
            if rune_tree == tree_names[tree]:
                for emoji in primary_rune_tree_emoji:
                    if rune_tree == primary_rune_tree_emoji[emoji]:
                        rune_tree = emoji
                        tree_name = tree
                        break

print(rune_tree, tree_name)