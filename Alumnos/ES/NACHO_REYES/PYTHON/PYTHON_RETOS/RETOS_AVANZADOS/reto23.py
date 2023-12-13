# RETO 23

from collections import Counter

misPeliculas = {'PeliculaA':81, 'PeliculaB':83, 'PeliculaC':87}
moda, freq = Counter(misPeliculas).most_common(1)[0]
print(f'La moda es: {moda} con una frequencia de {freq}')