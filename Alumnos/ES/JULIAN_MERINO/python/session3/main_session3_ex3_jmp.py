#Session 3 exercise 3 - EDEM MDA ES Julián Merino Pérez
#Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no.
#If a year is divisible by 4, it's a leap year
def lapyear(year):
  if year % 4 == 0:
    print(f'{year} is a leap year.')
  else:
    print(f'{year} is not a leap year.')

#We iterate a range of years from a list.
years = range(1990, 2031)
for i in years:
  lapyear(i)