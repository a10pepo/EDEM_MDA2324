import csv



palabras = []

with open('palabras.csv') as csvfile:
    words = csv.reader(csvfile, delimiter=',')
    for row in words:
        for word in row:
            palabras.append(word.lower())

print(word)
print(palabras)
