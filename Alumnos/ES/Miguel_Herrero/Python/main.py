import json

# Definimos la función para cargar los alumnos desde el archivo JSON
def cargar_alumnos():
    try:
        with open('alumnos.json', 'r') as archivo:
            alumnos = json.load(archivo)
    except FileNotFoundError:
        alumnos = {}
    return alumnos

# Definimos la función para guardar los alumnos en el archivo JSON
def guardar_alumnos(alumnos):
    with open('alumnos.json', 'w') as archivo:
        json.dump(alumnos, archivo, indent=2)

# Definimos la función para añadir un nuevo alumno
def agregar_alumno():
    nif = input("NIF: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    aprobado = True 
    
    alumno = {
        "NIF": nif,
        "Nombre": nombre,
        "Apellidos": apellidos,
        "Telefono": telefono,
        "Email": email,
        "Aprobado": aprobado
    }
    
    return alumno

# Definimos la función para eliminar un alumno por NIF
def eliminar_alumno(nif, alumnos):
    if nif in alumnos:
        del alumnos[nif]
        print(f"El alumno con NIF {nif} ha sido eliminado.")
    else:
        print(f"No se ha encontrado un alumno con NIF {nif}.")

# Definimos la función para actualizar datos de un alumno por NIF
def actualizar_alumno(nif, alumnos):
    if nif in alumnos:
        print(f"Actualización de los datos del alumno con NIF {nif}:")
        nuevo_alumno = agregar_alumno()
        alumnos[nif] = nuevo_alumno
        print(f"Los datos del alumno con NIF {nif} han sido actualizados.")
    else:
        print(f"No se ha encontrado un alumno con NIF {nif}.")

# Definimos la función para mostrar datos de un alumno por NIF
def mostrar_alumno_por_nif(nif, alumnos):
    if nif in alumnos:
        print("Datos del alumno:")
        print(json.dumps(alumnos[nif], indent=2))
    else:
        print(f"No se ha encontrado un alumno con NIF {nif}.")

# Definimos la función para mostrar datos de un alumno por Email
def mostrar_alumno_por_email(email, alumnos):
    encontrado = False
    for alumno in alumnos.values():
        if alumno["Email"] == email:
            print("Datos del alumno:")
            print(json.dumps(alumno, indent=2))
            encontrado = True
            break
    if not encontrado:
        print(f"No se ha encontrado un alumno con Email {email}.")

# Definimos la función para listar a todos los alumnos
def listar_alumnos(alumnos):
    print("Esta es la lista de todos los alumnos:")
    for alumno in alumnos.values():
        print(json.dumps(alumno, indent=2))
        print("---------------------------")

# Definimos la función para aprobar a un alumno por NIF
def aprobar_alumno(nif, alumnos):
    if nif in alumnos:
        alumnos[nif]["Aprobado"] = True
        print(f"El alumno con NIF {nif} ha aprobado.")
    else:
        print(f"No se ha encontrado un alumno con NIF {nif}.")

# Definimos la función para suspender a un alumno por NIF
def suspender_alumno(nif, alumnos):
    if nif in alumnos:
        alumnos[nif]["Aprobado"] = False
        print(f"El alumno con NIF {nif} ha suspendido.")
    else:
        print(f"No se ha encontrado ningún alumno con NIF {nif}.")

# Definimos la función para mostrar todos los alumnos aprobados
def mostrar_aprobados(alumnos):
    aprobados = []
    print("Estos son los alumnos aprobados:")
    
    for alumno in alumnos.values():
        if alumno["Aprobado"]:
            aprobados.append(alumno)
    
    for alumno in aprobados:
        print(json.dumps(alumno, indent=2))
        print("---------------------------")


# Definimos la función para mostrar todos los alumnos suspendidos
def mostrar_suspendidos(alumnos):
    suspendidos = []
    print("Estos son los alumnos suspendidos:")
    
    for alumno in alumnos.values():
        if not alumno["Aprobado"]:
            suspendidos.append(alumno)
    
    for alumno in suspendidos:
        print(json.dumps(alumno, indent=2))
        print("---------------------------")

# Definimos el programa principal
if __name__ == "__main__":
    alumnos = cargar_alumnos()

    while True:
        print("\nMenú:")
        print("(1) Añadir un alumno")
        print("(2) Eliminar alumno por NIF")
        print("(3) Actualizar datos de un alumno por NIF")
        print("(4) Mostrar datos de un alumno por NIF")
        print("(5) Mostrar datos de un alumno por Email")
        print("(6) Listar Todos los alumnos")
        print("(7) Aprobar a un Alumno por NIF")
        print("(8) Suspender a un Alumno por NIF")
        print("(9) Mostrar los alumnos aprobados")
        print("(10) Mostrar los alumnos suspendidos")
        print("(X) Finalizar Programa")

        opcion = input("\nSeleccione una opción: ").upper()

        if opcion == "1":
            nuevo_alumno = agregar_alumno()
            alumnos[nuevo_alumno["NIF"]] = nuevo_alumno
            print("\n----- ALUMNO AÑADIDO -----")

        elif opcion == "2":
            nif_eliminar = input("Ingrese el NIF del alumno a eliminar: ")
            eliminar_alumno(nif_eliminar, alumnos)

        elif opcion == "3":
            nif_actualizar = input("Ingrese el NIF del alumno a actualizar: ")
            actualizar_alumno(nif_actualizar, alumnos)

        elif opcion == "4":
            nif_mostrar = input("Ingrese el NIF del alumno a mostrar: ")
            mostrar_alumno_por_nif(nif_mostrar, alumnos)

        elif opcion == "5":
            email_mostrar = input("Ingrese el Email del alumno a mostrar: ")
            mostrar_alumno_por_email(email_mostrar, alumnos)

        elif opcion == "6":
            listar_alumnos(alumnos)

        elif opcion == "7":
            nif_aprobar = input("Ingrese el NIF del alumno a aprobar: ")
            aprobar_alumno(nif_aprobar, alumnos)

        elif opcion == "8":
            nif_suspender = input("Ingrese el NIF del alumno a suspender: ")
            suspender_alumno(nif_suspender, alumnos)

        elif opcion == "9":
            mostrar_aprobados(alumnos)
                              
        elif opcion == "10":
            mostrar_suspendidos(alumnos)

        elif opcion == "X":
            print("\n----- PROGRAMA FINALIZADO -----")
            break

        else:
            print("\nEsta opción no es válida. Seleccione una de las opciones disponibles en el Menú.")

    # Guardamos los cambios en el archivo JSON al finalizar el programa
    guardar_alumnos(alumnos)


