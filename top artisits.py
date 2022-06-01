import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
scope = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))

top_5 = sp.current_user_top_tracks(limit=5, offset=0, time_range='medium_term')
for idx, item in enumerate(top_5['items']):
    track = item['track']
    print(idx + 1, track['artists'][0]['name'], " – ", track['name'])