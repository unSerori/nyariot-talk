'''
鯖側のメイン
vv鯖を立て、鯖が立ったら会話の処理を開始する。
録音し音声ファイルを生成、書き起こし、GPTに投げ、VVに投げ音声ファイルを生成、再生。
'''

# ぬいぐるみ側で音を拾う。投げる
# サバ側で受け取る
#     通信はwifi？
# 受け取った音声を再生

# サーバー起動
# 音声を受け取る
# 文字起こし
# chatGPTに投げる。テキストが帰ってくる
# テキストを、クエリデータ生成してvv_engineに投げる
# 生成物をクライアントに投げて再生してもらう




# もじゅーるいんぽーと
import os  # パス確認
import subprocess  # system()でバッチを起動
import requests  # 鯖の疎通確認
# import socket  # 鯖の疎通確認
import time  # 一時停止
# 自作もじゅーる
import recording  # 録音する
import vv_transcribe_audio  # 文字起こし speech_recognition 速度重視
import vv_transcribe_audio_whisper  # 文字起こし whisper 精度重視
import nyariot_talk  # チャットGPTに投げる
import vv_gen_afile  # テキストを、クエリデータ生成してvv_engineに投げる
# import vv_nogen_afile  # テキストを、クエリデータ生成してvv_engineに投げる
import play_audio_test  # 音声を再生




# パスの確認
print("path")  # os.chdir()
print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())
print("__file__: 実行ファイルの絶対パス: " + __file__)
print("os.path.dirname(__file__): 実行ファイルのディレクトリの絶対パス: " + os.path.dirname(__file__))
print("os.path.basename(__file__): 実行ファイルのファイル名: " + os.path.basename(__file__))

os.chdir(os.path.dirname(__file__))  # カレントディレクトリを実行ファイルのパスに変更。以降のパスは実行ファイルからの相対パスを書く
print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())  # カレントディレクトリ確認 # debug

# サーバー起動
subprocess.Popen(["start", "run-vv_engine.bat"], shell=True)  # バッチ起動
engine_port = 50021


# リクエストを送り正常起動していれば次の処理に進む
while True:
    try:
        print("応答を待機しています...")
        engine_info = requests.get(f"http://127.0.0.1:{engine_port}/supported_devices")
        print(engine_info)
        if engine_info.status_code == 200:
            engine_device_info = engine_info.json()
            break
        time.sleep(1)
    except:
        pass


print("本処理開始＾～\n") # debug


# 全体をwhileで回し続ける
while True:
    # 録音 本来は # 音声を受け取る******************
    recording.recording_audio()


    # 文字起こし
    # recog_text = vv_transcribe_audio.recog_input_voice()  # テキストデータにしてもらう
    recog_text = vv_transcribe_audio_whisper.recog_input_voice()  # テキストデータにしてもらう


    if recog_text:  # 変数の中身が存在するなら
        # chatGPTに投げる。テキストが帰ってくる
        chat_text = nyariot_talk.talk_GPT(recog_text)
        print("debug: recog_text: " + recog_text)  # debug
        print("debug: chat_text: " + chat_text)  # debug

        # テキストを、クエリデータ生成してvv_engineに投げる
        vv_gen_afile.talk_vv_gen_afile(chat_text)

        # 再生しとく 本来は # 生成物をクライアントに投げて再生してもらう******************
        play_audio_test.play_wav_audio("vv_voice.wav")

    else:   # 文字起こせなかったらchatGPTをスキップ
        chat_text = "ごめん、よく聞こえなかった" 
        print("debug: chat_text: " + chat_text + " (エラー)")  # debug

        # 再生しとく 本来は # 生成物をクライアントに投げて再生してもらう******************
        play_audio_test.play_wav_audio("vv_voice_could_not_be_transcribed.wav")


    print("\n")  # ループ毎の改行