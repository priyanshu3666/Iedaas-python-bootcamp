import requests
import bs4
result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(result.text,'lxml')
first_item  = soup.select('.toctext')
print()
print("the content of table of wikipedia file of Grace Hopper page\n")

for item in first_item :
    print(f'\t {item.getText()}')