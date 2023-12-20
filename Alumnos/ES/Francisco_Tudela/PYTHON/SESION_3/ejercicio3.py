def bisiesto():
    lista = list(range(1500,2800))
    años_lista = []
    for año in lista:
        es_bisiesto = False
        if año % 4 == 0:
            es_bisiesto = True
        elif año % 100 == 0 and año % 400 == 0:
            es_bisiesto = True
        if es_bisiesto:
            años_lista.append(año)
    return años_lista
        
Años_bisiestos = bisiesto()
print(Años_bisiestos)
            
