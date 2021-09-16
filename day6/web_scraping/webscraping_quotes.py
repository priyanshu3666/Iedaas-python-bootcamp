import bs4,requests
base_url = requests.get('https://quotes.toscrape.com/')
soup =bs4.BeautifulSoup(base_url.text,'lxml')
author_ = set()
for name in soup.select('.author'):
    author_.add(name.text)
print(author_)

quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)

print(quotes)

top_ten_tags =[]
for tag in soup.select('.tag-item'):
    top_ten_tags.append(tag.text.strip('\n'))

print(top_ten_tags)

url =  'https://quotes.toscrape.com/'


page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    page_url = url+str(page)
    
    res = requests.get(page_url)
    
    if "No quotes found!" in res.text:
        break
    soup = bs4.BeautifulSoup(res.text,'lxml')
    for name in soup.select(".author"):
        authors.add(name.text)
        
    page += 1

print(authors)