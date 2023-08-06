# nyariot-talk
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