print("Hola Mundo")
import requests


url= 'https://api.chucknorris.io/jokes/random'

#a=1
while True:
    response = requests.get(url)

    if response.status_code == 200:
    
        data = response.json()
        print(data['value'])
        broma_str = str(data['value'])
    
        with open('results.txt', 'a') as archivo:
        
                archivo.write(broma_str+"\n")
        #a+=1

    else:
        print('Error en la solicitud. Código del estado:', response.status_code)
       #a=30





