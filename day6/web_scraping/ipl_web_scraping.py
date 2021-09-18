import requests,bs4
base_url = 'https://www.iplt20.com/teams/men'
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text,'lxml')


product_title = soup.select('.card__title')
product_subtitle = soup.select('.card__subtitle')
product_year = soup.select('.team-card__wins')

title = []
venue = []
winning_year = []

for i in range(8):
    title.append(product_title[i].getText())
    venue.append(product_subtitle[i].getText().strip())
    if i< len(product_year):
        winning_year.append(product_year[i].getText().strip())
     
print(title)
print(venue)
print(winning_year)


