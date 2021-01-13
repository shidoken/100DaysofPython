import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# getting songs by billboard 100 by year

# year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = '2020-02-07'

# going to billboard top 100 and grabbing songs
response = requests.get('https://www.billboard.com/charts/hot-100/' + year)
result = response.text
soup = BeautifulSoup(result, "html.parser")

songs = soup.find_all('span', class_="chart-element__information__song")
artists = soup.find_all('span', class_="chart-element__information__artist")

song_list = [song.getText() for song in songs]

# spotify api and spotipy
user = 'shidoken'
id = os.environ.get('SPOT_CLIENT')
secret = os.environ.get('SPOT_SECRET')
scope = 'playlist-modify-private'
spotify_creds = SpotifyOAuth(
    client_id=id, client_secret=secret, redirect_uri='https://example.com',
    cache_path=".cache", scope=scope)
with open(".cache") as file:
    cache = file.read()
spotify = spotipy.Spotify(client_credentials_manager=spotify_creds)

# creating the song list of 100 songs
song_uris = []
for song in song_list:
    result = spotify.search(song, type='track')
    song_uris.append(result['tracks']['items'][0]['uri'])

# creating the playlist name
name_list = spotify.user_playlist_create(user, f"{year} Billboard 100")
playlist = spotify.user_playlists(user=user)
for dot in playlist['items']:
    if dot['name'] == name_list['name']:
        list_uri = dot['uri']

print(song_uris[0])
print("adding to playlist")
spotify.playlist_add_items(list_uri, song_uris)
