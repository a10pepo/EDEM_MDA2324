import time

def main():
    # Obtenemos el tiempo actual
    tiempoInicial = time.time()
        
    # Muestra un mensaje
    print("Iniciando...")

    # Array de palabras
    words = ["REMEDIO", "PRONUNCIAR", "MANEJAR", "LEY", "ELEFANTE"]
    alphabet = alphabetList()
    
    intentos = 0
    
    # recorrer las palabras
    for word in words:
        # Iniciamos el contador de coincidencias
        cont = 0
        intentoPalabra = 0
        # Recorremos el alfabeto
        for letter in alphabet:
            # Sumas las coincidencias
            cont += word.count(letter)
            intentos +=1
            intentoPalabra +=1
            
            if cont == len(word): 
                print(word, intentoPalabra)
                break
    
    
    tiempoFinal = time.time()
      
     
            
    # Imprime el contador
    print(f"Numero de intentos: {intentos}")
    print(f"Tiempo de ejecucion: {tiempoFinal - tiempoInicial}")
       

    
def alphabetList():
    alfabeto = ['A', 'E', 'O', 'I', 'N', 'R', 'L', 'S', 'U', 'T', 'C', 'D', 'P', 'M', 'Y', 'Q', 'B', 'G', 'V', 'H', 'F', 'J', 'Z', 'X', 'K', 'Ñ', 'W']
    return alfabeto
    
# Iniciar
main()

