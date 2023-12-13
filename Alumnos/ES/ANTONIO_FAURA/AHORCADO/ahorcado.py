import pandas as pd

letras = ['e', 'a', 'o', 'i', 's', 'n', 'r', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'g', 'b', 'v', 'y', 'q', 'h', 'f', 'j', 'z', 'x', 'k', 'w', 'ñ']


palabras_df = pd.read_csv("palabras.csv")

def ahorcado(palabras):
    intentos = 0
  
    for i, palabra_elegida in palabras.iterrows():
        letras_acertadas = 0
      
        for letra_elegida in letras:
            intentos += 1
          
            if letra_elegida in palabra_elegida["palabras"]:
                letras_acertadas += palabra_elegida["palabras"].count(letra_elegida)
              
                if letras_acertadas == len(palabra_elegida["palabras"]):
                    break
                  
    print(f"Me ha llevado {intentos} intentos. No te pido que me lo mejores, iguálamelo")
ahorcado(palabras_df)