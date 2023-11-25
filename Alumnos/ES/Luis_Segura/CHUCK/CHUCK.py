import os
import requests
import time

def fetch_chuck_norris_joke():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()['value']
    else:
        return None

def save_jokes_to_file(jokes, file_name="chisteschuck.txt"):
    # Obtiene el directorio del chuck.py!!!
    script_directory = os.path.dirname(os.path.realpath(__file__))
    
    # Crea la ruta completa al archivo dentro del directorio actual!!!!
    file_path = os.path.join(script_directory, file_name)

    with open(file_path, "a", encoding="utf-8") as file:
        for joke in jokes:
            file.write(joke + "\n")

def main():
    num_jokes_to_fetch = 5
    interval_seconds = 100

    while True:
        jokes = []
        for _ in range(num_jokes_to_fetch):
            joke = fetch_chuck_norris_joke()
            if joke:
                jokes.append(joke)
                print(f"{joke}")

        save_jokes_to_file(jokes)

        # Esperar el intervalo de tiempo especificado antes de obtener más bromas
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
