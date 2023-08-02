#ESP32-PC間通信用プログラム(PC側)
#socketライブラリをインポート
import socket
ip_address = '10.200.5.160' #サーバー（ESP32のIPアドレス）
port = 5000 #ポート番号
buffer_size = 4092 #一度に受け取るデータの大きさを指定
recieve_message = "Hello! ESP32!"
recieve_status = True
#クライアント用インスタンスを生成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバーに接続を要求する（IPアドレスとポート番号を指定）
client.connect((ip_address, port))
while (True):
    # サーバにデータを送信する
    message = input("送信するメッセージを入力してください\n→")
    message += "\n"#文末に改行コードを追加
    client.sendall(bytes(message, encoding='ASCII'))#文字列をバイトに変換し送信（文字コードはASCIIを使用）
    print("サーバーへデータ送信")
    #サーバーからの応答を受信
    data = client.recv(buffer_size) #サーバから送られてきたデータを読み取り（上限4092ビット）
    print("サーバからのメッセージ")
    print(data.decode())#受け取ったデータ（バイト形式）を読める形式にデコードして表示