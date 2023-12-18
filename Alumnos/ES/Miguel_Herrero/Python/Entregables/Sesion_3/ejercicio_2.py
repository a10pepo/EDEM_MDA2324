def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos_hasta_100():
    print("Estos son los números primos que hay del 1 al 100:")
    for num in range(1, 101):
        if es_primo(num):
            print(num, end=" ")

if __name__ == "__main__":
    numeros_primos_hasta_100()
