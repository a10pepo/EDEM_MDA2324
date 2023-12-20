#Crea una aplicación de consola que calcule los resultados de una inversión. Debe
#Pedir por consola una cantidad (numérica) de Inversión
#Pedir el % de interés anual
#Pedir el número de años que se va a mantener la inversión
#Finalmente, calcular la cantidad generada en los años especificados por el usuario

def inversion(cant,inter,anos):
    total = cant*(1+inter/100)**anos
    print(f'la inversión total de {cant} dutante {anos} años al {inter} de interes es igual a {total}')
    

cant = int(input('Qué cantidad deseas invertir?: '))
inter = float(input('Dime el interés anual: '))
anos = int(input('Cuantos años: '))
inversion(cant,inter,anos)