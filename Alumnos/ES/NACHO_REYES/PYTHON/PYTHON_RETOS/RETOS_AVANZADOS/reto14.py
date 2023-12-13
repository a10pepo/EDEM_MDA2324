#RETO 14

miCodigo = 'print("Hola Mundo")'
otroCodigo = """
def multiplicar(x,y):
    return x*y

print('Multiplica: 2 * 4: ',multiplicar(2,4))
"""
print(exec(miCodigo))
exec((otroCodigo))