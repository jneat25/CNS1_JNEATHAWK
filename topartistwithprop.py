import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
import csv
import sys


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope="user-top-read"))

results = sp.current_user_top_tracks(time_range='short_term', limit=1)
for i, item in enumerate(results['items']):
    song_id = item['id']
    features = sp.audio_features(song_id)
    energy = features[0]['energy']
    instrumental = features[0]['instrumentalness']
    dance = features[0]['danceability']
    artist = item['artists'][0]['name']
    print (item['name'], "|", item['artists'][0]['name'] ,"|",item['id'], "|", energy,"|", instrumental,"|", dance)




