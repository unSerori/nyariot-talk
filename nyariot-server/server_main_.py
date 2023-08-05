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
import vv_transcribe_audio  # 文字起こし
import nyariot_talk  # チャットGPTに投げる
import vv_transcribe_audio  # vv鯖に投げて音声ファイルを作る
import vv_gen_afile  # テキストを、クエリデータ生成してvv_engineに投げる
# import vv_nogen_afile  # テキストを、クエリデータ生成してvv_engineに投げる
import play_audio_test  # 音声を再生




# パスの確認
print("path")  # os.chdir()
print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())
print("__file__: 実行ファイルの絶対パス: " + __file__)
print("os.path.dirname(__file__): 実行ファイルのディレクトリの絶対パス: " + os.path.dirname(__file__))
print("os.path.basename(__file__): 実行ファイルのファイル名: " + os.path.basename(__file__))

os.chdir(os.path.dirname(__file__))  # カレントディレクトリを実行ファイルのパスに変更。以降のパスは実行ファイルからの相対パスを書くだけでいい。
print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())  # カレントディレクトリ確認


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


print("本処理開始＾～") # debug


# 全体をwhileで回し続ける
while True:
    # 録音 本来は # 音声を受け取る******************
    recording.recording_audio()


    # 文字起こし
    recog_text = vv_transcribe_audio.recog_input_voice()  # テキストデータにしてもらう
    print("debug: recog_text: " + recog_text)  # debug
    if not recog_text:  # 文字起こせなかったら次ループに逃げる
        continue


    # chatGPTに投げる。テキストが帰ってくる
    chat_text = nyariot_talk.talk_GPT(recog_text)
    print("debug: chat_text: " + chat_text)  # debug


    # テキストを、クエリデータ生成してvv_engineに投げる
    vv_gen_afile.talk_vv_gen_afile(chat_text)


    # 再生しとく 本来は # 生成物をクライアントに投げて再生してもらう******************
    play_audio_test.play_wav_audio()

    input("pause")

    # 書き起こしの際削除