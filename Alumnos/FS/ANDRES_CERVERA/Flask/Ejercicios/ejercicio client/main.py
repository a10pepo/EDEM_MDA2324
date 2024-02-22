import requests

ret=requests.get("https://pokeapi.co/api/v2/pokemon/1")
print(ret)
print(ret.json())
