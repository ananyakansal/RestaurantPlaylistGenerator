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
        print(req)
        result = initPlaylist(req)
        if result == 'ok':
            return json.dumps({'status':'OK', 'choices': req})
        else:
            return json.dumps('bad selection')
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
    form = interpretForm(req)
    #newest_getPlaylist.setStaticList(['classical'], 'aggressive', 'bright', 'instrumental', 'fast', 'not_dance')
    try:
        newest_getPlaylist.setStaticList(form[0], form[1], form[2], form[3], form[4], form[5])
        newest_getPlaylist.initQueue()
        global currSong
        global playerReady
        global queueUpdate
        currSong = newest_getPlaylist.playQueue(songSPL)
        playerReady = True
        queueUpdate = True
        return('ok')
    except SelectionError as e:
        print(e)
        return(e)

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
    print(form)
    print(type(form[1]))
    print(type('aggressive'))
    return form

@app.route("/startPlayback", methods= ['GET', 'POST'])
def startPlayback():
    global playFlag
    global currSong
    global queueUpdate
    playFlag = True
    if (progress == 0):
        currSong = newest_getPlaylist.playQueue(useSPL, songSPL)
        spotifyPlayback2.startPlayback(currSong)
        queueUpdate = True
    spotifyPlayback2.startPlayback(currSong)
    # if request.method == "POST":
    return 'nothing'
    # return songInfo[0]

@app.route("/updateElements")
def update():
    # queue = newest_getPlaylist.getQueue()
    global queueUpdate
    # spl=runningSPL.SPL(1024)
    spl=''
    if playerReady and queueUpdate:
        songInfo1 = spotifyPlayback2.getSongInfo(currSong)
        queue = newest_getPlaylist.getQueue()
        songInfo2 = spotifyPlayback2.getSongInfo(queue[0])
        songInfo3 = spotifyPlayback2.getSongInfo(queue[1])
        songInfo4 = spotifyPlayback2.getSongInfo(queue[2])
        queueUpdate = False
        return jsonify(song1=songInfo1[0], song2=songInfo2[0], song3=songInfo3[0], song4=songInfo4[0], spl=spl)
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
    # a = threading.Thread(target=runSPL)
    # a.start()
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    a = threading.Thread(app.run(debug=True, threaded=True, port=5000))
    p.join()
    t.join()