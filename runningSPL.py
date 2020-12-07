import pyaudio
import wave
import numpy
import math

global p
global stream
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1

# print('Measuring...')
def openMic():
    global p
    global stream

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    return True


def SPL():
    global p
    global stream
    amps = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = numpy.frombuffer(stream.read(CHUNK), dtype = numpy.int16)
        newDecoded = numpy.max(data)/32767
        # print(newDecoded)
        # if (newDecoded == 0):
        #     newDecoded = 0.5
        blockLogRms = 10*numpy.log10((numpy.mean(numpy.absolute((newDecoded)**2))))
        amps.append(blockLogRms)
        i = i + 1
    ave = sum(amps)/(RATE / CHUNK * RECORD_SECONDS)

    return ave

def closeMic():
    stream.stop_stream()
    stream.close()
    p.terminate()
    return False

# dbs = []
# while True:
#     db = SPL(1024)
#     dbs.append(db)
#     window_size = 10

#     j = 0
#     moving_averages = []
#     warndown = -15
#     warnup = 15

#     while j < len(dbs) - window_size + 1:

#         this_window = dbs[j : j + window_size]
#         window_average = sum(this_window) / window_size
#         moving_averages.append(window_average)
#         j += 1
#     if j >= 10:
#         print(moving_averages[-1])

dbs = []
moving_averages = []
def getRMS(block=1024):
    global dbs
    global moving_averages 
    db = SPL(block)
    dbs.append(db)
    window_size = 10

    j = 0
    # warndown = -15
    # warnup = 15

    while j < len(dbs) - window_size + 1:
        this_window = dbs[j : j + window_size - 1]
        window_average = sum(this_window) / window_size
        moving_averages.append(window_average)
        j += 1 
        return window_average
        # print(moving_averages)
        # return (moving_averages[-1])
        # if j >= 10:
        #     print(moving_averages)
        #     print(moving_averages[-1])
        #     return moving_averages[-1]

# while True:
#     getRMS()