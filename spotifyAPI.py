
# requesting data and converting api info to base64
import requests
import json
import base64

# display popup to auth
import webbrowser

# detect url from pop up window
from pywinauto import Application
from pywinauto.findwindows import find_windows

# debugging
import time
import pprint



# TODO turn into secrets
clientId = ''
clientSecret = ''
callbackURL = 'https://example.com/callback/'





'''

ENDPOINTS
https://developer.spotify.com/documentation/web-api/reference/

'''




# auth scopes
scopes = [
 'ugc-image-upload',
 'user-read-recently-played',
 'user-top-read',
 'user-read-playback-position',
 'user-read-playback-state',
 'user-modify-playback-state',
 'user-read-currently-playing',
 'app-remote-control',
 'streaming',
 'playlist-modify-public',
 'playlist-modify-private',
 'playlist-read-private',
 'playlist-read-collaborative',
 'user-follow-modify',
 'user-follow-read',
 'user-library-modify',
 'user-library-read',
 'user-read-email',
 'user-read-private'
]
full_permission = ''
for i in scopes:
    full_permission += i + ' '




#  Authorization by getting token
def authorize_spotify_NO_USER():
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')

    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "authorization_code"


    r = requests.post(url, headers=headers, data=data).json()

    token = r['access_token']
    return token
def authorize_spotify_IMPLICIT(): # sleeps for 3 seconds and detects open chrome window

    headers = {
        'client_id' : clientId,
        'response_type' : 'token',
        'redirect_uri' : callbackURL,
        'scope' : full_permission,
    }

    # open url on browser
    url = f"https://accounts.spotify.com/authorize?client_id={headers['client_id']}&response_type={headers['response_type']}&redirect_uri={headers['redirect_uri']}&scope={headers['scope']}"
    browser = webbrowser.open(url, new=1)





    # detect url from open apps
    # find_windows(best_match='chrome')
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*")
    dlg = app.top_window()
    url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()

    # get auth code after user accepts
    auth_code_token =  url.split("=")[1].split("&")[0] 


    return auth_code_token
def authorize_spotify_REFRESHABLE(): # sleeps for 3 seconds and detects open chrome window

    headers = {
        'client_id' : clientId,
        'response_type' : 'code',
        'redirect_uri' : callbackURL,
        'scope' : full_permission,
    }

    # open url on browser
    url = f"https://accounts.spotify.com/authorize?client_id={headers['client_id']}&response_type={headers['response_type']}&redirect_uri={headers['redirect_uri']}&scope={headers['scope']}"
    browser = webbrowser.open(url, new=1)





    # detect url from open apps
    # find_windows(best_match='chrome')
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*")
    dlg = app.top_window()
    url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()

    # get auth code after user accepts
    auth_code  =  url.split("?")[1].split("=")[1] 



    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')

    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "authorization_code"
    data['code'] = auth_code
    data['redirect_uri'] = callbackURL



    r = requests.post(url, headers=headers, data=data).json()
    token = r['access_token']
    return token





# endpoints
def user_profile(token):
    playlistUrl = f"https://api.spotify.com/v1/me"
    headers = {"Authorization": "Bearer " + token}
    res = requests.get(url=playlistUrl, headers=headers).json()
    return res

def user_likes(token):
    playlistUrl = f"https://api.spotify.com/v1/me/tracks"
    headers = {"Authorization": "Bearer " + token}
    
    
    results = requests.get(url=playlistUrl, headers=headers).json()
    all_songs = []
    totalLikedSongs = int(results['total'])
    while results:   # LOOKUP SONGS
        for idx, item in enumerate(results['items']):
            track = item['track']
            all_songs.append( (track['artists'][0]['name'], track['name'] , track['id'] , track['popularity']) )

        if results['next']: #next page check
            results = requests.get(url=results['next'], headers=headers).json()
        else:
            results = None

    return all_songs
def user_albums(token):
    playlistUrl = f"https://api.spotify.com/v1/me/albums"
    headers = {"Authorization": "Bearer " + token}
    results = requests.get(url=playlistUrl, headers=headers).json()

    all_albums = {}
    count = 0
    while results:   # LOOKUP SONGS
        for item in results['items']:
            album = item['album']
            all_albums[count] =  {
                'album_name' : item['album']['name'],
                "genres" : album['genres'],
                "id" : album['id'],
                "popularity" : album['popularity'],
                "songs" : [],
            }
            for track in item['album']['tracks']['items']:
                all_albums[count]['songs'].append(   (track['id'] , track['name'])   )
            count += 1

        if results['next']: #next page check
            results = requests.get(url=results['next'], headers=headers).json()
        else:
            results = None
    return all_albums
def user_playlists(token):
    playlistUrl = f"https://api.spotify.com/v1/me/playlists"
    headers = {"Authorization": "Bearer " + token}
    results = requests.get(url=playlistUrl, headers=headers).json()

    all_playlists = {}
    count = 0
    # EVERY PLAYLIST
    while results:   
        for item in results['items']:
            all_playlists[count] =  {
                'owner' : item['owner']['display_name'],
                'playlist_name' : item['name'],
                "description" : item['description'],
                "id" : item['id'],
                "songs" : [],
            }

            # LOOKUP SONGS
            pl_tracks_call = requests.get(url=item['tracks']['href'] , headers = headers).json()
            while pl_tracks_call:
                for track in pl_tracks_call['items']:
                    all_playlists[count]['songs'].append(   (track['track']['id'] , track['track']['name'])   )
            
                # PAGINATION [TRACKS]
                if pl_tracks_call['next']:
                    pl_tracks_call = requests.get(url=pl_tracks_call['next'] , headers = headers).json()
                else:
                    pl_tracks_call = None
            
            count += 1

         # PAGINATION [PLAYLISTS]
        if results['next']:
            results = requests.get(url=item['next'] , headers = headers).json()
        else:
            results = None
    return all_playlists




# handmade api requests

# AUTHORIZE
# token = authorize_spotify_NO_USER()
# token = authorize_spotify_IMPLICIT()
token = authorize_spotify_REFRESHABLE()




# ENDPOINTS

user_info = user_profile(token)
likes = user_likes(token)
albums = user_albums(token)
playlists = user_playlists(token)


# output
print(user_info.keys())
print(likes)
print(albums.keys())
print(playlists.keys())
