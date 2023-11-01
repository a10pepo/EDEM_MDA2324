import time 

listaPalabras= ['remedio', 'pronunciar', 'manejar', 'ley','elefante']

abecedario = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z','ñ']

intento = 0
coicide = 0
inicio = time.time() 

def contar_letras_unicas(palabra):
    return len(set(palabra))

for palabra in listaPalabras:
   for letra in abecedario:
     unicas = contar_letras_unicas(palabra)
     if (unicas!=coicide):
        if (letra in palabra):
           intento = intento + 1 
           coicide = coicide + 1
        else:
           intento = intento + 1
    

fin = time.time() 
tiempo_transcurrido = fin - inicio

print (tiempo_transcurrido)
print(intento)

