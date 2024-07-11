import requests

URL = "http://127.0.0.1:8000/data/"

req = requests.get(url=URL)

datas = req.json()
print(datas)