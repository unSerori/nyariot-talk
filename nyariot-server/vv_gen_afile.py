import requests # API
import json # APIで取得したJSONデータの処理


# チャットからもらった値を入れて鯖に投げる
# text = "こんにちは！元気？今日も一日頑張ろうね！"
def talk_vv_gen_afile(text):
    # 音声合成クエリの作成
    res1 = requests.post('http://127.0.0.1:50021/audio_query',params = {'text': text, 'speaker': 8})
    # 音声合成データの作成
    res2 = requests.post('http://127.0.0.1:50021/synthesis',params = {'speaker': 8},data=json.dumps(res1.json()))


    # wavデータの生成
    with open('test.wav', mode='wb') as f:
        f.write(res2.content)


# test
talk_vv_gen_afile("こんにちは")