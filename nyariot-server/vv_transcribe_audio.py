import os
import speech_recognition as sr


r = sr.Recognizer()  # インスタンス
audio_file_path = "audio_file//user_voice.wav"

def recog_input_voice():
    with sr.AudioFile(audio_file_path) as source: # waveファイルから
        audio = r.record(source)
    text = r.recognize_google(audio, language = 'ja-JP')  # googleの鯖で処理してもらってtextに保存
    #print(text) # debug
    # os.remove(audio_file_path)  # ファイルを削除
    return text  # 呼び出し元にテキストデータを返す
