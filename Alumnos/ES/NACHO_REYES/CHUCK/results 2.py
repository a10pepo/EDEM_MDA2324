import requests

print('hola mundo')

all_data = []

for i in range(100):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        data = response.json()['value']
        print(data)
        all_data.append(data)

all_text = " ".join(all_data)

words = all_text.split()
word_count = {}

for word in words:
    word = word.strip(".,!?")
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

file_path = '/Users/nacho/Documents/GitHub/EDEM_MDA2324/Alumnos/ES/NACHO_REYES/CHUCK/results/results.txt'
with open(file_path, 'w') as file:
    for word, count in word_count.items():
        file.write(f'Palabra: {word}, Conteo: {count}\n')
