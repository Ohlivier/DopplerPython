import pyaudio
import numpy as np
import time


from scipy.fft import fft


CHUNK_SIZE = 12000   
FORMAT = pyaudio.paInt16   
CHANNELS = 1         
RATE = 50000         # samples per second
OBSERVERFREQ = float(input("freq"))



p = pyaudio.PyAudio()


stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE)


while True:
   
    data = stream.read(CHUNK_SIZE)


    samples = np.frombuffer(data, dtype=np.int16)


    freqs = fft(samples)


    max_freq = np.argmax(np.abs(freqs))


    freq_hz = max_freq * RATE / CHUNK_SIZE

    # Print the frequency in Hz
    z = 343/freq_hz
    y = z*OBSERVERFREQ
    x = y-343
    strx = str(x)
    strhz = str(freq_hz)
    print("M/S = " + strx + " HZ = " + strhz)

    time.sleep(0.01)
