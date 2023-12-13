"""
1. Enunciado Proyecto FInal

Una empresa de formación quiere gestionar su cartera de alumnos.

Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

NIF (string)
Nombre (string)
Apellidos (string)
Teléfono (string)
Email (string)
Aprobado (boolean)
El programa debe mostrar las siguientes opciones por consola para que escoja el usuario:

(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS os alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X
"""

from students import Student

#Let's define the different options of the program:
def add_student():
    nif = input(f"Enter the student's NIF: ")
    name = input(f"Enter the student's name: ")
    surname = input(f"Enter the student's surname: ")
    phone = input(f"Enter the student's phone number: ")
    email = input(f"Enter the student's email: ")
    passed = eval(input(f"Enter whether the new student has passed the course (True) or not (False): "))
    new_student = Student(nif, name, surname, phone, email, passed)
    print('New student added.')
    return new_student

def del_student(nif: str, list):
    for i in range(len(list)):
        if list[i].nif == nif:
            print(f'Student {list[i].name} {list[i].surname} with NIF: {list[i].nif} removed.')
            del list[i]
        else:
            print(f'Student {nif} not found.')

def update_student(nif: str, list, a: bool, b: bool):
    if a:
        for i in range(len(list)):
            if list[i].nif == nif:
                nif = input(f"Enter the student's NIF: ")
                list[i].name = input(f"Enter the student's name: ")
                list[i].surname = input(f"Enter the student's surname: ")
                list[i].phone = input(f"Enter the student's phone number: ")
                list[i].email = input(f"Enter the student's email: ")
                list[i].passed = eval(input(f"Enter whether the new student has passed the course (True) or not (False): "))
            else:
                print(f'Student {nif} not found.')
    elif not a and b:
        for i in range(len(list)):
            if list[i].nif == nif:
                list[i].passed = True
                print(f'Student {list[i].name} PASSED the course.')
                break
            else:
                print(f'Student {nif} not found.')
    elif not a and not b:
        for i in range(len(list)):
            if list[i].nif == nif:
                list[i].passed = False
                print(f'Student {list[i].name} FAILED the course.')
            else:
                print(f'Student {nif} not found.')

def search_student(nif: str, list):
    found = False
    for i in range(len(list)):
        if list[i].nif == nif:
            print(f'''
NIF: {list[i].nif} 
Name: {list[i].name} 
Surname: {list[i].surname} 
Phone: {list[i].phone}
e-mail: {list[i].email}
Passed: {list[i].passed}
            ''')
            found = True       
    if found == False:
        print("No matches found.")

def search_student_email(email: str, list):
    found = False
    for i in range(len(list)):
        if list[i].email == email:
            print(f'''
NIF: {list[i].nif} 
Name: {list[i].name} 
Surname: {list[i].surname} 
Phone: {list[i].phone}
e-mail: {list[i].email}
Passed: {list[i].passed}
            ''')
            found = True       
    if found == False:
        print("No matches found.")

def list_all(list, a: bool, b: bool):
    if a and b:
        for i in range(len(list)):
            print(f'''
NIF: {list[i].nif} 
Name: {list[i].name} 
Surname: {list[i].surname} 
Phone: {list[i].phone}
e-mail: {list[i].email}
Passed: {list[i].passed}
                ''')
    elif not a and b:
        for i in range(len(list)):
            if list[i].passed == True:
                print(f'''
NIF: {list[i].nif} 
Name: {list[i].name} 
Surname: {list[i].surname} 
Phone: {list[i].phone}
e-mail: {list[i].email}
Passed: {list[i].passed}
                ''')
    elif not a and not b:
        for i in range(len(list)):
            if list[i].passed == False:
                print(f'''
NIF: {list[i].nif} 
Name: {list[i].name} 
Surname: {list[i].surname} 
Phone: {list[i].phone}
e-mail: {list[i].email}
Passed: {list[i].passed}
                ''')

students_book = []

def students_database(list):
    choice = str
    while choice != 'x':
        print('''
          Welcome to Students Management Program. Pick a choice:
          1. Add a student
          2. Remove a student by NIF
          3. Update a student's record by NIF
          4. Search a student by NIF
          5. Search a student by email
          6. List ALL students
          7. Pass a student by NIF
          8. Fail a student by NIF
          9. Show PASSED students ONLY
         10. Show FAILED students ONLY
          X. Quit
          ''')
        choice = input('Option: ')
        if choice == '1':
            list.append(add_student())
        elif choice == '2':
            nif = input("Enter the student's NIF: ")
            del_student(nif, list)
        elif choice == '3':
            nif = input("Enter the student's NIF: ")
            update_student(nif, list, a = True, b = True)
        elif choice == '4':
            nif = input("Enter the student's NIF: ")
            search_student(nif, list)
        elif choice == '5':
            email = input("Enter the student's email: ")
            search_student_email(email, list)
        elif choice == '6':
            list_all(list, a = True, b = True)
        elif choice == '7':
            nif = input("Enter the student's NIF: ")
            update_student(nif, list, a = False, b = True)
        elif choice == '8':
            nif = input("Enter the student's NIF: ")
            update_student(nif, list, a = False, b = False)
        elif choice == '9':
            list_all(list, a = False, b = True)
        elif choice == '10':
            list_all(list, a = False, b = False)
        elif choice.lower() == 'x':
            print('Goodbye.')
            break
        else:
            print('Wrong option. Retry.')
    return list

students_database(students_book)
