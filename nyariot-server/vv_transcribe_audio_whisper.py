'''
文字起こし
返り血は文字列
'''

import whisper  # オフライン書き起こし
import os  # カレントディレクトリ変更
import time  # 計測用
'''
import whisper  # インポート
model = whisper.load_model("tiny")  # モデル指定
result = model.transcribe("example.mp3")  # 音声ファイルから文字お越しし、変数に格納
print(result["text"])  # 表示
'''




if __name__ == "__main__":  # カレントディレクトリを変更
    os.chdir(os.path.dirname(__file__))  # カレントディレクトリを実行ファイルのパスに変更。以降のパスは実行ファイルからの相対パスを書く
    print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())  # カレントディレクトリ確認 # debug


audio_file_path = "audio_file/from_client/user_voice.wav"  # 出力先の設定
models_path = "virtualenv_nyariot-server/Lib/site-packages/whisper/models"
lang = "ja"  # 言語設定

model_type = "large"  # モデルを指定。tiny, base, small, medium, large
model = whisper.load_model(model_type, download_root=models_path)  # そのモデルで設定


# 辞書
dictionary = ""
dictionary = dictionary + ""  # 挨拶


def recog_input_voice():
    # text = model.transcribe(audio_file_path, verbose=True, language=lang, initial_prompt=dictionary, condition_on_previous_text=True)["text"]  # 書き起こした結果をtextに入れる ファイルパス, 進行状況やデバックメッセージの出力有無, 言語設定, プロンプト(辞書), 次のウィンドウのプロンプトとしてモデルの前の出力を提供する(true)
    print("model_type: " + model_type)  # model
    
    time_start = time.time()  # 計測
    text = model.transcribe(audio_file_path, verbose=True, language=lang, initial_prompt=dictionary, condition_on_previous_text=True, fp16=False)["text"]  # 書き起こした結果をtextに入れる ファイルパス, 進行状況やデバックメッセージの出力有無, 言語設定, プロンプト(辞書), 次のウィンドウのプロンプトとしてモデルの前の出力を提供する(true)
    print(str(round(time.time() - time_start, 2)) + "s")  # かかった時間
    print()  # 改行
    return text




if __name__ == "__main__":
    recog_text = recog_input_voice()
    if recog_text:
        print("debug: recog_text: " + recog_text)  # debug
    else:
        chat_text = "ごめん、よく聞こえなかった" 
        print("debug: chat_text: " + chat_text + " (エラー)")  # debug
