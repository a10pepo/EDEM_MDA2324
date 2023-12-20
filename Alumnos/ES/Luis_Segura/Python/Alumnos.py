import time

class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

def agregar_alumno():
    nif = input("NIF: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    aprobado = input("¿El alumno ha aprobado? (Sí/No): ").lower() == "sí"
    nuevo_alumno = Alumno(nif, nombre, apellidos, telefono, email, aprobado)
    alumnos.append(nuevo_alumno)
    print("Alumno añadido correctamente.")

def eliminar_alumno_por_nif():
    nif = input("NIF del alumno a eliminar: ")
    for alumno in alumnos:
        if alumno.nif == nif:
            alumnos.remove(alumno)
            print("Alumno eliminado correctamente.")
            return
    print("No hay ningún alumno con ese NIF.")

def actualizar_datos_por_nif():
    nif = input("NIF del alumno a actualizar: ")
    for alumno in alumnos:
        if alumno.nif == nif:
            alumno.nombre = input("Nuevo nombre: ")
            alumno.apellidos = input("Nuevos apellidos: ")
            alumno.telefono = input("Nuevo teléfono: ")
            alumno.email = input("Nuevo email: ")
            print("Datos del alumno actualizados correctamente.")
            return
    print("No hay ningún alumno con ese NIF.")

def mostrar_datos_por_nif():
    nif = input("NIF del alumno a mostrar: ")
    for alumno in alumnos:
        if alumno.nif == nif:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")
            return
    print("No hay ningún alumno con ese NIF.")

def mostrar_datos_por_email():
    email = input("Email del alumno a mostrar: ")
    for alumno in alumnos:
        if alumno.email == email:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")
            return
    print("No hay ningún alumno con ese email.")

def listar_todos_los_alumnos():
    if not alumnos:
        print("No hay ningún alumno en la lista.")
    else:
        for alumno in alumnos:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Teléfono: {alumno.telefono}, Email: {alumno.email}, Aprobado: {alumno.aprobado}")

def aprobar_alumno_por_nif():
    nif = input("NIF del alumno a aprobar: ")
    for alumno in alumnos:
        if alumno.nif == nif:
            alumno.aprobado = True
            print("Alumno aprobado correctamente.")
            return
    print("No hay ningún alumno con ese NIF.")

def suspender_alumno_por_nif():
    nif = input("NIF del alumno a suspender: ")
    for alumno in alumnos:
        if alumno.nif == nif:
            alumno.aprobado = False
            print("Alumno suspendido correctamente.")
            return
    print("No hay ningún alumno con ese NIF.")

def mostrar_alumnos_aprobados():
    aprobados = [alumno for alumno in alumnos if alumno.aprobado]
    if not aprobados:
        print("No hay alumnos aprobados.")
    else:
        for alumno in aprobados:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Aprobado: {alumno.aprobado}")

def mostrar_alumnos_suspendidos():
    suspendidos = [alumno for alumno in alumnos if not alumno.aprobado]
    if not suspendidos:
        print("No hay alumnos suspendidos.")
    else:
        for alumno in suspendidos:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Aprobado: {alumno.aprobado}")

#Aquí se genera la lista que va guardando los alumnos conforme se introducen sus datos
alumnos = []

while True:
    print("\nOpciones:")
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
        print("Apagando el programa...")
        time.sleep(2)
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")