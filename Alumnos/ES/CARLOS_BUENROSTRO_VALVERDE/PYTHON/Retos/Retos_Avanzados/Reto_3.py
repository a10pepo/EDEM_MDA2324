# # Reto 3: El nuevo gobierno ha decidido replantear el sistema de pago de impuestos. Ha pensado que a partir de ahora:
# - Si una persona es mayor de 16 años y menor de 70 ésta debe pagar impuestos.
# - En caso de no tener ingresos iguales o superiores a 800€ se acumulará una deuda mensual del 10%.
# - Si supera los 800€, pero no llega a los 2000€, deberá pagar un impuesto del 30% mensual
# - Si supera los 2000€ esta persona deberá pagar el 50% en concepto de impuestos
# - Si la persona es menor de 16 años, no tiene que pagar impuestos
# Escribe un programa capaz de calcular la cantidad de impuestos, o endeudamiento, de una lista de personas durante un año entero (12 meses).

def pago_impuestos():
    edad = int(input("Introduzca la edad del contribuyente: "))
    ingresos = 0
    deuda = 0
    impuestos = 0
    if edad < 16 or edad > 70:
        print("No es contribuyente. No pagará impuestos.")
    else:
        ingresos = int(input("Introduzca los ingresos mensuales: "))
        if ingresos < 800:
            deuda = ingresos * 0.10
            print(f'Con la edad de {edad} años y un salario de {ingresos}, la deuda con el Estado será de {round(deuda *12, 2)} euros en un año.')
        elif ingresos > 800 and ingresos < 2000:
            deuda = ingresos * 0.30
            print(f'Con la edad de {edad} años y un salario de {ingresos}, la deuda con el Estado será de {round(deuda *12, 2)} euros en un año.')
        elif ingresos < 2000:
            deuda = ingresos * 0.50
            print(f'Con la edad de {edad} años y un salario de {ingresos}, la deuda con el Estado será de {round(deuda *12, 2)} euros en un año.')

pago_impuestos()