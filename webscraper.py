import requests
import bs4

url = 'https://lolcounter.com/champions'

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'lxml')

champion = soup.find_all('div', {'class': 'champions'})[0].find('a').text

print(champion)
