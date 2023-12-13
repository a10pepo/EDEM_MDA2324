class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

# 1. Añadir un nuevo alumno a la lista

def agregar_alumno():
    print("Introduce los datos del nuevo alumno:")
    nif = input("NIF: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    alumno = Alumno(nif, nombre, apellidos, telefono, email)
    lista_alumnos.append(alumno)
    print("Alumno añadido correctamente.")


# 2. Eliminar un alumno por NIF

def eliminar_alumno_por_nif():
    nif = input("Introduce el NIF del alumno que quieres eliminar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            lista_alumnos.remove(alumno)
            print("Alumno eliminado correctamente.")
            return
    print("Alumno no encontrado.")

# 3. Actualizar datos de un alumno por NIF

def actualizar_datos_por_nif():
    nif = input("Introduce el NIF del alumno para actualizar sus datos: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            alumno.nombre = input("Nuevo nombre: ")
            alumno.apellidos = input("Nuevos apellidos: ")
            alumno.telefono = input("Nuevo teléfono: ")
            alumno.email = input("Nuevo email: ")
            print("Datos actualizados correctamente.")
            return
    print("Alumno no encontrado.")

# 4. Mostrar datos de un alumno por NIF

def mostrar_datos_por_nif():
    nif = input("Introduce el NIF del alumno para mostrar sus datos: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            print(f"NIF: {alumno.nif}")
            print(f"Nombre: {alumno.nombre}")
            print(f"Apellidos: {alumno.apellidos}")
            print(f"Teléfono: {alumno.telefono}")
            print(f"Email: {alumno.email}")
            print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
            return
    print("Alumno no encontrado.")

# 5. Mostrar datos de un alumno por Email.

def mostrar_datos_por_email():
    email = input("Introduce el email del alumno para mostrar sus datos: ")
    for alumno in lista_alumnos:
        if alumno.email == email:
            print(f"NIF: {alumno.nif}")
            print(f"Nombre: {alumno.nombre}")
            print(f"Apellidos: {alumno.apellidos}")
            print(f"Teléfono: {alumno.telefono}")
            print(f"Email: {alumno.email}")
            print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
            return
    print("Alumno no encontrado.")


# 6. listar todos los alumnos

def listar_todos_los_alumnos():
    print("Lista de todos los alumnos:")
    for alumno in lista_alumnos:
        print(f"NIF: {alumno.nif} - Nombre: {alumno.nombre} {alumno.apellidos}")

# 7. Aprobar a un alumno por NIF
def aprobar_alumno_por_nif():
    nif = input("Introduce el NIF del alumno que quieres aprobar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            alumno.aprobado = True
            print("Alumno aprobado correctamente.")
            return
    print("Alumno no encontrado.")


# 8. suspender a un alumno por NIF

def suspender_alumno_por_nif():
    nif = input("Introduce el NIF del alumno que quieres suspender: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            alumno.aprobado = False
            print("Alumno suspendido correctamente.")
            return
    print("Alumno no encontrado.")

# 9. Mostrar alumnos aprobados.

def mostrar_alumnos_aprobados():
    print("Alumnos aprobados:")
    for alumno in lista_alumnos:
        if alumno.aprobado:
            print(f"NIF: {alumno.nif} - Nombre: {alumno.nombre} {alumno.apellidos}")

# 10.Mostrar alumnos suspensos.

def mostrar_alumnos_suspensos():
    print("Alumnos suspensos:")
    for alumno in lista_alumnos:
        if not alumno.aprobado:
            print(f"NIF: {alumno.nif} - Nombre: {alumno.nombre} {alumno.apellidos}")

# Lista para almacenar los alumnos
lista_alumnos = []

while True:
    print("\n*** Gestión de Alumnos ***")
    print("(1) Añadir un alumno")
    print("(2) Eliminar alumno por NIF")
    print("(3) Actualizar datos de un alumno por NIF")
    print("(4) Mostrar datos de un alumno por NIF")
    print("(5) Mostrar datos de un alumno por Email")
    print("(6) Listar TODOS los alumnos")
    print("(7) Aprobar Alumno por NIF")
    print("(8) Suspender Alumno por NIF")
    print("(9) Mostrar alumnos aprobados")
    print("(10) Mostrar alumnos suspensos")
    print("(X) Finalizar Programa")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        eliminar_alumno_por_nif()
    elif opcion == "3":
        actualizar_datos_por_nif()
    elif opcion == "4":
        mostrar_datos_por_nif()
    elif opcion == "5":
        mostrar_datos_por_email()
    elif opcion == "6":
        listar_todos_los_alumnos()
    elif opcion == "7":
        aprobar_alumno_por_nif()
    elif opcion == "8":
        suspender_alumno_por_nif()
    elif opcion == "9":
        mostrar_alumnos_aprobados()
    elif opcion == "10":
        mostrar_alumnos_suspensos()
    elif opcion.lower() == "x":
        break
    else:
        print("Opción no válida. Introduce una opción válida.")


    