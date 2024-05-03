import requests

data = {"key": "my_key", "value": "my_value"}

response = requests.post('http://localhost:8080/keyvalue', json=data)

try:
    json_response = response.json()
    print(json_response)
except ValueError:
    print("Failed to decode JSON response")
    print("Response content:", response.content)
