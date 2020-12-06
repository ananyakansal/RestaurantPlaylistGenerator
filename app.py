from flask import Flask, render_template, redirect, request, url_for, jsonify
import spotifyAuthentication
import spotifyPlayback2
import newest_getPlaylist
from newest_getPlaylist import SelectionError
import runningSPL
import json
import time
import threading
from multiprocessing import Process, Value

app = Flask(__name__)

global currSong
playFlag = False
playerReady = False
global progress
global playerSet
playerSet = False
progress = 1
global event
global token
global queueUpdate
global songSPL
global useSPL
global currArt
currArt = ''
useSPL = False
songSPL = []
queueUpdate = True

@app.route("/", methods= ['GET', 'POST'])
def index():
    return render_template('about.html', title="Home")

@app.route("/callback/")
def callback():
    return redirect(spotifyAuthentication.getAuth())

@app.route("/player/", methods= ['GET', 'POST'])
def player():
    # global token
    # userToken = spotifyAuthentication.getUserToken(request.args['code'])
    # token = {'userToken': userToken[0]}
    if request.method == "POST":
        req = request.form
        # print(req)
        try:
            result = initPlaylist(req)
        except:
            return json.dumps('Please fill out the entire form.')
        if result == 'ok':
            return json.dumps('Thank you! Your submission has been received!')
        else:
            return json.dumps('Your current selection is unavailable. Please make a new selection.')
        # return render_template('player.html', token=token, songTitle='something')
    else:
        if 'code' in request.args:
            global token
            userToken = spotifyAuthentication.getUserToken(request.args['code'])
            token = {'userToken': userToken[0]}
        return render_template('player.html', token=token)

@app.route("/initPlayer", methods= ['GET','POST'])
def initPlayer():
    global playerSet
    if not playerSet:
        spotifyPlayback2.initPlayer()
        playerSet = True
    return 'nothing'

# @app.route("/initPlaylist", methods= ['POST', 'GET'])
def initPlaylist(req):
    global queueUpdate
    global currSong
    form = interpretForm(req)
    #newest_getPlaylist.setStaticList(['classical'], 'aggressive', 'bright', 'instrumental', 'fast', 'not_dance')
    try:
        newest_getPlaylist.setStaticList(form[0], form[1], form[2], form[3], form[4], form[5])
    except SelectionError as e:
        # print(e)
        newest_getPlaylist.clearQueue()
        queueUpdate = True
        currSong = ''
        return(e)
    newest_getPlaylist.initQueue()
    global playerReady
    global playFlag
    global progress
    progress = 0
    playFlag = False
    currSong = newest_getPlaylist.playQueue(songSPL)
    playerReady = True
    queueUpdate = True
    return('ok')

def interpretForm(req):
    global useSPL
    mood = req['Genre']
    genre = [k for k,v in req.items() if v == 'on']
    instrument = req['instrumental']
    timbre = req['radio-5']
    tempo = req['radio']
    dance = req['danceability']
    if (req['radio-6'] == 'spl'):
        useSPL = True
    else:
        useSPL = False
    form = [genre, mood, timbre, instrument, tempo, dance]
    return form

@app.route("/startPlayback", methods= ['GET', 'POST'])
def startPlayback():
    global playFlag
    global currSong
    global queueUpdate
    global currArt
    playFlag = True
    if (progress == 0):
        currSong = newest_getPlaylist.playQueue(useSPL, songSPL)
        spotifyPlayback2.startPlayback(currSong)
        queueUpdate = True
    spotifyPlayback2.startPlayback(currSong)
    return jsonify(art=currArt)
    # return songInfo[0]

@app.route("/updateElements")
def update():
    # queue = newest_getPlaylist.getQueue()
    global queueUpdate
    global currArt
    if useSPL:
        spl='Room Noise: ' + str(runningSPL.SPL(1024))
    else:
        spl=''
    if playerReady and queueUpdate:
        try:
            queue = newest_getPlaylist.getQueue()
        except IndexError:
            return jsonify(song1='', song2='', song3='', song4='', spl=spl)
        songInfo1 = spotifyPlayback2.getSongInfo(currSong)
        currArt = songInfo1[2]
        songInfo2 = spotifyPlayback2.getSongInfo(queue[0])
        # songInfo3 = spotifyPlayback2.getSongInfo(queue[1])
        # songInfo4 = spotifyPlayback2.getSongInfo(queue[2])
        queueUpdate = False
        # return jsonify(song1=songInfo1[0], song2=songInfo2[0], song3=songInfo3[0], song4=songInfo4[0], spl=spl)
        return jsonify(song1=songInfo1[0], art=songInfo1[2], song2=songInfo2[0], song3='', song4='', spl=spl)
    return jsonify(spl=spl)

@app.route("/pausePlayback", methods= ['GET', 'POST'])
def pausePlayback():
    global playFlag
    playFlag = False
    spotifyPlayback2.pausePlayback()
    return 'nothing'

def checkPlaystate():
    while True:
        playcheck()
        time.sleep(4)

def checkSPL():
    while True:
        runSPL()

def runSPL():
    global queueUpdate
    global songSPL
    if useSPL:
        spl=runningSPL.SPL(1024)
        songSPL.append(spl)
        # print(len(songSPL))
        if queueUpdate:
            songSPL = []

def playcheck():
    global progress
    if playerReady and playFlag:
        # while not event.is_set():
        progress = spotifyPlayback2.getProgress()
        if progress == 'NoneType':
            progress = 0
        if progress == 0:
            startPlayback()

if __name__ == "__main__":
    p = threading.Thread(target=checkPlaystate)
    p.daemon = True
    p.start()
    t = threading.Thread(target=checkSPL)
    t.daemon = True
    t.start()
    a = threading.Thread(app.run(debug=True, threaded=False, port=5000))
    p.join()
    t.join()