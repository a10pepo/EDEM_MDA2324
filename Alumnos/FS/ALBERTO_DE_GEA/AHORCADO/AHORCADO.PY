#PASO 1
letras = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#PASO 2
with open("palabras.txt", "r") as archivo:
    palabras = archivo.read().splitlines()

#PASO 3
#for palabra in palabras:
    #letras = len(palabra)
    #print(f'La palabra {palabra} contiene {letras} letras')

#PASO 4
letras = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
palabras = ["REMEDIO", "PRONUNCIAR", "MANEJAR", "LEY", "ELEFANTE"]
total_recorridos = 0
total_no_recorridos = 0

for palabra in palabras:
    for letra in letras:
        contador = palabra.count(letra)
        if contador > 0:
            total_recorridos += 1
        else:
            total_no_recorridos += 1
            print(f'La letra "{letra}" aparece {contador} veces en la palabra "{palabra}"')

print(f'Número total de veces que se recorren las letras: {total_recorridos}')
print(f'Número total de veces que se recorren las letras: {total_no_recorridos}')
