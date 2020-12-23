import requests
import bs4

url = 'https://lolcounter.com/champions'

res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())
