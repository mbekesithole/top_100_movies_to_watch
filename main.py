import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
response.encoding = "utf-8"
empire_online_page = response.text

soup = BeautifulSoup(empire_online_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movies_list = [movie.getText() for movie in movies]
sorted_movies_list = movies_list[::-1]

with open("movies.txt", mode="w") as file:
    for movie in sorted_movies_list:
        file.write(f"{movie}\n")
