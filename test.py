import requests as r

url = "http://127.0.0.1:8000/api/v1/grid_positions/"
positions = [
    {"grid_id": 12, "x": 9271764.19761, "y": 97465.01726, "z": 87651.12351},
    {"grid_id": 975, "x": 12341.19761, "y": 6541.3, "z": 62134.12351},
    {"grid_id": 4435, "x": 5344123.19761, "y": 915.01726, "z": 887151.12351},
    {"grid_id": 367, "x": 164.19761, "y": 5.01726, "z": 775.12351}
]

response = r.post(url, json=positions)
print(response.json())


url = "http://127.0.0.1:8000/api/v1/grid_positions/latest/"
response = r.get(url)
print(response.json())

response

data = [
    {"uuid":"129448123554376162_144115188075855895_Sudentor MK1.7.3 Dawson CS","entity_id":129448123554376162,"grid_name":"Sudentor MK1.7.3 Dawson CS","owner_id":144115188075855895,"faction_tag":"PBC"},
    {"uuid":"96113300194743417_144115188075855895_Large Grid 5409","entity_id":96113300194743417,"grid_name":"Large Grid 5409","owner_id":144115188075855895,"faction_tag":"PBC"}
    ]

url = "http://127.0.0.1:8000/api/v1/grids/"
response = r.post(url, json=data)
print(response.json())

data = [
{"type": "poi", "gps": "GPS:Ariel:-4110989.31:3110909.45:-359192.17:#FF40EC34:", "radius": 10000},
{"type": "poi", "gps": "GPS:Beratnas Gas Station Jupiter:-119500.8:-2955103.11:351258.18:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Beratnas Gas Station Saturn:2290226.37:1817047.82:-195774.09:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Beratnas Gas Station Uranus:-4106322.64:3003556.83:-69235.74:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Bush Naval Shipyards:-860377.39:251612.55:58803.99:#FF75C9F1:Nation HQs:"},
{"type": "dx", "gps": "GPS:C1 - (R300km):600000:1600000:0:#FFFFFF00:DX7:"},
{"type": "dx", "gps": "GPS:C2 - (R300km):-600000:1600000:0:#FFFFFF00:DX7:"},
{"type": "dx", "gps": "GPS:Ceres - (R400km):0:2350000:100000:#FFFFFF00:DX7:"},
{"type": "poi", "gps": "GPS:Ceres Station:-9793.86:2325984.53:84772.28:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Ceres:0:2350000:100000:#FFD6931E:", "radius": 30000},
{"type": "poi", "gps": "GPS:Corley Station:3001481.29:1908187.5:-105165.49:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Deimos:900000:-800000:0:#FF40EC34:", "radius": 4500},
{"type": "dx", "gps": "GPS:E1 - (R:300km):-1725000:0:0:#FFFFFF00:DX4:"},
{"type": "dx", "gps": "GPS:E2 - (R300km):-1500000:-900000:0:#FFFFFF00:DX4:"},
{"type": "dx", "gps": "GPS:Earth - (R400km):-800000:100000:80000:#FFFFFF00:DX4:"},
{"type": "poi", "gps": "GPS:Earth:-800000:100000:80000:#FF40EC34:", "radius": 100000},
{"type": "poi", "gps": "GPS:Europa KOTH:404015.47:-3195511.14:108837.6:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Europa:400000:-3200000:100000:#FF40EC34:", "radius": 10500},
{"type": "poi", "gps": "GPS:Ganymede Botanical:-404041.3:-3093957.08:-285675.6:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Ganymede:-400000:-3100000:-300000:#FF40EC34:", "radius": 17500},
{"type": "dx", "gps": "GPS:Greek Cluster - (R400km):-1600000:-2700000:-334490:#FFFFFF00:DX2:"},
{"type": "poi", "gps": "GPS:Greek Cluster Waystation:-1380846.75:-2582155.58:-302303.08:#FFD6931E:"},
{"type": "dx", "gps": "GPS:Inner High Speed Zone - (R2750km):0:-1725000:100000:#FFFFFF00:DX5:"},
{"type": "poi", "gps": "GPS:Io:200000:-2900000:-100000:#FF40EC34:", "radius": 11000},
{"type": "dx", "gps": "GPS:Jupiter - (R750km):0:-3200000:0:#FFFFFF00:DX6:"},
{"type": "poi", "gps": "GPS:Jupiter:0:-3200000:0:#FF40EC34:", "radius": 140000},
{"type": "poi", "gps": "GPS:Kirino Orbital Shipyards:827693.09:-813745.92:-77878.79:#FFF1C875:Nation HQs:"},
{"type": "poi", "gps": "GPS:Luna:-650000:225000:0:#FF40EC34:", "radius": 14000},
{"type": "dx", "gps": "GPS:M1 - (R300km):800000:-1550000:0:#FFFFFF00:DX3:"},
{"type": "dx", "gps": "GPS:M2 - (R300km):1550000:-800000:0:#FFFFFF00:DX3:"},
{"type": "dx", "gps": "GPS:Mars - (R400km):750000:-750000:-80000:#FFFFFF00:DX3:"},
{"type": "poi", "gps": "GPS:Mars:750000:-750000:-80000:#FF40EC34:", "radius": 60000},
{"type": "poi", "gps": "GPS:MCRN Free Rebel Fleet:3200000:2250000:35000:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Miller Mobile Construction Barge:-9605.07:2310850.71:122318.61:#FFF17575:Nation HQs:"},
{"type": "dx", "gps": "GPS:P1 - (R300km):-800000:-1550000:0:#FFFFFF00:DX2:"},
{"type": "dx", "gps": "GPS:Pallas - (R300km):0:-1725000:100000:#FFFFFF00:DX2:"},
{"type": "poi", "gps": "GPS:Pallas:0:-1725000:100000:#FFFFFF00:", "radius": 14000},
{"type": "poi", "gps": "GPS:Pallas Station:-3296:-1727232:76613:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Phobos:650000:-650000:-250000:#FF40EC34:", "radius": 4400},
{"type": "poi", "gps": "GPS:Rhea:2700000:1800000:100000:#FF40EC34:", "radius": 9000},
{"type": "dx", "gps": "GPS:Saturn - (R750km):2800000:2000000:-100000:#FFFFFF00:DX8:"},
{"type": "poi", "gps": "GPS:Saturn:2800000:2000000:-100000:#FF40EC34:", "radius": 60000},
{"type": "poi", "gps": "GPS:Scrap Yard:2750000:2435000:130000:#FFD6931E:"},
{"type": "dx", "gps": "GPS:Sol Gate - (R80km):-3900000:3600000:-200000:#FFFFFF00:DX6:"},
{"type": "poi", "gps": "GPS:Sol Gate:-3900000:3600000:-200000:#FFFFFF00:"},
{"type": "dx", "gps": "GPS:T1 - (R300km):1725000:0:0:#FFFFFF00:DX2:"},
{"type": "poi", "gps": "GPS:Titan:3000000:1900000:-100000:#FF40EC34:", "radius": 10000},
{"type": "dx", "gps": "GPS:Trojan Cluster - (R400km):1600000:-2700000:445350:#FFFFFF00:DX2:"},
{"type": "poi", "gps": "GPS:Trojan Cluster Waystation:1420788.01:-2531349.34:404487.57:#FFD6931E:"},
{"type": "dx", "gps": "GPS:Tycho - (R300km):1400000:1000000:-50000:#FFFFFF00:DX2:"},
{"type": "poi", "gps": "GPS:Tycho Hub:1400000:1000000:-50000:#FFD6931E:"},
{"type": "dx", "gps": "GPS:Uranus - (R500km):-4200000:3000000:-250000:#FFFFFF00:DX6:"},
{"type": "poi", "gps": "GPS:Uranus:-4200000:3000000:-250000:#FF40EC34:", "radius": 80000},
{"type": "dx", "gps": "GPS:Vesta - (R300km):-1400000:1000000:-50000:#FFFFFF00:DX2:"},
{"type": "poi", "gps": "GPS:Vesta Station:-1412860:986040:-49577:#FFD6931E:"},
{"type": "poi", "gps": "GPS:Vesta:-1400000:1000000:-50000:#FFD6931E:", "radius": 28000}
]

url = "http://127.0.0.1:8000/api/v1/gps/"
response = r.post(url, json=data)
print(response.json())


