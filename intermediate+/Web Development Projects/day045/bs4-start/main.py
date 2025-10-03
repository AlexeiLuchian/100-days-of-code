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

span_scores = soup.find_all(name="span", class_="score")
scores_text = [score.getText() for score in span_scores]
scores = [int(score.split()[0]) for score in scores_text]

max_score = scores[0]
for i in range(1, len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]
        max_title = titles[i]
        max_link = links[i]

print(max_title)
print(max_link)
print(max_score)


# print(titles)
# print(links)
# print(scores)