# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import time

import datetime
import sys


#socketライブラリをインポート
import socket
ip_address = '192.168.10.115' #サーバー
port = 5000 #ポート番号
buffer_size = 4092 #一度に受け取るデータの大きさを指定

import mik
import speaker

# Multi Process import
from concurrent.futures import ThreadPoolExecutor

recieve_message = ""
recieve_status = True
#クライアント用インスタンスを生成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバーに接続を要求する（IPアドレスとポート番号を指定）
client.connect((ip_address, port))

speak_mode = False

def client(ip, port, fname):    #ファイル送信
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        try:
            with open(fname, mode='rb') as f:
                for line in f:
                    s.sendall(line)
                    data = s.recv(1024)
                print(repr(data.decode()))
        except:
            pass

def server(ip, port, ext):    #ファイル受信
    output_list = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                dt_now = datetime.datetime.now()
                fname = "./audio_file/from_server/nyariott." + ext
                with open(fname, mode="ab") as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        conn.sendall(b'Received done')
                    speak_mode = True
                    exit()

def file_receive():
    while True:
        server(ip_address, port, 'wav')

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

with ThreadPoolExecutor(3) as executor:
    executor.submit(mik.record)
    executor.submit(fileCheckObserver)
    executor.submit(file_receive)