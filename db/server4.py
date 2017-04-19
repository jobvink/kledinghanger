import requests, json

response = requests.get('http://127.0.0.1:8000/products/1231425363543/').json()
print response['size']