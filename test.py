import requests as r

url = "http://127.0.0.1:8000/signals/"
drive_sig = {
    'faction_tag': 'WSN',
    'x': '3',
    'y': '2',
    'z': '5000'
    }

response = r.post(url, json=drive_sig)
print(response.json())
