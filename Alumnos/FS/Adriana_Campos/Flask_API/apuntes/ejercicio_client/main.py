import requests


# obtenemos por el terminal lo que hay en la API
#el get es para trearte lo que esta en la api

ret=requests.get("https://pokeapi.co/api/v2/pokemon/1")
print(ret)
print(ret.json())
