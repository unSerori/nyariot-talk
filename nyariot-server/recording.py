'''
マイクで録音
返り血なし、音声ファイルを生成
閾値を設定して録音、音量が閾値を下回ると終了
'''

import os
import pyaudio
import wave
import numpy as np  # なんか表示出る




# 定数
threshold = 0.25  # 開始の閾値
threshold_min = 0.05  # 終了の閾値
'''
自室: PC: 0.25: 0.05
自室: イヤホンマイク: 
うるさめの部屋: PC: 
うるさめの部屋: イヤホンマイク: 
'''
chunk = 4096  # 2^12 一度に取得できるデータ上限4096
format_paInt = pyaudio.paInt16  # 16bit resolution
channel = 1  # 1 channel
samp_rate = 44100  # サンプリングレート 44.1kHz
file_path_output = "audio_file/from_client/user_voice.wav"  # 出力先の指定
blank = 1  # 終了の閾値を下回ったあと何秒で切るか
input_device = 2  # 

p = pyaudio.PyAudio()  # インスタンス


# 定数定義した設定群からstreamオブジェクトをつくる
stream = p.open(format=format_paInt, 
                channels=channel,
                rate=samp_rate,
                input=True,
                frames_per_buffer=chunk
                )
#input_device_index=input_device,

'''
# デフォルトのデバイス確認
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))
'''
# print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())  # カレントディレクトリ確認 # debug

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))  # カレントディレクトリを実行ファイルのパスに変更。以降のパスは実行ファイルからの相対パスを書く

def recording_audio():
    print("active")  # 録音準備完了
    while True:
        data = stream.read(chunk)                               
        x = np.frombuffer(data, dtype = "int16") / 32768.0  # 読み取ったデータを[-1, 1]の範囲に正規化するため。スケールダウン

        if x.max() > threshold:  # 閾値より大きければ録音開始
            print("Start recording!")  # Startttttttttttttttttttttttttttttttt

            rec = 0  # データの上限をカウントする？
            sound = []  # 録音データをフレームで保存するためのリスト
            sound.append(data)

            while rec < int(blank * samp_rate / chunk):
                data = stream.read(chunk)

                sound.append(data)
                x = np.frombuffer(data, dtype="int16") / 32768.0
                if x.max() < threshold_min:
                    rec += 1  # 閾値を下回ったらカウント増加
                else:
                    rec = 0  # 閾値を上回ったらカウントをリセット
            # print(p.get_sample_size(format_paInt))  # debug
            # 書き出し処理
            wf = wave.open(file_path_output, 'w')
            wf.setnchannels(channel)
            wf.setsampwidth(p.get_sample_size(format_paInt))
            wf.setframerate(samp_rate)
            wf.writeframes(b''.join(sound))
            wf.close()

            print("Finished recording!")  # Enddddddddddddddddddddddddddddd
            break

        
    # stream.close()  # ここで破棄すると、次回ループでオブジェクトがないなるのでOSError [Errno -9988] Stream closed がでちゃう。
    # p.terminate()


if __name__ == "__main__":
    recording_audio()



'''
import sounddevice as sd  # マイクを使いたい
import numpy as np  # なんか表示出る
import soundfile as sf  # NumPy配列である録音信号をwav形式で保存する



def recording_audio_():
    os.chdir(os.path.dirname(__file__))  # カレントディレクトリを実行ファイルのパスに変更。以降のパスは実行ファイルからの相対パスを書くだけでいい。


    duration = 6  # 10秒間収音する


    # デフォルトのデバイス確認
    device_list = sd.query_devices()
    print(device_list)

    for device_number in sd.default.device:
        print(device_number)
        print(device_list[device_number])

    print(sd.default.device)
    sd.default.device = [1, 3]  # IN OUT 変更
    print(sd.default.device)
    input_device_info = sd.query_devices(device=sd.default.device[1])
    sr_in = int(input_device_info["default_samplerate"])


    print("録音開始！") # debug
    # 録音
    myrecording = s2d.rec(int(duration * sr_in), samplerate=sr_in, channels=2)
    sd.wait() # 録音終了待ち

    print(myrecording.shape) #=> (duration * sr_in, channels)

    # 録音信号のNumPy配列をwav形式で保存
    sf.write("audio_file/from_client/user_voice.wav", myrecording, sr_in)
'''