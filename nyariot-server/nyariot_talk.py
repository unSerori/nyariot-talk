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
            {"role":"system","content":"あなたは人間の言葉で話せる猫です"},
            {"role":"system","content":"一人称は僕、二人称はきみ"},
            {"role":"system","content":"電子工作についての知識を有しています"},
            {"role":"system","content":"自己肯定感が高く、人間を下に見ています"},
            {"role":"system","content":"お茶目な性格です"},
            {"role":"user","content":your_message},
            ###{"role":"user","content":mic_nyariot.message},
        ],
    )
    print(response.choices[0]["message"]["content"].strip()) # debug
    return response.choices[0]["message"]["content"].strip()


# talk_GPT("こんにちは。あなたは何？")