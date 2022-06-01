import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
credentials = json.load(open('authorization.json', encoding="utf8"))
client_id = credentials['client_id']
client_secret = credentials['client_secret']

playlist_index = 0

playlists = json.load(open('playlists_like_dislike.json', encoding="utf8"))
playlist_uri = playlists[playlist_index]['uri']
like = playlists[playlist_index]['like']

