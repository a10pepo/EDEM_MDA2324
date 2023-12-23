# EJERCICIOS SESIÓN 2

print(f'Hola. Bienvenido al sistema de cálculo de inversiones.')
cantidad = int(input('''¿Cuanto quieres invertir?
'''))
interes = int(input('''¿Cuál es el interés anual (en %)?
'''))
años = int(input('''¿Cuántos años vas a mantener la inversión?
'''))
resultado = años * cantidad * (interes/100)
print(f'En {años} años habrás recibido {resultado}€ de interés')