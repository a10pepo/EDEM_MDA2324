""" Reto 3
El nuevo gobierno ha decidido replantear el sistema de pago de impuestos. Ha pensado que a partir de ahora:

si una persona es mayor de 16 años y menor de 70 ésta debe pagar impuestos.
En caso de no tener ingresos iguales o superiores a 800€ se acumulará una deuda mensual del 10%.
Si supera los 800€, pero no llega a los 2000€, deberá pagar un impuesto del 30% mensual
Si supera los 2000€ esta persona deberá pagar el 50% en concepto de impuestos
si la persona es menor de 16 años, no tiene que pagar impuestos
Escribe un programa capaz de calcular la cantidad de impuestos, o endeudamiento, de una lista de
personas durante 
un año entero (12 meses). """

josan=["Josan",38,2000]

def calculoImpuesto(persona):
    impuestosmensualesapagar=0
    impuestosAnualesapagar=impuestosmensualesapagar*12
    deudaMensual=0
    deudaAnual=deudaMensual*12
    if 16<persona[1]<70:
        impuestosmensualesapagar=0
    else:
        if persona[2]<=800:
            deudaMensual=persona[2]*0.1
        elif 800<persona[2]<=2000:
            impuestosmensualesapagar=persona[2]*0.3
        else:
            impuestosmensualesapagar=persona[2]*0.5
    return deudaAnual, impuestosAnualesapagar

print(calculoImpuesto(josan))