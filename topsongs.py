import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
results = (sp.current_user_top_tracks(limit=10,offset=0,time_range='short_term'))
for idx, item in enumerate(results['items']):
        print(idx + 1, item['name'], '-', item['artists'][0]['name'], '-', item['album']['name'],'-',item['duration_ms'])
print()
