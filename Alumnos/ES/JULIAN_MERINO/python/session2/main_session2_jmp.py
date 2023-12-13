#Session 2 exercises - EDEM MDA ES Julián Merino Pérez
#1. Pedir por consola una cantidad (numérica) de Inversión
invest = int(input(str("Welcome to the investment calculator. How much do you want to invest?: ")))
#2. Pedir el % de interés anual
aipy = float(input(str("What is the annual interest rate (%)?: "))) / 100
#3. Pedir el número de años que se va a mantener la inversión
years = int(input(str("How many years do you want to invest?: ")))
#4. Finalmente, calcular la cantidad generada en los años especificados por el usuario
generated = invest * years * aipy
total = generated + invest
#Print the output:
print(f'In {years} years, you will generate {generated}€, with a total of {total}€')