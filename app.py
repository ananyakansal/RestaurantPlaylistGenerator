from flask import Flask, render_template, redirect, request, url_for
import spotifyAuthentication
import spotifyPlayback
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html', title="Home")

@app.route("/callback/")
def callback():
    return redirect(spotifyAuthentication.getAuth())

@app.route("/player/", methods= ['GET', 'POST'])
def player():
    userToken = spotifyAuthentication.getUserToken(request.args['code'])
    token = {'userToken': userToken[0]}
    # print(token)
    return render_template('player.html', token=token)

@app.route("/initPlayer")
def initPlayer():
    spotifyPlayback.initPlayer()

@app.route("/startPlayback")
def startPlayback():
    spotifyPlayback.startPlayback()

@app.route("/pausePlayback")
def pausePlayback():
    spotifyPlayback.pausePlayback()
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)