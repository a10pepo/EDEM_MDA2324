"""
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
### Datos alumnos
alumnos = {
    "12345678A": {"nif": "12345678A", "nombre": "Juan", "apellidos": "Pérez García", "teléfono": "612345678", "email": "juan.perez@email.com", "aprobado": True},
    "87654321B": {"nif": "87654321B", "nombre": "Ana", "apellidos": "López Fernández", "teléfono": "698765432", "email": "ana.lopez@email.com", "aprobado": False},
    "23456789C": {"nif": "23456789C", "nombre": "Carlos", "apellidos": "García Martín", "teléfono": "623456789", "email": "carlos.garcia@email.com", "aprobado": True},
    "34567890D": {"nif": "34567890D", "nombre": "Lucía", "apellidos": "Martínez Sánchez", "teléfono": "634567890", "email": "lucia.martinez@email.com", "aprobado": False},
    "45678901E": {"nif": "45678901E", "nombre": "Marta", "apellidos": "Rodríguez López", "teléfono": "645678901", "email": "marta.rodriguez@email.com", "aprobado": True},
    "56789012F": {"nif": "56789012F", "nombre": "David", "apellidos": "Gómez Alonso", "teléfono": "656789012", "email": "david.gomez@email.com", "aprobado": False},
    "67890123G": {"nif": "67890123G", "nombre": "Sofía", "apellidos": "Jiménez Gil", "teléfono": "667890123", "email": "sofia.jimenez@email.com", "aprobado": True},
    "78901234H": {"nif": "78901234H", "nombre": "Óscar", "apellidos": "Ruiz Navarro", "teléfono": "678901234", "email": "oscar.ruiz@email.com", "aprobado": False},
    "89012345I": {"nif": "89012345I", "nombre": "Teresa", "apellidos": "Hernández Cabrera", "teléfono": "689012345", "email": "teresa.hernandez@email.com", "aprobado": True},
    "90123456J": {"nif": "90123456J", "nombre": "Sergio", "apellidos": "Sánchez Iglesias", "teléfono": "690123456", "email": "sergio.sanchez@email.com", "aprobado": False}
}


### Menu
def menu():
    print ("(1) Añadir un alumno")
    print ("(2) Eliminar alumno por NIF")
    print ("(3) Actualizar datos de un alumno por NIF")
    print ("(4) Mostrar datos de un alumno por NIF")
    print ("(5) Mostrar datos de un alumno por Email")
    print ("(6) Listar TODOS os alumnos")
    print ("(7) Aprobar Alumno por NIF")
    print ("(8) Suspender Alumno por NIF")
    print ("(9) Mostrar alumnos aprobados")
    print ("(10) Mostrar alumnos suspensos")
    print ("(X) Finalizar Programa")
    return (input('¿Qué quieres hacer? '))

### Añadir alumno
def add_alumno():
        print ("Vamos a añadir un alumno nuevo.")
        nif= input ("Introduce NIF: ")
        id = nif
        nombre= input ("Intoduce su nombre: ")
        apellidos= input ("Introduce sus apellidos: ")
        telefono= input ("Introduce un número de teléfono: ")
        correo= input ("introduce un correo electrónico: ")
        estado= input ("¿Está aprobado? [S]Sí - [N]No: ")
        if estado.upper == "S":
                return True
        elif estado.upper == "N":
                return False
        else:
                print ("Por favor introduzca [S] para sí o [N] para no.")
        alumnos.update ({id: {"nif": nif, "nombre": nombre, "apellidos": apellidos, "teléfono": telefono, "email": correo, "aprobado": estado}})

### Eliminar alumno
def eliminar_alumno():
    print("Vamos a eliminar a un alumno. Esta opción no se puede deshacer.")
    nif = input("Introduce su NIF: ")
    if nif in alumnos:
        del alumnos[nif]
        print(f"Alumno con NIF {nif} eliminado.")
    else:
        print("No se encontró el alumno.")

### Actualizar datos de un alumno por NIF
def actualizar_alumno():
    print ("A ver, mi rey. ¿A quién quieres actualizar?")
    nif= input ("Introduce NIF: ")
    id = nif
    nombre= input ("Intoduce su nombre: ")
    apellidos= input ("Introduce sus apellidos: ")
    telefono= input ("Introduce un número de teléfono: ")
    correo= input ("introduce un correo electrónico: ")
    estado= input ("¿Está aprobado? [S]Sí - [N]No: ")
    if estado.upper == "S":
                return True
    elif estado.upper == "N":
                return False
    else:
                print ("Por favor introduzca [S] para sí o [N] para no.")
    alumnos.update ({id: {"nif": nif, "nombre": nombre, "apellidos": apellidos, "teléfono": telefono, "email": correo, "aprobado": estado}})
    
### Mostrar datos de un alumno por NIF
def mostrar_datos_nif():
    id= input("Introduce el NIF del alumno que quieres saber sus datos: ")
    alumnos.get (id) 

### Mostrar datos de un alumno por email
def mostrar_datos_email():
       correo = input("Introduce el email del alumno: ")
       alumnos.get (correo)

### Listar todos los alumnos
def mostrar_alumnos():
    print("Estos son los alumnos:")
    for nif, datos in alumnos.items():
        print(f"NIF: {nif}, Datos: {datos}")

### Aprobar alumno por NIF
def aprobar_alumno():
    print("A ver, mi rey. ¿A quién quieres aprobar?")
    nif = input("Introduce NIF: ")
    if nif in alumnos:
        alumnos[nif]["aprobado"] = True
        print(f"Alumno con NIF {nif} ha sido aprobado.")
    else:
        print("No se encontró el alumno con ese NIF.")

### Suspender alumno por NIF
def suspender_alumno():
    print("A ver, mi rey. ¿A quién quieres suspender?")
    nif = input("Introduce NIF: ")
    if nif in alumnos:
        alumnos[nif]["aprobado"] = False
        print(f"Alumno con NIF {nif} ha sido suspendido.")
    else:
        print("No se encontró el alumno con ese NIF.")

### Mostrar alumnos aprobados
def lista_aprob_alumno():
    print("Esta es la lista de aprobados:")
    for nif, datos in alumnos.items():
        if datos["aprobado"]:
            print(f"NIF: {nif}, Nombre: {datos['nombre']}, Apellidos: {datos['apellidos']}")

### Mostrar alumnos suspensos
def lista_sus_alumno():
    print("Esta es la lista de aprobados:")
    for nif, datos in alumnos.items():
        if not datos["aprobado"]:
            print(f"NIF: {nif}, Nombre: {datos['nombre']}, Apellidos: {datos['apellidos']}")

### La vaina para que esto funcione
while True:
    opcion = menu()
    if opcion.upper() == "X":
        print("Cerrando el programa...")
        break
    elif opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            add_alumno()
        elif opcion == 2:
            eliminar_alumno()
        elif opcion == 3:
            actualizar_alumno()
        elif opcion == 4:
            mostrar_datos_nif()
        elif opcion == 6:
            mostrar_alumnos()
        elif opcion == 7:
            aprobar_alumno()
        elif opcion == 8:
            suspender_alumno() 
        elif opcion == 9:
            lista_aprob_alumno()
        elif opcion == 10:
            lista_sus_alumno()
    else:
        print("Por favor, elige una opción válida")