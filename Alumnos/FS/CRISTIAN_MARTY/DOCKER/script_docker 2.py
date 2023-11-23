import sys

try:
    primero = int(sys.argv[1])
    segundo = int(sys.argv[2])
    suma = primero + segundo
    print(f"Sum:{suma}")
    
    
    
except (IndexError, ValueError):
    print("Error!!!!")