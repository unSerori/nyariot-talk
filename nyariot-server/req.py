import requests

url = 'https://httpbin.org/get'

r = requests.get("https://localhost")

print(r.text)