import pyaudio
import wave
import numpy
import math

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

amps = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = numpy.frombuffer(stream.read(CHUNK), dtype = numpy.int16)
    if i % 32 == 0: #just to visualize that the recording is still going on
        print(".")
    newDecoded = numpy.max(data)/32767
    blockLogRms = 20*numpy.log10(numpy.sqrt(numpy.mean(numpy.absolute(newDecoded)**2)))
    amps.append(blockLogRms)
ave = sum(amps)/(RATE / CHUNK * RECORD_SECONDS)
print(ave, "dB")

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()


