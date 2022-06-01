import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url))
reccomend = sp.recommendations(seed_tracks='464C9LimEzfjihNJvzwHlH', limit=1)
