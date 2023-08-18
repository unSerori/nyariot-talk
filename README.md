# nyariot-talk
## 概要
音声が一定以上の大きさであれば録音が開始され、「ニャリオット」が返事をしてくれる。会話ができます！


## 環境構築
1.
"nyariot-server/audio_file": 子機から送られてくる音声ファイルを保存しておく

2.
"nyariot-server/virtualenv_nyariot-server": 仮想環境はvirtualenvで作成。
パッケージはrequirements.txtから入れてください。

3.
"nyariot-server/voicevox_engine/windows-cpu": エンジンは [https://github.com/VOICEVOX/voicevox/releases/tag/0.14.7] からビルド済みのvoicevox_engine-windows-cpu-0.14.5.7z.001 を使わせていただいた。
環境にあったものをかりよう！解凍&リネームしておく。
gpuを使いたい場合は「windows-cpuのフォルダ名」と「nyariot-server/run-vv_engine.batの5行目set "run_path=voicevox_engine/windows-cpu"」を適宜変更。

4.
whisperを動かすために、ffmpeg本体(ビルド済みのbin/ffmpeg.exe)のインストールとパスを通す必要がある

5.
whisperが出力を次のプロンプトへ継続的に引用できるように(精度を高めるために)、whisper/transcribe.pyの中身を
```python:書き換え
- decode_options["prompt"] = all_tokens[prompt_reset_since:]
+ decode_options["prompt"] = initial_prompt_tokens

```
変更した。


## 使い方
server_main.pyを起動するとvv鯖が立ち上がる。
1.一定以上の大きさの声で話すと録音され、一定以下になると録音終了。
2.文字に書き起こし、vv鯖に投げられ返ってきた音声を再生する。
3.1~2を繰り返す。