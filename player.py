# Project Studio Group 3
# username(s): jocekav
# name(s): Jocelyn Kavanagh
# version: 1
# description: Plays wave file when a user inputs a path. User has the ability to stop playback.
#               Currently implemented with callbackPlayback.py, but blockPlayback functionality is commented
# sources: Adapted from PyAudio documentation found at https://people.csail.mit.edu/hubert/pyaudio/docs/


import pyaudio
# import blockPlayback as player
import callbackPlayback as player
import time

# create PyAudio context
pa = pyaudio.PyAudio()

txt = input("Plays a wave file. Copy in the path to a wave file: ")

# [wf, stream, data] = player.initSong(txt, pa, 1024)
[wf, stream] = player.initSong(txt, pa, 1024) 

# stop stream if user enters stop
while stream.is_active():
    txt = input("Type 'stop' to stop playback ")
    if "stop" in txt:
        player.pause(stream)
        txt = input("Type 'play' to resume playback ")
        if "play" in txt:
            player.play(wf,stream)
    time.sleep(0.1)


# txt = input("Type 'stop' to stop playback")
# stop stream if user enters stop
# if "stop" in txt:
#     stream.stop_stream()
#     txt = input("Type 'play' to resume playback ")
#     if "play" in txt:
#         stream.start_stream()
# data = player.play(wf, stream, data, 1024)
# while len(data) > 0 or "stop" in txt:
#     data = player.play(wf, stream, data, 1024)
    # txt = input("Type 'stop' to stop playback")
    