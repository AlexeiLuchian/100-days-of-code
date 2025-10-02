from bs4 import BeautifulSoup
import requests

yc_url = "https://news.ycombinator.com/news"

response = requests.get(url=yc_url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
a_tags = soup.select('span.titleline>a')

titles = []
links = []

for tag in a_tags:
    titles.append(tag.getText())
    links.append(tag.get("href"))

print(titles)
print(links)