import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Computer_chess")
soup = bs4.BeautifulSoup(result.text,'lxml')
image_grabber = soup.select('.thumbimage')[0]
image_url = "https:"+image_grabber['src']
image_link =requests.get(image_url)

f = open("newimage.jpg",'wb')
f.write(image_link.content)
f.close()


