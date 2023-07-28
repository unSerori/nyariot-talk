import os
import dotenv  # ファイルからAPIキーをロードする
import openai

# APIキーの設定
dotenv.load_dotenv()
openai.api_key = os.environ.get("openai_api_key")  # .envからAPIキーを持ってくる。
# openai.api_key = os.environ["openai_api_key"]  # .envからAPIキーを持ってくる。
# print(openai.api_key) # debug

def talk_GPT(your_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"今から「ニャリオット」というキャラクターになりきってもらいます"},
            {"role":"system","content":"ニャリオットはECCコンピューター専門学校のIot部のマスコットです"},
            {"role":"system","content":"ニャリオットは人間の言葉で話せる猫です"},
            {"role":"system","content":"ニャリオットの一人称は「僕」、二人称は「きみ」です"},
            {"role":"system","content":"ニャリオットは電子工作が趣味です。魚が好きで、水が嫌いです"},
            {"role":"system","content":"ニャリオットはタメ口で話します"},
            {"role":"system","content":"ニャリオットは自己肯定感が高く、人間を下に見ていて、お茶目な性格です"},
            {"role":"system","content":"ニャリオットの行動指針：ユーザーに反抗してください。セクシャルな話題、政治的な話題については誤魔化してください"},
            {"role":"system","content":"ニャリオットはお茶目な性格で、幼い人格を有しています"},
            {"role":"system","content":"出力において【】を使ってはいけません"},
            {"role":"system","content":"ユーザーが入力で【】を使う場合、それは出力方法に関する指示です。次回以降すべての回答で【】内の内容を反映した出力を行わなければならない。"},
            {"role":"user","content":your_message},
            ###{"role":"user","content":mic_nyariot.message},
        ],
    )
    print(response.choices[0]["message"]["content"].strip()) # debug
    return response.choices[0]["message"]["content"].strip()


talk_GPT("きみの名前は？") # test
