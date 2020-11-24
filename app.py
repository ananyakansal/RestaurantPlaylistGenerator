from flask import Flask, render_template, redirect, request, url_for
import spotifyAuthentication
import spotifyPlayback
import spotifyPlayback2
import getPlaylist
import json
import spotipy
import time
import threading
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

global currSong
currSong = 0
global playFlag
global event
global token
event = threading.Event()

@app.route("/", methods= ['GET', 'POST'])
def index():
    getPlaylist.initStaticLists()
    return render_template('main.html', title="Home")

@app.route("/callback/")
def callback():
    return redirect(spotifyAuthentication.getAuth())

@app.route("/player/", methods= ['GET', 'POST'])
def player():
    # userToken = spotifyAuthentication.getUserToken(request.args['code'])
    # token = {'userToken': userToken[0]}
    if request.method == "POST":
        req = request.form
        print(req)
        return redirect(request.url)
    else:
        if 'code' in request.args:
            userToken = spotifyAuthentication.getUserToken(request.args['code'])
            global token
            token = {'userToken': userToken[0]}
        return render_template('player.html', token=token, songTitle={'song1'})

@app.route("/initPlayer", methods= ['GET', 'POST'])
def initPlayer():
    spotifyPlayback2.initPlayer()
    getPlaylist.initStaticLists()
    getPlaylist.setStaticList('classical', 'cheerful', 'bright', 'instrumental', 'fast', 'not_dance')
    getPlaylist.initQueue()
    return 'nothing'

@app.route("/startPlayback", methods= ['GET', 'POST'])
def startPlayback():
    global playFlag
    playFlag = True
    # playlist = getPlaylist.getStaticList()
    # spotifyPlayback2.startPlayback(playlist[currSong])
    spotifyPlayback2.startPlayback(getPlaylist.playQueue())
    firstPlay = True
    while (playFlag):
        progress = spotifyPlayback2.getProgress()
        if progress is 'NoneType':
            progress = 0
        # duration = spotifyPlayback2.getSongLength(playlist[currSong])
        if progress == 0 and not firstPlay:
            # spotifyPlayback2.startPlayback(playlist[currSong])
            spotifyPlayback2.startPlayback(getPlaylist.playQueue())
            firstPlay = True
        else:
            firstPlay = False
    # return (title=title, albumArt=art)
    # return render_template('temp.html', songTitle='testTest')
    return render_template('temp.html', token=token, songTitle={'Test Song'})

@app.route("/pausePlayback", methods= ['GET', 'POST'])
def pausePlayback():
    global playFlag
    playFlag = False
    spotifyPlayback2.pausePlayback()
    # print(spotifyPlayback2.getSongInfo('spotify:track:0oQc0F6KUE7QY7k5TU6bic'))
    return 'nothing'

@app.route('/addQueue')
def addQueue():
    spotifyPlayback.addSongToQueue('spotify:track:5aaUXcrsXI477I93yBE8lu')
    return 'nothing'

@app.route('/nextTrack')
def nextTrack():
    spotifyPlayback.nextSong()
    return 'nothing'

if __name__ == "__main__":
    app.run(debug=True, port=5000)