#paso1
inversión = float(input("¿Cuanto quieres invertir?"))
print(f"Quieres invertir{inversión}€")

#paso2
print("¿Cuál es el interes?")
interes = float(input())
print(f"El interes es {interes}%")

#paso3
print("¿En cuantos años?")
numero_años = int(input())
print(f"En {numero_años} años")


#paso4
cantidad_generada = inversión * (1 + (interes / 100)) ** numero_años
print(f"La cantidad generada en {numero_años} años será: {cantidad_generada:.2f}")


