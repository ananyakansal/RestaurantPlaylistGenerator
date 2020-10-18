import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""
PORT = "5000"
CLIENT_URL = "http://127.0.0.1"
REDIRECT_URI = "{}:{}/player/".format(CLIENT_URL, PORT)
SCOPE = "user-modify-playback-state user-read-recently-played streaming user-read-currently-playing user-read-playback-state user-read-email user-read-private"
TOKEN_DATA = []


def initPlayer():
    global sp
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI))
    # sp.transfer_playback(device_id='1360e7e1bf1126627e48ce5c86e08e04697abb5e')
    # devices = sp.devices()['devices']
    # for i in devices:
    #     if devices[i] is 'Spotify Player':
    #         DEVICE_ID = devices[i]['id']
    #         break
    # sp.transfer_playback(device_id=DEVICE_ID)
    # return sp.devices()['devices'][0]['name']
    DEVICE_ID = sp.devices()['devices'][0]['id']
    sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

def startPlayback():
    sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

def pausePlayback():
    sp.pause_playback()
