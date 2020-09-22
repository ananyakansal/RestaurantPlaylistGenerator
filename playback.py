# Project Studio Group 3
# username(s): jocekav
# name(s): Jocelyn Kavanagh
# version: 1
# description: Plays wave file when a user inputs a path. User has the ability to stop playback
# sources: Adapted from PyAudio documentation found at https://people.csail.mit.edu/hubert/pyaudio/docs/

import time
import pyaudio
import wave

# create PyAudio context
pa = pyaudio.PyAudio()

# prompt user to type path to wave file and store input
txt = raw_input("Plays a wave file. Copy in the path to a wave file: ")

# open the wave file
wf = wave.open(txt, 'rb')

# callback function to check the completion of the stream
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

# open the stream using callback
stream = pa.open(format=pa.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

# start the stream
stream.start_stream()

# wait for stream to finish and prompt user to 
while stream.is_active():
    # prompt user to stop playback at anytime
    txt = raw_input("Type 'stop' to stop playback")
    # stop stream if user enters stop
    if "stop" in txt:
        stream.stop_stream()
        txt = raw_input("Type 'play' to resume playback ")
        if "play" in txt:
            stream.start_stream()
    time.sleep(0.1)

# stop stream once it has ended
stream.stop_stream()
# close stream
stream.close()
# close wave file
wf.close()
# close PyAudio
pa.terminate()
