import requests
import json

##server side
CLIENT_ID = "cc02566bde9444cdb1aa1855f3fce9d1"
CLIENT_SECRET = ""
PORT = "5000"
CLIENT_URL = "http://127.0.0.1"
REDIRECT_URI = "{}:{}/callback/".format(CLIENT_URL, PORT)
SCOPE = "user-modify-playback-state user-read-recently-played streaming user-read-currently-playing user-read-playback-state"
TOKEN_DATA = []

##spotify parameters
SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
RESPONSE_TYPE = 'code'   
HEADER = 'application/x-www-form-urlencoded'
REFRESH_TOKEN = ''


def getAuth():
    return "{}client_id={}&response_type={}&redirect_uri={}&scope={}".format(SPOTIFY_URL_AUTH, CLIENT_ID, RESPONSE_TYPE, REDIRECT_URI, SCOPE) 

def getUserToken(authCode):
    global TOKEN_DATA
    body = {
        "grant_type": "authorization_code",
        "code": str(authCode),
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    postRequest = requests.post(SPOTIFY_URL_TOKEN, data=body)
    response = json.loads(postRequest.text)
    authHeader = {"Authorization": "Bearer {}".format(response["access_token"])}
    REFRESH_TOKEN = response["refresh_token"]
    return [response["access_token"], authHeader, response["scope"], response["expires_in"]]


def refreshToken(time):
    time.sleep(time)
    body = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }
    postRefresh = requests.post(SPOTIFY_URL_TOKEN, data=body, headers=HEADER)
    response = json.dumps(postRefresh)
    authHeader = {"Authorization": "Bearer {}".format(response["access_token"])}
    REFRESH_TOKEN = response["refresh_token"]
    return [response["access_token"], authHeader, response["scope"], response["expires_in"]]

def getAccessToken():
    return TOKEN_DATA
