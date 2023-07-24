# nyariot-talk
仮想環境はvirtualenvで virtualenv_nyariot-serverとして作成。
パッケージはrequests, pyaudio, などを入れた

エンジンは[https://github.com/VOICEVOX/voicevox/releases/tag/0.14.7]からビルド済みのvoicevox_engine-windows-cpu-0.14.5.7z.001 を使わせていただいた。
解凍してvoicevox_engineとした。

鯖起動用
run.exe --host 0.0.0.0 --allow_origin *