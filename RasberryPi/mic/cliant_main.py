# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import time

import datetime
import sys

import mik
import speaker

import base64
import responder

from http.server import *

# Multi Process import
from concurrent.futures import ThreadPoolExecutor

ip = "0.0.0.0"
port = 8887

httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
httpd.serve_forever()


def file_receive():
    @api.route("/")
    async def on_post(req, resp):
        data = await req.media()
        data_bytes = base64.b64decode(data['file'].encode())

        with open("wav_file.wav", 'bw') as f:
            f.write(data_bytes)

# FileSystemEventHandler の継承クラスを作成
class FileChangeHandler(FileSystemEventHandler):
    # ファイル作成時のイベント
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s created' % filename)

    # ファイル変更時のイベント
    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s changed' % filename)

        client(ip_address, port, filepath)

    # ファイル削除時のイベント
    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s deleted' % filename)

    # ファイル移動時のイベント
    def on_moved(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s moved' % filename)

# コマンド実行の確認
def fileCheckObserver():
    if __name__ == "__main__":
        # 監視対象ディレクトリを指定する
        target_dir = './audio_file/to_server'
        # ファイル監視の開始
        event_handler = FileChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, target_dir, recursive=True)
        observer.start()
        # 処理が終了しないようスリープを挟んで無限ループ
        try:
            while True:
                time.sleep(0.1)
                if(speak_mode):
                    speaker.speak()
        except KeyboardInterrupt:
            print("Error")
            observer.stop()
        observer.join()




if __name__ == "__main__":
    run_http_server()

with ThreadPoolExecutor(3) as executor:
    executor.submit(mik.record)
    executor.submit(fileCheckObserver)
    executor.submit(file_receive)
