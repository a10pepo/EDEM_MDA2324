'''A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
1.a Crea una función que reciba un rango de números como parámetro y muestre por 
consola únicamente los valores primos'''

def primo (rango1,rango2):
    for elemento in range(rango1, rango2):
        es_primo = True
        for i in range(2, int(elemento**0.5) + 1):
            if elemento % i == 0:
                es_primo = False
                break  

        if es_primo == True:
            print(elemento)
primo(5,20)



'''1.b Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no'''

def primo(numero):
    is_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            is_primo = False
            break

    if is_primo:
        print(f'el {numero} es primo')
    else:
        print(f'el {numero} no es primo')
primo(15)


        
'''1.c Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.'''

def año(numero):
    es_bisiesto = True
    if numero % 4 ==0:
        es_bisiesto = True
    elif numero % 400 == 0:
        es_bisiesto = True
    elif numero % 100 !=0:
        es_bisiesto = False 
    if es_bisiesto:
        print('Es bisiesto')   
    else:
        print('No es bisiesto') 
año(2012)
        

