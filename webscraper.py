import requests
import bs4


url = 'https://na.op.gg/champion/nasus/statistics'

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'lxml')

rune_tree = soup.find_all('div', {'class': 'perk-page__row'})[0].find('img').attrs['src']
keystone = soup.find_all('div', {'class': 'perk-page__item--active'})[0].find('img').attrs['src']
rune1 = soup.find_all('div', {'class': 'perk-page__item--active'})[1].find('img').attrs['src']
secondary = soup.find_all('div', {'class': 'perk-page__item--active'})[5].find('img').attrs['src']
rune_tree_2 = soup.find_all('div', {'class': 'perk-page__item--mark'})[1].find('img').attrs['src']
print(rune_tree_2)
