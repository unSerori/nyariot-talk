from prettytable import PrettyTable
import requests
import time
import json
import os,sys
import subprocess

def yes_no_input(text):
    while True:
        choice = input(text).lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            return None

config_path = "config.json"
default_json = {
    "engine_path":"voicevox_engine/windows-cpu/run.exe",
    "port":50021,
    "use_gpu":False,
    "default_spaker_id":18,
    "use_default":False,
    "stop_keyword":"stop",
    "cpu_engine_download_url":"https://github.com/VOICEVOX/voicevox_engine/releases/download/0.13.3/windows-cpu.7z.001",
    "gpu_engine_download_url":"https://github.com/VOICEVOX/voicevox_engine/releases/download/0.13.3/windows-nvidia.7z.001"
}

if os.path.exists(config_path):
    try:
        with open(config_path,"r",encoding="utf-8") as read_config:
            setting_json = json.load(read_config)
    except:
        setting_json = default_json
else:
    with open(config_path,"w",encoding="utf-8") as write_config:
        json.dump(default_json,write_config)

    setting_json = default_json

reset_config = False
stop_app = False
while True:
    if reset_config:
        with open(config_path,"w",encoding="utf-8") as write_config:
            json.dump(default_json,write_config)

        setting_json = default_json
    try:
        engine_path = os.path.abspath(default_json["engine_path"])
        engine_port = setting_json["port"]
        stop_keyword = setting_json["stop_keyword"]
        use_default = setting_json["use_default"]
        default_id = setting_json["default_spaker_id"]
        break
    except:
        while True:
            ask_reset_config = yes_no_input("configの読み込みに失敗しました、configを再生成しますか? [y/n]")
            if ask_reset_config == None:
                continue
            elif ask_reset_config:
                reset_config = True
                break
            else:
                stop_app = True
                break
    if stop_app:
        break

if stop_app:
    sys.exit(1)

command_list = [engine_path,"--port",str(engine_port)]

session = requests.session()
print("エンジンを起動しています...")
engine_proc = subprocess.Popen(command_list,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

while True:
    try:
        print("応答を待機しています...")
        engine_info = session.get(f"http://127.0.0.1:{engine_port}/supported_devices")
        if engine_info.status_code == 200:
            engine_device_info = engine_info.json()
            break
        time.sleep(1)
    except:
        pass

can_gpu = False
table = PrettyTable(['デバイス','使用可能か'])
for key in engine_device_info.keys():
    if engine_device_info[key]:
        table.add_row([key,"使用可能"])
    else:
        table.add_row([key,"使用不可能"])

    if engine_device_info["cuda"]:
        can_gpu = True

print(table)

while True:
    if can_gpu and setting_json["use_gpu"]:
        cuda_question = yes_no_input("CUDAを使用しますか? [y/n]\n>>>")
        if cuda_question == None:
            continue
        elif cuda_question:
            print("エンジンを再起動しています...")
            command_list.append("--use_gpu")
            engine_proc.kill()
            engine_proc.wait()
            engine_proc = subprocess.Popen(command_list,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            break
        else:
            break
    else:
        break

while True:
    try:
        print("エンジンの情報を取得しています...")
        speakers_res = session.get(f"http://localhost:{engine_port}/speakers")
        if speakers_res.status_code == 200:
            speakers = speakers_res.json()
            break
        time.sleep(1)
    except:
        pass

table_list = []
table = PrettyTable(['ID','名前',"スタイル"])

for speaker in speakers:
    speaker_name = speaker["name"]

    for speaker_style in speaker["styles"]:
        add_list = []

        style_id = speaker_style["id"]
        style_name = speaker_style["name"]

        add_list.append(style_id)
        add_list.append(speaker_name)
        add_list.append(style_name)

        table.add_row(add_list)

print(table)