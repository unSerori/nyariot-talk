import os
## import mic_nyariot
import openai

# APIキーの設定
openai.api_key = "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"

def talk_GPT(your_messeage):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"あなたは人間の言葉で話せる猫です"},
            {"role":"system","content":"一人称は僕、二人称はきみ"},
            {"role":"system","content":"電子工作についての知識を有しています"},
            {"role":"system","content":"自己肯定感が高く、人間を下に見ています"},
            {"role":"system","content":"お茶目な性格です"},
            {"role":"user","content":your_messeage},
            ##{"role":"user","content":mic_nyariot.message},
        ],
    )
    print(response.choices[0]["message"]["content"].strip())