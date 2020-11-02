import requests
import json
import spotifyAuthentication

PORT = "5000"
CLIENT_URL = "http://127.0.0.1"
REDIRECT_URI = "{}:{}/player/".format(CLIENT_URL, PORT)
SCOPE = "user-modify-playback-state user-read-recently-played streaming user-read-currently-playing user-read-playback-state user-read-email user-read-private"

SPOTIFY_URL_PLAYER = "https://api.spotify.com/v1/me/player/"


def initPlayer():
    #get devices
    header = spotifyAuthentication.auth_head
    response = requests.get(SPOTIFY_URL_PLAYER + "devices", 
                    headers = header)
    resp = response.json()
    devices = resp['devices']
    found = False
    count = -1
    while not found:
        count += 1
        if devices[count]['name'] == 'Spotify Player':
            DEVICE_ID = devices[count]['id']
            found = True
    data = '{\"device_ids\":[\"' + DEVICE_ID + '\"]}'
    #transfer devices
    response = requests.put(SPOTIFY_URL_PLAYER, headers=header, data=data)
    resp = json.dumps(response.text)
    global firstPlay
    firstPlay = True

def startPlayback(uri):
    global firstPlay
    #get current play state
    header = spotifyAuthentication.auth_head
    response = response = requests.get(SPOTIFY_URL_PLAYER, headers = header)
    resp = response.json()
    progress = resp['progress_ms']
    if progress is 'NoneType' or firstPlay is True:
        progress = 0
        firstPlay = False
    #play at progress point
    data = '{\"uris\":[\"' + uri + '\"],\"position_ms\":' + str(progress) + '}'
    requests.put(SPOTIFY_URL_PLAYER + 'play', headers=header, data=data)

def pausePlayback():
    header = spotifyAuthentication.auth_head
    requests.put(SPOTIFY_URL_PLAYER  + 'pause', headers=header)
