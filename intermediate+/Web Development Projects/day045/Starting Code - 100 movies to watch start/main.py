import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, 'html.parser')

movies_headers = soup.find_all(name="h3", class_="title")
movie_titles = [title.getText() for title in movies_headers]

with open("movies.txt", 'a') as file:
    for i in range(len(movie_titles)-1,-1,-1):
        file.write(movie_titles[i]+"\n")