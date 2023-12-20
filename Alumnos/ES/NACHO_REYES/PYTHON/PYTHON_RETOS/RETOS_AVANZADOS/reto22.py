# RETO 22

listaTuplas = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
miDiccionario = {}

for i in listaTuplas:
    if i[0] not in miDiccionario:
        miDiccionario[i[0]] = [i[1]]
    else:
        miDiccionario[i[0]].append(i[1])

miDiccionario