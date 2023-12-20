cantidad_inversion = float(input("Por favor, indícame la cantidad de inversión que deseas ingresar:\n"))
interes_anual = float(input("Cuál es el interés anual que deseas recibir:\n"))
tiempo = int(input("A cuántos años deseas ingresar la inversión:\n"))

calculo_interes= (cantidad_inversion*interes_anual)/100
calculo_final= float(calculo_interes*tiempo)

print(f'La cantidad generada en {tiempo} años será de: {calculo_final}')