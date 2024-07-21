import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from apikey import API_KEY, CLIENT_ID, REDIRECT_URI
import ui
scope = "playlist-read-private"
auth_manager = SpotifyOAuth(client_id=CLIENT_ID, 
                                        client_secret=API_KEY, 
                                        scope=scope, 
                                        redirect_uri=REDIRECT_URI)

sp = spotipy.Spotify(auth_manager=auth_manager)

# load user playlist into dict: key = name val = id
playlists = sp.current_user_playlists()
playlist_dict = {}
while playlists:
    for i, playlist in enumerate(playlists['items']):
        playlist_dict[playlist['name']] = playlist['id']
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None


test_playlist = 'Trap playlist'
id = playlist_dict[test_playlist]
test_playlist_songs = sp.playlist_tracks(playlist_id=id)

ui.UI_Loop(list(playlist_dict.keys()))
quit()
for idx, song in enumerate(test_playlist_songs['items']):
    name = song['track']['name']
    artists_dict = song['track']['artists']
    artists = []
    for artist in artists_dict:
        artists.append(artist['name'])
    print(name + ": " + ", ".join(artists))
  