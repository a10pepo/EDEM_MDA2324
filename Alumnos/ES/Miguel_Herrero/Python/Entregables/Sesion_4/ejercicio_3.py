import requests

url='https://randomuser.me/api'
response = requests.get(url)
if response.status_code == 200:
        data = response.json()

user_info = data['results'][0]['name']
first_name = user_info['first']
last_name = user_info['last']

print(f"Nombre y apellido retornados por la API: {first_name} {last_name}")
