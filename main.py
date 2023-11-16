import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/year-end/2022/hot-100-songs/"

# ------------------------------------------------ WEB SCRAPING ---------------------------------------------------- #

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story")

top_100_list = []
for song in songs:
    title = (song.getText().strip())
    top_100_list.append(title)

print(top_100_list)