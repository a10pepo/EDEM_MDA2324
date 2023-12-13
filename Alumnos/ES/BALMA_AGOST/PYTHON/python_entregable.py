''' Una empresa de formación quiere gestionar su cartera de alumnos.

Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

NIF (string)
Nombre (string)
Apellidos (string)
Teléfono (string)
Email (string)
Aprobado (boolean) 

(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS los alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X '''

alumnos = {}
lista_alumnos = []
    
# AÑADIR ALUMNO

def añadir_alumno(alumnos):
    
    NIF_alumno = str(input("Ingrese NIF del alumno: "))
    nombre_alumno = str(input("Ingrese el nombre del alumno: "))
    apellidos_alumno = str(input("Ingrese los apellidos del alumno: "))
    telefono_alumno = str(input("Ingrese el teléfono del alumno: "))
    email_alumno = str(input("Ingrese el email del alumno: "))
    aprobado = bool(input("Indique si el alumno ha aprobado (S/N): ").lower() == 's')

    alumnos[NIF_alumno] = {
        "NIF": NIF_alumno,
        "Nombre": nombre_alumno,
        "Apellidos": apellidos_alumno,
        "Telefono": telefono_alumno,
        "Email": email_alumno,
        "Aprobado": aprobado
    }

    print("Alumno añadido correctamente.")


# ELIMINAR ALUMNO POR NIF

def eliminar_alumno(alumnos):
    
    NIF_alumno = str(input('Ingrese NIF del alumno que desea eliminar: '))
    if NIF_alumno in alumnos:
        del alumnos[NIF_alumno]
        print("Alumno eliminado correctamente")
    else:
        print("Alumno no encontrado")

# ACTUALIZAR ALUMNO POR NIF

def actualizar_alumno(alumnos):
    
    NIF_alumno = str(input('Ingrese NIF del alumno que desea actualizar: '))
    if NIF_alumno in alumnos:
        alumno = alumnos[NIF_alumno]
        alumno['Nombre'] = input(f"Nuevo nombre para {alumno['Nombre']}: ")
        alumno['Apellidos'] = input(f"Nuevos apellidos para {alumno['Apellidos']}: ")
        alumno['Telefono'] = input(f"Nuevo teléfono para {alumno['Telefono']}: ")
        alumno['Email'] = input(f"Nuevo email para {alumno['Email']}: ")
        print("Los datos han sido actualizados correctamente")
    else:
        print("Alumno no encontrado.")

# MOSTRAR ALUMNO POR NIF

def mostrar_datos_por_nif(alumnos):
    
    NIF_alumno = str(input('Ingrese NIF del alumno que desea mostrar: '))
    if NIF_alumno in alumnos:
        alumno = alumnos[NIF_alumno]
        print(f"NIF: {NIF_alumno}")
        print(f"Nombre: {alumno['Nombre']}")
        print(f"Apellidos: {alumno['Apellidos']}")
        print(f"Telefono: {alumno['Telefono']}")
        print(f"Email: {alumno['Email']}")
        print(f"Aprobado: {'Si' if alumno['Aprobado'] else 'No'}")
    else:
        print("Alumno no encontrado.")

# MOSTRAR ALUMNO POR EMAIL

def mostrar_datos_por_email(alumnos):
    
    email_alumno = str(input('Ingrese email del alumno que desea mostrar: '))
    for alumno in alumnos.values():
        if alumno['Email'] == email_alumno:
            print(f"NIF: {alumno['NIF']}")
            print(f"Nombre: {alumno['Nombre']}")
            print(f"Apellidos: {alumno['Apellidos']}")
            print(f"Telefono: {alumno['Telefono']}")
            print(f"Email: {alumno['Email']}")
            print(f"Aprobado: {'Sí' if alumno['Aprobado'] else 'No'}")
            
    else:
        print("Alumno no encontrado.")

# MOSTRAR TODOS LOS ALUMNOS 

def listar_alumnos(alumnos):
    
    for NIF_alumno, alumno in alumnos.items():
        print(f"NIF: {NIF_alumno} Nombre: {alumno['Nombre']} {alumno['Apellidos']}")

    if not alumnos:
        print("No hay alumnos registrados.")

# APROBAR ALUMNO POR NIF

def aprobar_alumno_por_nif(alumnos):
    
    NIF = str(input('Ingrese el NIF del alumno: '))
    if NIF in alumnos:
        alumnos[NIF]['Aprobado'] = True
        print('Alumno aprobado')
    else:
        print('Alumno no encontrado.')

# SUSPENDER ALUMNO POR NIF

def suspender_alumno_por_nif(alumnos):
    
    NIF = str(input('Ingrese el NIF del alumno: '))
    if NIF in alumnos:
        alumnos[NIF]['Aprobado'] = False
        print('Alumno suspendido')
    else:
        print('Alumno no encontrado.')

# LISTAR ALUMNOS APROBADOS

def listar_alumnos_aprobados(alumnos):
    print("Listado de todos los alumnos aprobados: ")
    for NIF_alumno, alumno in alumnos.items():
        if alumno['Aprobado']:
            print(f"NIF: {NIF_alumno} Nombre: {alumno['Nombre']} {alumno['Apellidos']}")


# LISTAR ALUMNOS SUSPENSOS

def listar_alumnos_suspendidos(alumnos):
    print("Listado de todos los alumnos suspensos: ")
    for NIF_alumno, alumno in alumnos.items():
        if not alumno['Aprobado']:
            print(f"NIF: {NIF_alumno} Nombre: {alumno['Nombre']} {alumno['Apellidos']}")

# ---------------------------------------------


opcion_escogida = ''

while opcion_escogida != 'X':
    opcion_escogida = input(
       
  '''
            Hola, escoge una opción:
            1. Añadir alumno
            2. Eliminar alumno por NIF
            3. Actualizar datos de un alumno por NIF
            4. Mostrar datos de un alumno por NIF
            5. Mostrar datos de un alumno por Email
            6. Listar TODOS los alumnos
            7. Aprobar Alumno por NIF
            8. Suspender Alumno por NIF
            9. Mostrar alumnos aprobados
            10. Mostrar alumnos suspensos
            X. Finalizar Programa 

            '''
    )

    if opcion_escogida == '1':
        añadir_alumno(alumnos)
    elif opcion_escogida == '2':
        eliminar_alumno(alumnos)
    elif opcion_escogida == '3':
        actualizar_alumno(alumnos)
    elif opcion_escogida == '4':
            mostrar_datos_por_nif(alumnos)
    elif opcion_escogida == '5':
            mostrar_datos_por_email(alumnos)
    elif opcion_escogida == '6':
            listar_alumnos(alumnos)
    elif opcion_escogida == '7':
            aprobar_alumno_por_nif(alumnos)
    elif opcion_escogida == '8':
            suspender_alumno_por_nif(alumnos)
    elif opcion_escogida == '9':
            listar_alumnos_aprobados(alumnos)
    elif opcion_escogida == '10':
            listar_alumnos_suspendidos(alumnos)
    elif opcion_escogida == 'X':
        break