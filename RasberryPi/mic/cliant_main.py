# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import time

import mik

# Multi Process import
from concurrent.futures import ThreadPoolExecutor


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
        except KeyboardInterrupt:
            print("Error")
            observer.stop()
        observer.join()

with ThreadPoolExecutor(2) as executor:
     executor.submit(mik.record)
     executor.submit(fileCheckObserver)