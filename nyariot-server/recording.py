'''
マイクで録音
返り血なし、音声ファイルを生成
'''

import os
import sounddevice as sd  # マイクを使いたい
import numpy as np  # なんか表示出る
import soundfile as sf  # NumPy配列である録音信号をwav形式で保存する

def recording_audio():
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
    myrecording = sd.rec(int(duration * sr_in), samplerate=sr_in, channels=2)
    sd.wait() # 録音終了待ち

    print(myrecording.shape) #=> (duration * sr_in, channels)

    # 録音信号のNumPy配列をwav形式で保存
    sf.write("audio_file/from_client/user_voice.wav", myrecording, sr_in)


if __name__ == "__main__":
    recording_audio()