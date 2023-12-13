#This script is part of the Docker deliverable for EDEM DA Master 2023 - Julián Merino
#This script gets 2 numbers (integers) and adds them

#Import sys so we can pass arguments to the function
import sys

#Let's define a function we can call, which returns the addition
def pysum(arg1: float, arg2: float):
    return arg1 + arg2

#Let's define a functions that checks whether the arguments are numbers (int or float):
def is_num(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

if is_num(sys.argv[1]) == True and is_num(sys.argv[2]) == True:
    print(f'Sum: {pysum(float(sys.argv[1]), float(sys.argv[2]))}')
else:
    print('All arguments must be numbers.')