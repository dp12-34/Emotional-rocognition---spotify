from __future__ import print_function
from ast import Import
import requests
from urllib.parse import urlencode
import base64
import webbrowser
import spotipy
import settings

CLIENT_ID = '05009217d148447f917b83b98137bf69'
CLIENT_SECRET = '74c94b99efdd45ebb6fa01d1423c4172'
REDIRECT_URI = 'http://localhost:8000/callback/'
USER_PLAYLISTS_URL = 'https://api.spotify.com/v1/me/playlists'
AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize?'
CODE = 'AQC_56RK0ZUzL1kNNMyp8CW6qM3F7ELH2AQ51cu5CW2gkD4p8lsFutWgAhVfjBdc_rvqfdpi2EOLgNfH4ALRz0J5Jq'

sillyGoofyPlaylist = ['spotify:track:3xZek9XkEaX130o3XN9cvd', 'spotify:track:28UMEtwyUUy5u0UWOVHwiI', 'spotify:track:02JIdsrod3BYucThfUFDUX', 'spotify:track:4Cd01GWLuMTNZhW0DE7cF4', 'spotify:track:1rKBOL9kJfX1Y4C3QaOvRH', 'spotify:track:3hSs17SMNlysCjVWkaJPFd']
happyPlaylist = ['spotify:track:463CkQjx2Zk1yXoBuierM9', 'spotify:track:0DiDStADDVh3SvAsoJAFMk', 'spotify:track:60APt5N2NRaKWf5xzJdzyC', 'spotify:track:57n3qOwXcoRMyGFjeqC1Rh', 'spotify:track:72Q0FQQo32KJloivv5xge2', 'spotify:track:0KKkJNfGyhkQ5aFogxQAPU', 'spotify:track:1rqqCSm0Qe4I9rUvWncaom', 'spotify:track:1V6gIisPpYqgFeWbMLI0bA', 'spotify:track:76hfruVvmfQbw0eYn1nmeC', 'spotify:track:1RUTIdTnFs8lHSc0Zr4UJB', 'spotify:track:3lB0GMiI5KxDbTOG8V3bOx', 'spotify:track:4KvlilbyIkDukYgD70F1Ve', 'spotify:track:62ZXL1CWLJDiDWUZUhfLfU', 'spotify:track:69w5X6uTrOaWM32IetSzvO']
sadPlaylist = ['spotify:track:161DnLWsx1i3u1JT05lzqU', 'spotify:track:7wTA0NKIm6T7nP2kaymU2a', 'spotify:track:047fCsbO4NdmwCBn8pcUXl', 'spotify:track:0rKtyWc8bvkriBthvHKY8d', 'spotify:track:0d2iYfpKoM0QCKvcLCkBao', 'spotify:track:41zXlQxzTi6cGAjpOXyLYH', 'spotify:track:7zFXmv6vqI4qOt4yGf3jYZ', 'spotify:track:2QjOHCTQ1Jl3zawyYOpxh6', 'spotify:track:0RUGuh2uSNFJpGMSsD1F5C', 'spotify:track:0dWOFwdXrbBUYqD9DLsoyK', 'spotify:track:7EdJ8z6IBotTjO50DfzzuV', 'spotify:track:3q2v8QaTnHLveAQzR6gvYm', 'spotify:track:3cjF2OFRmip8spwZYQRKxP', 'spotify:track:0GaBIpyHvytM1UBYmqXu08']
angryPlaylist = ['spotify:track:6VExFHGjEEuxS4fFDghWnB', 'spotify:track:5SsR3wtCOafDmZgvIdRhSm', 'spotify:track:6Js9pKLTyVw7xZQ1MIjkVo', 'spotify:track:0waK9D203FQO5FpMmfjxBw', 'spotify:track:57BGVV6wcyhbn3hsjlqEZB', 'spotify:track:4xqIYGwwZTEem9U8A42SPF', 'spotify:track:7JuHVG3qQKQKxC4doneXVW', 'spotify:track:7Bpx2vsWfQFBACRz4h3IqH', 'spotify:track:6G9aDedv5hYaTgNYDuduqk', 'spotify:track:4zGvb8hxGLB2jEPRFiRRqw', 'spotify:track:7mLWNwcvwRdEviz6SfYp8A']
fearPlaylist = ['spotify:track:6gwWEPNLpFAYSvoYVInVqx', 'spotify:track:7vggqxNKwd6xdRoYS0pQtM', 'spotify:track:0j35X8cTq543QDYLOyqB8W', 'spotify:track:62aP9fBQKYKxi7PDXwcUAS', 'spotify:track:3aftC8snv7QPeTkvQrw17h', 'spotify:track:3Gqf3oTMOjrjLXi4ELzhbB', 'spotify:track:3gFQOMoUwlR6aUZj81gCzu', 'spotify:track:7pRcWov3NHxi0GDkKdbSb0']

# auth_headers = {
#     "client_id": CLIENT_ID,
#     "response_type": "code",
#     "redirect_uri": REDIRECT_URI,
#     "scope": "playlist-modify-public"
# }

def user_authorize_Spotipy():
    ACCESS_TOKEN = spotipy.util.prompt_for_user_token(username='',scope='playlist-modify-public playlist-modify-private',client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
    #print("Access Token: {}".format(ACCESS_TOKEN))
    return ACCESS_TOKEN

def initialize_playlist(name, public):
    response = requests.post(USER_PLAYLISTS_URL, 
                             headers = {"Authorization": f"Bearer {settings.ACCESS_TOKEN}"}, 
                             json = {"name": name, "public": public})
    print(response)
    json_resp = response.json()
    return json_resp

def add_to_playlist(songs, playlistURL):
    response = requests.post(playlistURL,
                             headers = {"Authorization": f"Bearer {settings.ACCESS_TOKEN}"},
                             json = {"uris": songs})
    json_resp = response.json()
    return json_resp

def read_saved_tracks():
    response = requests.get("https://api.spotify.com/v1/me/tracks",
                            headers = {"Authorization": f"Bearer {settings.ACCESS_TOKEN}", "Content-Type": "application/json"},
                            params = {"limit" : 50})
    json_resp = response.json()
    return json_resp

def create_mood_playlist(mood):
    if mood == 'happy':
        newPlaylist = initialize_playlist(name = "Happy :D", public=False)
        newPlaylistURL = newPlaylist['tracks']['href']
        add_to_playlist(happyPlaylist, newPlaylistURL)
    elif mood == 'sad':
        newPlaylist = initialize_playlist(name = "Sad :(", public=False)
        newPlaylistURL = newPlaylist['tracks']['href']
        add_to_playlist(sadPlaylist, newPlaylistURL)
    elif mood == 'angry':
        newPlaylist = initialize_playlist(name = "Get Hyped >:)", public=False)
        newPlaylistURL = newPlaylist['tracks']['href']
        add_to_playlist(angryPlaylist, newPlaylistURL)
    elif mood == 'fear':
        newPlaylist = initialize_playlist(name = "Calm down", public=False)
        newPlaylistURL = newPlaylist['tracks']['href']
        add_to_playlist(fearPlaylist, newPlaylistURL)
    return newPlaylist['external_urls']['spotify']

# def main():
#     global ACCESS_TOKEN
#     ACCESS_TOKEN = user_authorize_Spotipy()
#     # create_mood_playlist('happy')

# if __name__ == '__main__':
#     main()

'''
GET ARTIST HREF:
for song in json_resp['items']:
    for artist in song['track']['artists']:
        print(artist['href'])
        print('\n')
'''

'''
OLD AUTHORIZATION FUNCTION (NOT USING SPOTIPY):
def user_authorize():
    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
    encoded_credentials = base64.b64encode(CLIENT_ID.encode() + b':' + CLIENT_SECRET.encode()).decode("utf-8")
    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    token_data = {
        "grant_type": "authorization_code",
        "code": CODE,
        "redirect_uri": REDIRECT_URI
    }  
    response = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
    json_resp = response.json()
    ACCESS_TOKEN = json_resp["access_token"]
    # print(json_resp)
    return ACCESS_TOKEN
'''