import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
client_id = 'ad117b49aa1d4c9488a204f3c1955687'
client_secret = '888da137894b43eab12b43d7851f7d80'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlistdata = sp.playlist_tracks("1UHFB1THL3XfmTJw4zhZqm")
for idx, item in enumerate(playlistdata['items']):
    track = item['track']
    print(idx + 1, track['artists'][0]['name'], " – ", track['name'])