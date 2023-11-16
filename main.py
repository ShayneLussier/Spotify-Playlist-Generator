import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Enter a year (down to 2006): ")

URL = f"https://www.billboard.com/charts/year-end/{date}/hot-100-songs/"
SPOTIPY_CLIENT_ID = "___"
SPOTIPY_CLIENT_SECRET = "___"
SPOTIFY_USERNAME = "___"

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
    if '&' in artist:
        name = (artist.getText().strip()).split('&')
        top_100_artists.append(name[0])
    elif 'Featuring' in artist:
        name.split("Featuring")
        top_100_artists.append(name[0])
    elif 'FEATURING' in artist:
        name.split("FEAUTURING")
        top_100_artists.append(name[0])
    elif 'X' in artist:
        name.split("X")
        top_100_artists.append(name[0])
    else:
        name = (artist.getText().strip())
        top_100_artists.append(name[0])

# print(top_100_artists)
top_100_dict = {k: v for k, v in zip(top_100_title, top_100_artists)}
# print(top_100_dict)

# -------------------------------------------------------- SPOTIFY AUTHENTIFICATION ---------------------------------------------------- #

auth = SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME,
    )
sp = spotipy.Spotify(auth_manager=auth)

user = sp.current_user()
user_id = user["id"]

# ------------------------------------------------- CREATE PLAYLIST -------------------------------------------------------------- #

song_links = []

for k, v in top_100_dict.items():
    result = sp.search(q=f"track:{k} artist:{v} year:{date}", type="track")
    try:
        uri = result['tracks']['items'][0]["uri"]
        song_links.append(uri)
        print(result)
    except IndexError:
        print("Song doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_links)