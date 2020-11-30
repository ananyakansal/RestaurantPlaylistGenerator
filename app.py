from flask import Flask, render_template, redirect, request, url_for, jsonify
import spotifyAuthentication
import spotifyPlayback
import spotifyPlayback2
import getPlaylist
import spotipy
import json
import time
import threading
from spotipy.oauth2 import SpotifyOAuth
from multiprocessing import Process, Value

app = Flask(__name__)

global currSong
playFlag = False
playerReady = False
global progress
progress = 1
global event
global token
global queueUpdate
queueUpdate = True
event = threading.Event()

@app.route("/", methods= ['GET', 'POST'])
def index():
    # getPlaylist.initStaticLists()
    print("done")
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
        # return render_template('player.html', token=token, songTitle='something')
    else:
        if 'code' in request.args:
            userToken = spotifyAuthentication.getUserToken(request.args['code'])
            global token
            token = {'userToken': userToken[0]}
        return render_template('player.html', token=token)

@app.route("/initPlayer", methods= ['GET', 'POST'])
def initPlayer():
    spotifyPlayback2.initPlayer()
    getPlaylist.setStaticList('classical', 'cheerful', 'bright', 'instrumental', 'fast', 'not_dance')
    getPlaylist.initQueue()
    global currSong
    global playerReady
    global queueUpdate
    currSong = getPlaylist.playQueue()
    playerReady = True
    queueUpdate = True
    return render_template('player.html', token=token, songTitle='songInfo[0]')

@app.route("/startPlayback", methods= ['GET', 'POST'])
def startPlayback():
    global playFlag
    global currSong
    global queueUpdate
    playFlag = True
    if (progress == 0):
        currSong = getPlaylist.playQueue()
        spotifyPlayback2.startPlayback(currSong)
        queueUpdate = True
    spotifyPlayback2.startPlayback(currSong)
    # if request.method == "POST":
    return render_template('player.html', token=token)
    # return songInfo[0]

@app.route("/updateElements")
def update():
    # queue = getPlaylist.getQueue()
    global queueUpdate
    if playerReady and queueUpdate:
        songInfo1 = spotifyPlayback2.getSongInfo(currSong)
        queue = getPlaylist.getQueue()
        songInfo2 = spotifyPlayback2.getSongInfo(queue[0])
        songInfo3 = spotifyPlayback2.getSongInfo(queue[1])
        songInfo4 = spotifyPlayback2.getSongInfo(queue[2])
        queueUpdate = False
        return jsonify(song1=songInfo1[0], song2=songInfo2[0], song3=songInfo3[0], song4=songInfo4[0])
    return jsonify()

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

def tester():
    while True:
        print("testing ")
        time.sleep(1)

def checkPlaystate():
    while True:
        playcheck()
        time.sleep(4)

def playcheck():
    global progress
    if playerReady and playFlag:
        # while not event.is_set():
        progress = spotifyPlayback2.getProgress()
        if progress is 'NoneType':
            progress = 0
        if progress == 0:
            startPlayback()

if __name__ == "__main__":
    # tester = threading.Thread(target=tester())
    # app.run(debug=True, port=5000)
    # test_on = True
    # p = Process(target=checkPlaystate)
    # p.start() 
    p = threading.Thread(target=checkPlaystate)
    p.start()
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, port=5000)
    # p.join()