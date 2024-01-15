"""
Una empresa de formación quiere gestionar su cartera de alumnos.

Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

NIF (string)
Nombre (string)
Apellidos (string)
Teléfono (string)
Email (string)
Aprobado (boolean)

"""
"""""

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

# Definición de la clase Estudiante
class Estudiante:
    def __init__(self, dni, nombre, curso, email, nota_final):
        self.dni = dni
        self.nombre = nombre
        self.curso = curso
        self.email = email
        self.nota_final = nota_final

# Lista para almacenar objetos de estudiantes
estudiantes = []

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    dni = input("DNI del estudiante: ")
    nombre = input("Nombre completo del estudiante: ")
    curso = input("Curso actual del estudiante: ")
    email = input("Email del estudiante: ")
    nota_final = float(input("Nota final del estudiante (0-10): "))
    nuevo_estudiante = Estudiante(dni, nombre, curso, email, nota_final)
    estudiantes.append(nuevo_estudiante)
    print("Estudiante añadido correctamente.\n")

# Función para mostrar todos los estudiantes
def mostrar_todos_los_estudiantes():
    print("Listado de estudiantes:")
    for est in estudiantes:
        estado = "Aprobado" if est.nota_final >= 5 else "Suspenso"
        print(f"{est.nombre} - DNI: {est.dni} - Curso: {est.curso} - Email: {est.email} - Estado: {estado}")
    print()  # Añade una línea vacía para separar la salida

# Inicio del programa
opcion = ''
while opcion != 'salir':
    print("\n¿Qué te gustaría hacer a continuación?")
    print("1: Añadir un nuevo estudiante")
    print("2: Mostrar todos los estudiantes")
    print("escribir 'salir' para finalizar el programa")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        agregar_estudiante()
    elif opcion == '2':
        mostrar_todos_los_estudiantes()
    elif opcion == 'salir':
        print("Saliendo del programa...")
    else:
        print("Opción no reconocida, intenta de nuevo.")


