import requests

url='https://randomuser.me/api'
response = requests.get(url)
data = response.json()
user_info = data['results'][0]['name']
first_name = user_info['first']
last_name = user_info['last']
print(f"Nombre y apellidos: {first_name} {last_name}")