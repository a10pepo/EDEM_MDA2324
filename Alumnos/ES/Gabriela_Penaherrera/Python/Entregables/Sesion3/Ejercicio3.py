lista = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

for año in lista:
    if año % 4 == 0 and año % 100 != 0:
        print(f'{año} es bisiesto')
    elif año % 400 == 0:
        print(f'{año} es bisiesto')
    else:
        print(f'{año} no es bisiesto')

