import base64
import requests

def post_file():
    url = "http://0.0.0.0:8887"
    file_name = '/audio_file/to_client/vv_voice.wav'

    with open(file_name, 'rb') as f:
        data = f.read()

    data_bytes = base64.b64encode(data)
    files = {'file':data_bytes}

    requests.post(url, data=files)

if __name__=='__main__':
    post_file()