# RETO 9

num = int(input('Introduzca el número que quiere convertir a binario: '))
res = []

while num > 0:
    residuo = num % 2
    res.append(residuo)
    num = num // 2

res.reverse()

print("El número en binario es:", end=" ")
for i in res:
    print(i, end="")
