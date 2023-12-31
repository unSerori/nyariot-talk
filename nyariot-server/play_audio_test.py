'''
録音の再生
返り血はなし
'''

import pyaudio  # オーディオ処理
import wave  # wavの再生


def play_wav_audio(file_name):
    # パスを置いとく
    file_path = "audio_file/to_client/"
    CHUNK = 1024

    # ファイルがあるかどうかを見る
    try:
        wf = wave.open(file_path + file_name, "r")
    except FileNotFoundError: #ファイルが存在しなかった場合
        print("[Error 404] No such file or directory: " + file_path)
        return 0
    

    # ストリームを開く
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # 音声を再生
    data = wf.readframes(CHUNK)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.close()
    p.terminate()
    return


"""
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

"""