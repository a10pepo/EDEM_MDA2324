import pandas as pd


lista_palabras = ['japonesa','aullar','cosquillas','amistad', 'matrimonio','obligatorio','trenza','aldea','peinado','principal']

letras = ['e', 'a', 'o', 's', 'r', 'n', 'l', 'd', 'i', 'c', 't', 'u', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'z', 'j', 'ñ' 'x', 'k', 'w']

intentos = 0

for palabra in lista_palabras:
    cantidad_letras = len(palabra)
    while cantidad_letras > 0:  
        for letra in letras: 
            intentos += 1 
            if letra in palabra:
                    conteo = palabra.count(letra)
                    cantidad_letras -= conteo
                    if cantidad_letras == 0:
                         break


print(f'El numero de intentos ha sido: {intentos}')
