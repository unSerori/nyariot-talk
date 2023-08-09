import pyaudio
import wave
import numpy as np

threshold = 0.03
thresholdmin = 0.02
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
blank = 1
p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,                            #(1)
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = chunk
    )

sound=[]
def record_sample():
    while True:
        data = stream.read(chunk)                                      #(2)
        x = np.frombuffer(data, dtype="int16") / 32768.0
        if x.max() > threshold:        
            print("Start recording!")  # Start                            #(3)
            rec = 0
            filename = "test.wav"
            sound=[]
            sound.append(data)
            while rec < int(blank * RATE / chunk):
                data = stream.read(chunk)
            
                sound.append(data)
                x = np.frombuffer(data, dtype="int16") / 32768.0
                if x.max() < thresholdmin:                               #(4)
                    rec += 1
                else:
                    rec = 0
            
            data = b''.join(sound)
        
            out = wave.open(filename,'w')                              #(5)
            out.setnchannels(CHANNELS)
            out.setsampwidth(2)
            out.setframerate(RATE)
            out.writeframes(data)
            out.close()
            print("Finished recording!")  # Enddddddddddddddddddddddddddddd

            break

    stream.close()
    p.terminate()

record_sample()
