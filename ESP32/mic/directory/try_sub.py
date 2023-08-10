import os



def sub():
    print("path")  # os.chdir()
    print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())
    print("__file__: 実行ファイルの絶対パス: " + __file__)
    print("os.path.dirname(__file__): 実行ファイルのディレクトリの絶対パス: " + os.path.dirname(__file__))
    print("os.path.basename(__file__): 実行ファイルのファイル名: " + os.path.basename(__file__))



'''def sub():
    print("path")  # os.chdir()
    print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())
    print("__file__: 実行ファイルの絶対パス: " + __file__)
    print("os.path.dirname(__file__): 実行ファイルのディレクトリの絶対パス: " + os.path.dirname(__file__))
    print("os.path.basename(__file__): 実行ファイルのファイル名: " + os.path.basename(__file__))

    os.chdir("C:/")
    
    # パスの確認
    print("path")  # os.chdir()
    print("os.getcwd(): カレントディレクトリ(コマンドの実行場所の絶対パス): " + os.getcwd())
    print("__file__: 実行ファイルの絶対パス: " + __file__)
    print("os.path.dirname(__file__): 実行ファイルのディレクトリの絶対パス: " + os.path.dirname(__file__))
    print("os.path.basename(__file__): 実行ファイルのファイル名: " + os.path.basename(__file__))
'''