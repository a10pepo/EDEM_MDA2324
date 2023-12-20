def get_prime(last_number):

    primes = [1,3]

    for num in range(5,last_number+1):
        
        for primo in primes[1:]:
            if (num%2)==0:
                break
            elif (num % primo/2)==0:
                break
            elif (num % primo/2)!=0:
                if (primo == primes[-1]):
                    primes.append(num)
    
    return primes


def returnPrime(first_number,last_number):

    returnList = []
    primes = get_prime(last_number)
    
    for prime in primes:
        if (prime>=first_number):
            returnList.append(prime)
    
    return returnList


def isPrime(last_number):

    returnList = []

    primes = get_prime(last_number)

    if last_number in primes:
        return (f'El número {last_number} es primo')
    else:
        return (f'El número {last_number} no es primo')


def es_bisiesto(year):
    if (year % 100 == 0):
        if (year % 400 == 0):
            return True

    elif (year % 4 == 0):
        return True
    
    else: 
        return False




print(returnPrime(100,199))
print(isPrime(199))
print(es_bisiesto(1993))