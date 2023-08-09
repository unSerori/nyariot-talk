'''
文字起こし
返り血は文字列
'''

import os
import speech_recognition as sr


r = sr.Recognizer()  # インスタンス
# os.chdir(os.path.dirname(__file__))  # カレントディレクトリを実行ファイルのパスに変更。以降のパスは実行ファイルからの相対パスを書くだけでいい。
# audio_file_path = os.path.dirname(__file__).replace(os.sep, "/") + "/audio_file/from_client/user_voice.wav"
audio_file_path = "audio_file/from_client/user_voice.wav"  # 出力先の設定


def recog_input_voice():
    try:
        with sr.AudioFile(audio_file_path) as source: # waveファイルから
            audio = r.record(source)
        text = r.recognize_google(audio, language = 'ja-JP')  # googleの鯖で処理してもらってtextに保存
        # print(text) # debug
        return text  # 呼び出し元にテキストデータを返す
    except sr.UnknownValueError as e:  # 文字起こしできなかった場合
        # エラーメッセージ
        print(e)
        print(type(e))
        return ""


    os.remove(audio_file_path)  # ファイルを削除


if __name__ == "__main__":
    recog_text = recog_input_voice() # text   
    if not recog_text:
        print("error")  # continue
    else:
        print(recog_text)