import requests as r

url = "http://127.0.0.1:8000/api/v1/grid_positions/"
positions = [
    {"grid_id": 872513, "x": 9271764.19761, "y": 97465.01726, "z": 87651.12351},
    {"grid_id": 453, "x": 12341.19761, "y": 6541.3, "z": 62134.12351},
    {"grid_id": 1234, "x": 5344123.19761, "y": 915.01726, "z": 887151.12351},
    {"grid_id": 6689, "x": 164.19761, "y": 5.01726, "z": 775.12351}
]

response = r.post(url, json=positions)
print(response.json())
