# RETO 3

def impuestos():
    edad = int(input('Introduce la edad: '))
    sueldo: int = 0
    deuda: int = 0
    impuestos: int = 0
    
    if(edad < 16 or edad > 70):
        print('No tienes que pagar impuestos.')
    else:
        sueldo = int(input('Inroduce el salario al mes: '))
        if(sueldo <= 800):
            deuda = sueldo * 0.10
            print(f"Con una edad de {edad} y unos ingresos de {sueldo} al mes, tendrás una deuda con el Estado de{deuda * 12}€ este año")
        elif(sueldo > 800 and sueldo < 2000):
            impuestos = sueldo * 0.30
            print(f"Con la edad de {edad} y unos ingresos de {sueldo} al mes, tienes que pagar {impuestos * 12}€ en impuestos este año")
        else:
            impuestos = sueldo * 0.50
            print(f"Con la edad de {edad} y unos ingresos de {sueldo} al mes, tienes que pagar {impuestos * 12}€ en impuestos este año")

impuestos()