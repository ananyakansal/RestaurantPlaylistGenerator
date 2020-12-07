from flask import Flask, render_template, redirect, request, url_for, jsonify
import spotifyAuthentication
import spotifyPlayback2
import newest_getPlaylist
from newest_getPlaylist import SelectionError
import runningSPL
import json
import time
import threading

app = Flask(__name__)

global currSong
playFlag = False
playerReady = False
global progress
global playerSet
playerSet = False
progress = ''
global firstPlay
firstPlay = True
global token
global queueUpdate
global songSPL
global useSPL
global useSimilarity
global currArt
global duration
global micIsSet
micIsSet = False
duration = ''
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
    if request.method == "POST":
        req = request.form
        try:
            result = initPlaylist(req)
        except:
            return json.dumps('Please fill out the entire form.')
        if result == 'ok':
            return json.dumps('Thank you! Your submission has been received! Wait for the queue to load, then click on the play button to start listening!')
        else:
            return json.dumps('Your current selection is unavailable. Please make a new selection.')
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

def initPlaylist(req):
    global queueUpdate
    global currSong
    form = interpretForm(req)
    try:
        newest_getPlaylist.setStaticList(form[0], form[1], form[2], form[3], form[4], form[5])
    except SelectionError as e:
        newest_getPlaylist.clearQueue()
        queueUpdate = True
        currSong = ''
        return(e)
    newest_getPlaylist.initQueue()
    global playerReady
    global playFlag
    global progress
    global firstPlay
    progress = 0  
    firstPlay = True
    playFlag = False
    currSong = newest_getPlaylist.playQueue(songSPL, useSimilarity)
    playerReady = True
    queueUpdate = True
    return('ok')

def interpretForm(req):
    global useSPL
    global useSimilarity
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
    if (req['radio-6'] == 'similarity'):
        useSimilarity = True
    else:
        useSimilarity = False
    form = [genre, mood, timbre, instrument, tempo, dance]
    return form

@app.route("/startPlayback", methods= ['GET', 'POST'])
def startPlayback():
    global playFlag
    global currSong
    global queueUpdate
    global currArt
    global duration
    global firstPlay
    playFlag = True
    if (progress < 1 and not firstPlay):
        currSong = newest_getPlaylist.playQueue(useSPL, useSimilarity, songSPL)
        spotifyPlayback2.startPlayback(currSong)
        queueUpdate = True
    elif (firstPlay):
        spotifyPlayback2.startPlayback(currSong, firstPlay)
        firstPlay = False
    else:
        spotifyPlayback2.startPlayback(currSong)
    return jsonify(art=currArt)

@app.route("/updateElements")
def update():
    global queueUpdate
    global currArt
    global duration
    global progress
    if progress == '' or duration == '':
        dur = duration
        prog = progress
    else:
        dur = str(int(duration/60000)) + ":" + str(int(duration/1000)%60)
        prog = str(int(progress/60000)) + ":" + str(int(progress/1000)%60)
    if useSPL:
        spl='Room Noise: ' + str(runningSPL.SPL())
    else:
        spl=''
    if playerReady and queueUpdate:
        try:
            queue = newest_getPlaylist.getQueue()
        except IndexError:
            return jsonify(song1='', song2='', song3='', song4='', spl=spl, duration='', progress='')
            # return jsonify(song1='', song2='', song3='', song4='', spl=spl)
        songInfo1 = spotifyPlayback2.getSongInfo(currSong)
        currArt = songInfo1[2]
        duration = songInfo1[1]
        songInfo2 = spotifyPlayback2.getSongInfo(queue[0])
        # songInfo3 = spotifyPlayback2.getSongInfo(queue[1])
        # songInfo4 = spotifyPlayback2.getSongInfo(queue[2])
        queueUpdate = False
        return jsonify(song1=songInfo1[0], song2=songInfo2[0], song3='', song4='', spl=spl, duration=dur, progress=prog)
    #     return jsonify(song1=songInfo1[0], art=songInfo1[2], song2=songInfo2[0], song3='', song4='', spl=spl, duration=dur, progress=prog)
    return jsonify(spl=spl, duration=dur, progress=prog)
    # return jsonify(spl=spl)

@app.route("/pausePlayback", methods= ['GET', 'POST'])
def pausePlayback():
    global playFlag
    playFlag = False
    spotifyPlayback2.pausePlayback()
    return 'nothing'

def checkPlaystate():
    # while run_event.is_set():
    while True:
        with app.app_context():
            playcheck()
            time.sleep(2)

def checkSPL():
    # while run_event.is_set():
    while True:
        with app.app_context():
            runSPL()

# def runSPL():
#     global queueUpdate
#     global songSPL
#     if useSPL:
#         spl=runningSPL.SPL(1024)
#         songSPL.append(spl)
#         if queueUpdate:
#             songSPL = []

def runSPL():
    global queueUpdate
    global songSPL
    global micIsSet
    if useSPL:
        if not micIsSet:
            micIsSet = runningSPL.openMic()
        spl=runningSPL.SPL()
        songSPL.append(spl)
        if queueUpdate:
            songSPL = []
    if not useSPL:
        if micIsSet:
            micIsSet = runningSPL.closeMic()

def playcheck():
    global progress
    if playerReady and playFlag:
        progress = spotifyPlayback2.getProgress()
        if progress == 'NoneType':
            progress = 0
        if progress == 0:
            startPlayback()

@app.before_first_request
def startThreads():
    c = threading.Thread(target=checkPlaystate)
    c.daemon = False
    c.start()
    t = threading.Thread(target=checkSPL)
    t.daemon = False
    t.start()
    print('threads')

if __name__ == "__main__":
    # run_event = threading.Event()
    # run_event.set()
    # p = threading.Thread(target=checkPlaystate)
    # p.daemon = True
    # p.start()
    # t = threading.Thread(target=checkSPL)
    # t.daemon = True
    # t.start()
    a = threading.Thread(app.run(debug=True, threaded=False, port=5000))
    # p.join()
    # t.join()