import sys

def suma(num1,num2):
    print('La suma de los números es:', num1 + num2)

if __name__ == '__main__':
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    suma(num1,num2)