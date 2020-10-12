# Project Studio Group 3
# username(s): jocekav
# name(s): Jocelyn Kavanagh
# version: 1
# description: Functions to call for playback using blocking. Currently, no pause/play functionality
# sources: Adapted from PyAudio documentation found at https://people.csail.mit.edu/hubert/pyaudio/docs/

import pyaudio
import wave
import numpy
import math

def initSong(file, source, block, fade = 200):
    wf = wave.open(file, 'rb')
    stream = source.open(format=source.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
#    if fade:
#        fadein = numpy.arange(0, 1.0, 1/fade)
#        fadeout = numpy.arange(1.0, 0, -1/fade)
#        data = stream.read()
#        wf[:fade] = numpy.multiply(wf[:fade], fadein)
#        wf[-fade:] = numpy.multiply(wf[-fade:], fadeout)

    data = wf.readframes(block)
    return wf, stream, data

def endSong(wavefile, stream):
    stream.stop_stream()
    stream.close()
    wavefile.close()

def play(wavefile, stream, data, block):
    stream.write(data)
    data = wavefile.readframes(block)
    return data

def pause(stream):
    stream.stop_stream()

