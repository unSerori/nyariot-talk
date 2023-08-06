'''
処理時間を計測する。
'''

# もじゅーるいんぽーと
import time  # 計測
# 自作もじゅーる
import vv_gen_afile  # vvにリクエストを送る


number_of_trials = 5000  # 試行回数

# 開始時刻(エポック秒)を記録
start_time = time.time()


# 計測したい処理
for i in range(number_of_trials):
    vv_gen_afile.talk_vv_gen_afile("こんにちは！元気？今日も一日頑張ろうね！今日が当日だよ！")
    print(i)  # 回数を表示


# 実行時間(s) = 終了時刻 - 開始時刻
Execution_time = time.time() - start_time
print("Measurement result: " + str(Execution_time) + "s")
print("Seconds per operation" + str(Execution_time / number_of_trials) + "s")