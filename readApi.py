import requests

response = requests.get('http://localhost:8080/keyvalue/my_key')

print(response.json())
