import pyaudio
import wave
import numpy
import math

print('Recording...')
def SPL(chunk):
    CHUNK = chunk
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 1

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    amps = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = numpy.frombuffer(stream.read(CHUNK), dtype = numpy.int16)
        newDecoded = numpy.max(data)/32767
        blockLogRms = 20*numpy.log10(numpy.sqrt(numpy.mean(numpy.absolute(newDecoded)**2)))
        amps.append(blockLogRms)
        i = i + 1
    ave = sum(amps)/(RATE / CHUNK * RECORD_SECONDS)
    #print(ave, "dB")


    stream.stop_stream()
    stream.close()
    p.terminate()
    return ave

dbs = []
while True:
    db = SPL(1024)
    dbs.append(db)
    #print(dbs)
    window_size = 10

    j = 0
    moving_averages = []
    warndown = -15
    warnup = 15

    while j < len(dbs) - window_size + 1:

        this_window = dbs[j : j + window_size]
        window_average = sum(this_window) / window_size
        moving_averages.append(window_average)
        j += 1
    if j >= 10:
        print(moving_averages[-1])