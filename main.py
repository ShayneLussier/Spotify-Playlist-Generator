import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/year-end/2022/hot-100-songs/"

# ------------------------------------------------ WEB SCRAPING ---------------------------------------------------- #

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story")

top_100_title = []
for song in songs:
    title = (song.getText().strip())
    top_100_title.append(title)


top_100_artists = []
artist_1 = soup.find(name="span", class_="c-label a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block u-font-size-20@tablet").getText().strip()
top_100_artists.append(artist_1)

artists_rest = soup.find_all(name="span", class_="c-label a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block")
for artist in artists_rest:
    name = (artist.getText().strip())
    top_100_artists.append(name)

top_100_dict = {k: v for k, v in zip(top_100_title, top_100_artists)}
print(top_100_dict)