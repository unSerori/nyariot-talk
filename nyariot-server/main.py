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




import os  # system()でバッチを起動
import socket  # 鯖の疎通確認
import time  # 一時停止

import vv_transcribe_audio  # 文字起こし




# サーバー起動
command = "start" + " " + "run-vv_engine.bat"  # start + バッチファイルへのパス + args
os.system(command)  # バッチ起動

time.sleep(5)

# リクエストを送り正常起動していれば次の処理に進む
connection = True
while socket.socket().accept():
    try:
        server = socket.socket().connect(("localhost", 50021))  # withは確実なリソース開放が目的っぽい。接続出来たらbreakして以降の処理に移る
        connection, address = socket.accept()
        connection = (connection == False)
    except socket.error as e:
        time.sleep(1)


# 全体をwhileで回し続ける
'''while True:
    hoge
'''
# 音声を受け取る


# 文字起こし
recog_text = vv_transcribe_audio.recog_input_voice()  # テキストデータにしてもらう
print(recog_text) # debug


# chatGPTに投げる。テキストが帰ってくる


# テキストを、クエリデータ生成してvv_engineに投げる
