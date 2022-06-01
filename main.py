import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
features = sp.audio_features
results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx + 1, track['artists'][0]['name'], "–", track['name'], '-', features('danceability'))