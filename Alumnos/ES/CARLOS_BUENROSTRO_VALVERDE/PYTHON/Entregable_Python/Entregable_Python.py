# # Proyecto Final - Curso Python - EDEM_MDA2324


# Una empresa de formación quiere gestionar su cartera de alumnos. 

# Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

# - NIF (string)
# - Nombre (string)
# - Apellidos (string)
# - Teléfono (string)
# - Email (string)
# - Aprobado (boolean)

# El programa debe mostrar las siguientes opciones por consola para que escoja el usuario:

# (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno

# (2) Eliminar alumno por NIF

# (3) Actualizar datos de un alumno por NIF

# (4) Mostrar datos de un alumno por NIF

# (5) Mostrar datos de un alumno por Email

# (6) Listar TODOS os alumnos

# (7) Aprobar Alumno por NIF

# (8) Suspender Alumno por NIF

# (9) Mostrar alumnos aprobados

# (10) Mostrar alumnos suspensos

# (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X

lista_alumnos = []
alumnos = {}

def añadir_alumno():
    nif = str(input("Introduzca el NIF del alumno, por favor: "))
    nombre = str(input("Introduzca el nombre del alumno, por favor: "))
    apellidos = str(input("Introduzca los apellidos del alumno, por favor: "))
    telefono = str(input("Introduzca el teléfono del alumno, por favor: "))
    email = str(input("Introduzca el email del alumno, por favor: "))
    aprobado = bool(input("Inserte si el alumno ha aprobado: S/N: "))
    alumnos[nif] = {
        "NIF": nif,
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "aprobado": aprobado
    }

    print("El alumno ha sido añadido correctamente a la base de datos.")
    
def eliminar_alumno_nif():
    nif = input("Introduzca el NIF del alumno que desee eliminar, por favor: ")
    if nif in alumnos:
        del alumnos[nif]
        print(f"El alumno con el NIF {nif} ha sido eliminado de forma exitosa de la base de datos.")
    else:
        print(f"No se encontró ningún alumno con el NIF {nif} en nuestra base de datos.")

def actualizar_alumno_nif():
    nif = input("Introduzca el NIF del alumno que desee actualizar sus datos, por favor: ")
    if nif in alumnos:
        alumnos[nif]["nombre"] = input("Introduzca el nuevo nombre del alumno, por favor: ")
        alumnos[nif]["apellidos"] = input("Introduzca los nuevos apellidos del alumno, por favor: ")
        alumnos[nif]["telefono"] = input("Introduzca el nuevo teléfono del alumno, por favor: ")
        alumnos[nif]["email"] = input("Introduzca el nuevo email del alumno, por favor: ")
        print(f"Los datos del alumno con NIF {nif} han sido actualizados con éxito.")
    else:
        print(f"No se encontró ningún alumno con el NIF {nif} en nuestra base de datos.")

def mostrar_datos_nif():
    nif = input("Introduzca el NIF del alumno para poder conocer sus datos, por favor: ")
    if nif in alumnos:
        print("Datos del alumno seleccionado: ")
        print(f"El NIF del alumno es: {nif}")
        print(f"El nombre del alumno es: {alumnos[nif]['nombre']}")
        print(f"Los apellidos del alumno son: {alumnos[nif]['apellidos']}")
        print(f"El teléfono del alumno es: {alumnos[nif]['telefono']}")
        print(f"El email del alumno es: {alumnos[nif]['email']}")
        print(f"Expediente del alumno: {alumnos[nif]['aprobado']}")
    else:
        print(f"No se encontró ningún alumno con el NIF {nif} en nuestra base de datos.")

def mostrar_datos_email():
    email = str(input("Introduzca el email del alumno para poder conocer sus datos, por favor: "))
    for alumno in alumnos.values():
        if alumno['email'] == email:
            print("Datos del alumno seleccionado: ")
            print(f"El NIF del alumno es: {alumno['nif']}")
            print(f"El nombre del alumno es: {alumno['nombre']}")
            print(f"Los apellidos del alumno son: {alumno['apellidos']}")
            print(f"El teléfono del alumno es: {alumno['telefono']}")
            print(f"El email del alumno es: {alumno['email']}")
            print(f"Expediente del alumno: {alumno['aprobado']}")
        else:
            print(f"No se encontró ningún alumno con el email {email} en nuestra base de datos.")

def listar_alumnos():
    print("El listado de todos los alumnos registrados en la base de datos es el siguiente: ")
    for alumno in alumnos.values():
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")
        print("*******************************")

def aprobar_alumno_nif():
    nif = input("Introduzca el NIF del alumno que tiene que aprobar: ")
    if nif in alumnos and alumnos[nif]["aprobado"] == True:
        print(f"El alumno con NIF {nif} está aprobado")
    else:
        print("El alumno no está aprobado.")

def suspender_alumno_nif():
    nif = input("Introduzca el NIF del alumno que tiene que suspender: ")
    if alumnos[nif]["aprobado"] == False:
        print(f"El alumno con NIF {nif} se encuentra suspendido.")
    else:
        print(f"El alumno con NIF {nif} está aprobado.")

def listar_alumnos_aprobados():
    print("El listado de los alumnos aprobados es el siguiente: ")
    for alumno in alumnos.values():
        if alumno['aprobado'] == True:
            for clave, valor in alumno.items():
                print(f"{clave}: {valor}")
        print("*******************************")

def listar_alumnos_suspendidos():
    print("El listado de los alumnos suspendidos es el siguiente: ")
    for alumno in alumnos.values():
        if alumno['aprobado'] == False:
            for clave, valor in alumno.items():
                print(f"{clave}: {valor}")
        print("*******************************")

while True:
    print("""
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
      """)
    
    seleccion = input("Introduzca la selección deseada: ")

    if seleccion == "1":
        añadir_alumno()
    elif seleccion == "2":
        eliminar_alumno_nif()
    elif seleccion == "3":
        actualizar_alumno_nif()
    elif seleccion == "4":
        mostrar_datos_nif()
    elif seleccion == "5":
        mostrar_datos_email()
    elif seleccion == "6":
        listar_alumnos()
    elif seleccion == "7":
        aprobar_alumno_nif()
    elif seleccion == "8":
        suspender_alumno_nif()
    elif seleccion == "9":
        listar_alumnos_aprobados()
    elif seleccion == "10":
        listar_alumnos_suspendidos()
    elif seleccion =="x":
        print("Muchas gracias. Nos vemos a la próxima.")
        exit()