import requests

data = {"key": "my_key", "value": "new_value"}

response = requests.put('http://localhost:8080/keyvalue', json=data)

print(response.json())
