import requests

username = 'swaroop'
server_url = 'http://localhost:5000'

response = requests.get(f'{server_url}/chat/{username}')

print(response.text)
