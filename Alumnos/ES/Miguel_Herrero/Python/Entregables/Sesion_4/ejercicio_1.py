def es_bisiesto(i):
    i = int(i)
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        return True
    else:
        return False

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

años = []
for i in range(6):
    a = input('Introduce un año: ')
    años.append(int(a))

for año in años:
    if es_bisiesto(año):
        print(f"\nEl año {año} es bisiesto")
    if es_primo(año):
        print(f"\nEl año {año} es primo")
    else:
        print(f"\nEl año {año} no es primo ni bisiesto")
