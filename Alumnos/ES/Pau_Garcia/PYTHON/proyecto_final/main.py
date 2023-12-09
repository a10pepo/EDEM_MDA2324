from functions import *

lista_clase = []

while True:
    choice = input('''Escoja una opción:
          (1) Añadir un alumno 
          (2) Eliminar alumno por NIF
          (3) Actualizar datos de un alumno por NIF
          (4) Mostrar datos de un alumno por NIF
          (5) Mostrar datos de un alumno por Email
          (6) Listar TODOS los alumnos
          (7) Aprobar Alumno por NIF
          (8) Suspender Alumno por NIF
          (9) Mostrar alumnos aprobados
          (10) Mostrar alumnos suspensos
          (X) Finalizar Programa 
          ''')
    if (choice=='1'):
        addStudent(lista_clase)
    elif(choice=='2'):
        rmStudent(lista_clase)
    elif(choice=='3'):
        updateStudent(lista_clase)
    elif(choice=='4'):
        showStudent(lista_clase)
    elif(choice=='5'):
        showEmail(lista_clase)
    elif(choice=='6'):
        listStudents(lista_clase)
    elif(choice=='7'):
        passStudent(lista_clase)
    elif(choice=='8'):
        failStudent(lista_clase)
    elif(choice=='9'):
        showPass(lista_clase)
    elif(choice=='10'):
        showFail(lista_clase)
    elif(choice.lower()=='x'):
        break
    else:
        print('Opción seleccionada no es válida. Elija de nuevo.')