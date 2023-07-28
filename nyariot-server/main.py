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
import requests  # 鯖の疎通確認
# import socket  # 鯖の疎通確認
import time  # 一時停止

import vv_transcribe_audio  # 文字起こし
import nyariot_talk  # チャットGPTに投げる
import vv_transcribe_audio  # vv鯖に投げて音声ファイルを作る
import vv_gen_afile  # テキストを、クエリデータ生成してvv_engineに投げる
# import vv_nogen_afile  # テキストを、クエリデータ生成してvv_engineに投げる


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

print("hoge")

'''# 全体をwhileで回し続ける
while True:
    # 音声を受け取る
    # input("音声が来るまで待機。")

    # 文字起こし
    recog_text = vv_transcribe_audio.recog_input_voice()  # テキストデータにしてもらう
    print(recog_text)  # debug


    # chatGPTに投げる。テキストが帰ってくる
    chat_text = nyariot_talk.talk_GPT(recog_text)
    print(chat_text)  # debug

    # テキストを、クエリデータ生成してvv_engineに投げる
    #vv_gen_afile.talk_vv_gen_afile(chat_text)'''