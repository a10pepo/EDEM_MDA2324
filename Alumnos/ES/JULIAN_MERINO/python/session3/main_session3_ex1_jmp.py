#Session 3 exercise 1 - EDEM MDA ES Julián Merino Pérez
#1. A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

def invcalc():
  #1.Pedir por consola una cantidad (numérica) de Inversión
  invest = int(input(str('Welcome to the investment calculator. How much do you want to invest?: ')))
  #2. Pedir el % de interés anual
  aipy = float(input(str('What is the annual interest rate (%)?: '))) / 100
  #3. Pedir el número de años que se va a mantener la inversión
  years = int(input(str('How many years do you want to invest?: ')))
  #4. Finalmente, calcular la cantidad generada en los años especificados por el usuario
  generated = invest * years * aipy
  total = generated + invest
  #Print the output:
  print(f'In {years} years, you will generate {generated:.2f}€, with a total of {total:.2f}€')

#Let's do awhile, so it executes at least once:
calc = True
while calc == True:
  
  usr_input = input('Hello. Welcome to the investment calculator. Pick an option: \n [1] Calculate investment \n [X] Exit \n')
  if usr_input == '1':
    invcalc()
    calc = False
  elif usr_input.lower() == 'x':
    print('Bye!')
    calc = False
  else:
    print('Invalid option. Try again.')