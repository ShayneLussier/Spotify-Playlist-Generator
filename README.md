# Spotify-Playlist-Generator

Web scrape the Billboard's Top 100 end of year chart and create a Spotify playlist with all available songs.

## Usage

Prompts the user to choose a year to collect songs data. Billboard's charts are only available from 2006 to ...  
```python
while true:
    try:
        date = input("Enter a year (down to 2006): ")
        if int(date) > 2005:
            break
    except ValueError:
        print("Date should be above 2005!"))
```

Users need to enter their own Spotify-api credentials in the file or store them as .env variables.
```python
SPOTIPY_CLIENT_ID = "___"
SPOTIPY_CLIENT_SECRET = "___"
SPOTIFY_USERNAME = "___"
```

The Billboard charts may return artists and collaborators as one string. ex:
+ Elton John & Dua Lipa
+ Future Featuring Drake & Tems

Without splitting to find the main artist, only around 60% of the songs would be returned in the playlist. The following code returns over 90% of the songs, on the low end, to the playlist.
```
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
```
