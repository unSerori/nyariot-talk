#ESP32-PC間通信用プログラム(PC側)
#socketライブラリをインポート
import socket
import time
import pygame
import numpy as np
import scipy

ip_address = '192.168.2.149' #サーバー（ESP32のIPアドレス）
port = 5000 #ポート番号
buffer_size = 4096 #一度に受け取るデータの大きさを指定

recieve_message = ""
recieve_status = True

#クライアント用インスタンスを生成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバーに接続を要求する（IPアドレスとポート番号を指定）
client.connect((ip_address, port))

def strToIntArray (strData, recData):
  strData = str(strData)
  data = ""
  for string in strData:
    if (string in "0123456789"):
      data += string
    elif (data != ""):
      intData = int(data)
      recData.append(intData)
      data = ""
    else:
      if(string == "!"):
        print(recData)
        print(len(recData))
        print("finish")
        recData = ""
  return recData

recData = []
sendVoice = False
voice = "konnitiha! genki? kyoumo itiniti ganbarou ne!"

recDataHold = 0

while(True):
  if (sendVoice):
    # サーバにデータを送信する
    message = voice    #input("送信するメッセージを入力してください\n→")
    message += "\n"#文末に改行コードを追加
    client.sendall(bytes(message, encoding='utf_8'))#文字列をバイトに変換し送信（文字コードはASCIIを使用）
    print("サーバーへデータ送信")

  #サーバーからの応答を受信
  print("waiting...")
  data = (client.recv(buffer_size)) #サーバから送られてきたデータを読み取り（上限4096ビット）
  print("get")
  if(data != ""):
    data = data.decode()
    #print("サーバからのメッセージ")
    #print(data)   #受け取ったデータ（バイト形式）を読める形式にデコードして表示
    strToIntArray(data, recData)
    data = ""