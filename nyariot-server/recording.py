import sounddevice as sd  # マイクを使いたい
import numpy as np  # 
import soundfile as sf  # 


duration = 10  # 10秒間収音する


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


def recording_audio():
    while True:
        # 録音
        myrecording = sd.rec(int(duration * sr_in), samplerate=sr_in, channels=2)
        sd.wait() # 録音終了待ち

        print(myrecording.shape) #=> (duration * sr_in, channels)

        # 録音信号のNumPy配列をwav形式で保存
        sf.write("audio_file/from_client/user_voice.wav", myrecording, sr_in)