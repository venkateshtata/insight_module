import requests

x = requests.get("http://192.168.225.50:5000/test")
print(x.text)