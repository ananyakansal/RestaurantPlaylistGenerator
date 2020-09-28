# Project Studio Group 3
# username(s): jocekav
# name(s): Jocelyn Kavanagh
# version: 1
# description: Functions to call for playback using callback. No fade in/out functionality
# sources: Adapted from PyAudio documentation found at https://people.csail.mit.edu/hubert/pyaudio/docs/


import pyaudio
import wave
import numpy
import math

def setFile(file):
    global wf
    wf = file

def getFile():
    return wf

# callback function to check the completion of the stream
def callback(in_data, frame_count, time_info, status):
    data = getFile().readframes(frame_count)
    return (data, pyaudio.paContinue)

def initSong(file, source, fade = 200):
    # open the wave file
    wf = wave.open(file, 'rb')
    setFile(wf)
    # open the stream using callback
    stream = source.open(format=source.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
    # if fade:
    #     fadein = numpy.arange(0, 1.0, 1/fade)
    #     fadeout = numpy.arange(1.0, 0, -1/fade)
    #     data = stream.read()
    #     wf[:fade] = numpy.multiply(wf[:fade], fadein)
    #     wf[-fade:] = numpy.multiply(wf[-fade:], fadeout)
    stream.start_stream()
    return wf, stream


def endSong(wavefile, stream):
    # stop stream once it has ended
    stream.stop_stream()
    # close stream
    stream.close()
    # close wave file
    wavefile.close()

def play(wavefile, stream):
    stream.start_stream()

def pause(stream):
    stream.stop_stream()

