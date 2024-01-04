class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

# Lista para almacenar los alumnos
lista_alumnos = []

def agregar_alumno():
    nif = input("Ingrese el NIF del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    apellidos = input("Ingrese los apellidos del alumno: ")
    telefono = input("Ingrese el teléfono del alumno: ")
    email = input("Ingrese el email del alumno: ")
    
    nuevo_alumno = Alumno(nif, nombre, apellidos, telefono, email)
    lista_alumnos.append(nuevo_alumno)
    print("Alumno agregado correctamente.")

def eliminar_alumno_por_nif():
    nif = input("Ingrese el NIF del alumno que desea eliminar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            lista_alumnos.remove(alumno)
            print("Alumno eliminado correctamente.")
            return
    print("No se encontró ningún alumno con ese NIF.")

def actualizar_datos_por_nif():
    nif = input("Ingrese el NIF del alumno cuyos datos desea actualizar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            alumno.nombre = input(f"Nuevo nombre para {alumno.nombre}: ")
            alumno.apellidos = input(f"Nuevos apellidos para {alumno.apellidos}: ")
            alumno.telefono = input(f"Nuevo teléfono para {alumno.telefono}: ")
            alumno.email = input(f"Nuevo email para {alumno.email}: ")
            print("Datos actualizados correctamente.")
            return
    print("No se encontró ningún alumno con ese NIF.")

def mostrar_datos_por_nif():
    nif = input("Ingrese el NIF del alumno cuyos datos desea mostrar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            print(f"Datos del alumno con NIF {nif}:")
            print(f"Nombre: {alumno.nombre}")
            print(f"Apellidos: {alumno.apellidos}")
            print(f"Teléfono: {alumno.telefono}")
            print(f"Email: {alumno.email}")
            print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
            return
    print("No se encontró ningún alumno con ese NIF.")

def mostrar_datos_por_email():
    email = input("Ingrese el email del alumno cuyos datos desea mostrar: ")
    for alumno in lista_alumnos:
        if alumno.email == email:
            print(f"Datos del alumno con email {email}:")
            print(f"NIF: {alumno.nif}")
            print(f"Nombre: {alumno.nombre}")
            print(f"Apellidos: {alumno.apellidos}")
            print(f"Teléfono: {alumno.telefono}")
            print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
            return
    print("No se encontró ningún alumno con ese email.")

def listar_todos_los_alumnos():
    if lista_alumnos:
        print("Lista de todos los alumnos:")
        for alumno in lista_alumnos:
            print(f"NIF: {alumno.nif} - Nombre: {alumno.nombre} {alumno.apellidos}")
    else:
        print("No hay alumnos registrados.")

def aprobar_alumno_por_nif():
    nif = input("Ingrese el NIF del alumno que desea aprobar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            alumno.aprobado = True
            print("Alumno aprobado correctamente.")
            return
    print("No se encontró ningún alumno con ese NIF.")

def suspender_alumno_por_nif():
    nif = input("Ingrese el NIF del alumno que desea suspender: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            alumno.aprobado = False
            print("Alumno suspendido correctamente.")
            return
    print("No se encontró ningún alumno con ese NIF.")

def mostrar_alumnos_aprobados():
    alumnos_aprobados = [alumno for alumno in lista_alumnos if alumno.aprobado]
    if alumnos_aprobados:
        print("Lista de alumnos aprobados:")
        for alumno in alumnos_aprobados:
            print(f"NIF: {alumno.nif} - Nombre: {alumno.nombre} {alumno.apellidos}")
    else:
        print("No hay alumnos aprobados.")

def mostrar_alumnos_suspendidos():
    alumnos_suspendidos = [alumno for alumno in lista_alumnos if not alumno.aprobado]
    if alumnos_suspendidos:
        print("Lista de alumnos suspendidos:")
        for alumno in alumnos_suspendidos:
            print(f"NIF: {alumno.nif} - Nombre: {alumno.nombre} {alumno.apellidos}")
    else:
        print("No hay alumnos suspendidos.")

# Menú principal
while True:
    print("\nMenú Principal:")
    print("(1) Añadir un alumno")
    print("(2) Eliminar alumno por NIF")
    print("(3) Actualizar datos de un alumno por NIF")
    print("(4) Mostrar datos de un alumno por NIF")
    print("(5) Mostrar datos de un alumno por Email")
    print("(6) Listar TODOS los alumnos")
    print("(7) Aprobar Alumno por NIF")
    print("(8) Suspender Alumno por NIF")
    print("(9) Mostrar alumnos aprobados")
    print("(10) Mostrar alumnos suspendidos")
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
        mostrar_alumnos_suspendidos()
    elif opcion.upper() == "X":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
