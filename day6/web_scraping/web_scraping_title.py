import requests
import bs4
result = requests.get("http://www.example.com")
print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text,"lxml")
title_ = soup.select('title')[0].getText()
paragragh_text = soup.select('p')[0].getText()
print(soup)
print(title_)
print()
print(paragragh_text)