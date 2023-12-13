import sys
def pysum(a,b):
    result = (f'El resultado de sumar {a} y {b} es {a + b}')
    return result

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print(pysum(num1,num2))
