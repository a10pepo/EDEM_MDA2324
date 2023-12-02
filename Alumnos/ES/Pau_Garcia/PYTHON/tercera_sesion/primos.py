# Voy a crear una función para obtener los primos en un rango. 
# Según la teoría de números, para comprobar si un número es primo
# basta con comprobar que no es divisible por ningún primo menor entre 2
# sin tener en cuenta el 1, claro.

# La función primero crea una lista de primos con el 1 y el 3 ya incluidos,
# ya que quedan excluidos del algoritmo;
# luego anida dos bucles que iteran primero sobre el rango de números desdeado,
# y luego sobre la lista de primos. Si el número es par, queda excluido de la lista.
# Si no lo es se comprueba que no es divisible entre ningún primo menor entre dos, 
# y si lo es, num queda excluido también de la lista. 
# De lo contrario, se añade a la lista de primos que devuelve la función. 

def get_prime(last_number):

    primes = [1,3]

    for num in range(5,last_number):
        
        for primo in primes[1:]:
            if (num%2)==0:
                break
            elif (num % primo/2)==0:
                break
            elif (num % primo/2)!=0:
                if (primo == primes[-1]):
                    primes.append(num)
    
    return primes

num = int(input('Bienvenido, ¿hasta qué número quieres que calcule primos? '))
# Mejor no intentarlo con más de 100k
result = get_prime(num)
print(f'Los números primos entre el 1 y el {num} son los siguientes: {result}')


                
            
        
