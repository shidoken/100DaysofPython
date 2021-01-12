import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
result = response.text
soup = BeautifulSoup(result, "html.parser")

movie_title = [movie.string for movie in soup.find_all("h3", class_="title")]
movie_title.reverse()
movie_title[0] = "1) The Godfather"
for movie in movie_title:
    with open("movie.txt", "a") as data:
        data.write(movie+"\r")