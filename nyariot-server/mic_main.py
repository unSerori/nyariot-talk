import pyaudio
import wave
import numpy as np
import time

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz　サンプリング周波数
chunk = 4096 # 2^12 一度に取得するデータ数
record_secs = 5 # 録音する秒数
dev_index = 0 # デバイス番号
wav_output_filename = 'nyariot-server/audio_file/from_client/user_voice.wav' # 出力するファイル
blank = 1 #録音して一定の音量以下になったときに抜けるまでの秒数

threshold = 0.5     #開始音量0.9
thresholdmin = 0.1  #終了音量0.4

audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
'''こっちだと動かない？
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
'''
stream = audio.open(format = form_1,channels = chans,rate = samp_rate, \
                    input = True, frames_per_buffer=chunk)
print("active")

#print("recording")
'''
frames = []

data = 0

# loop through stream and append audio chunks to frame array
for i in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    frames.append(data)
    #print(data)
'''

def record():
    while True:
        data = stream.read(chunk)                                      
        x = np.frombuffer(data, dtype="int16") / 32768.0
        if x.max() > threshold:  
            print("Recording")
            rec = 0
            sound=[]
            sound.append(data)
            while rec < int(blank * samp_rate / chunk):
                data = stream.read(chunk)
            
                sound.append(data)
                x = np.frombuffer(data, dtype="int16") / 32768.0
                if x.max() < thresholdmin:                               
                    rec += 1
                else:
                    rec = 0
        
            out = wave.open(wav_output_filename,'w')                              
            out.setnchannels(chans)
            out.setsampwidth(audio.get_sample_size(form_1))
            out.setframerate(samp_rate)
            out.writeframes(b''.join(sound))
            out.close()
            
            print("Finished recording")
            break
        
        # stop the stream, close it, and terminate the pyaudio instantiation
        #stream.stop_stream()
        #stream.close()
        #audio.terminate()
        #print("Ctrl + C が押されました。ループを終了します。")

'''
# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
'''