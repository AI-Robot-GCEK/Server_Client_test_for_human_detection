import requests

x = requests.get("http://localhost:5000/human").json()
print(x)
