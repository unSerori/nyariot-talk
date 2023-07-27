# ぬいぐるみ側で音を拾う。投げる
# サバ側で受け取る
#     通信はwifi？
# 受け取った音声を再生

# サーバー起動
# 音声を受け取る
# 文字起こし
# chatGPTに投げる。テキストが帰ってくる
# テキストを、クエリデータ生成してvv_engineに投げる
# 生成物を子機に投げて再生してもらう


import subprocess  # system()でバッチを起動
import requests
import socket  # 鯖の疎通確認
import time  # 一時停止

import vv_transcribe_audio  # 文字起こし




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


# 全体をwhileで回し続ける
while True:
    # 音声を受け取る


    # 文字起こし
    recog_text = vv_transcribe_audio.recog_input_voice()  # テキストデータにしてもらう
    print(recog_text) # debug


    # chatGPTに投げる。テキストが帰ってくる


    # テキストを、クエリデータ生成してvv_engineに投げる
