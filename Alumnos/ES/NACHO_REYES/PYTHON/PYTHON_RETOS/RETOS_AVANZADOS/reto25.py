# RETO 25

comunidades = ["Madrid", "Aragón",
                    "Valencia", "Cataluña",
                    "Extremadura", "Castilla y León",
                    "Castilla La Mancha", "Asturias",
                    "Murcia", "Cantabria", "País Vasco",
                    "Andalucia"]

def ordenar_por_long(lst):
    lst = sorted(lst, key=len, reverse = True)
    print(lst)

ordenar_por_long(comunidades)