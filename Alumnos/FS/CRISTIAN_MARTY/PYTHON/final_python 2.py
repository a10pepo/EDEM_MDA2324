#Lista vacia
alumnos = []

#####Creacion de Funciones

#Funcion para Nuevo alumno
def agregar_alumno():
        nif = input("NIF:")
        nombre = input("Nombre:")
        apellidos = input("Apellidos:")
        telefono = input("Teléfono:")
        email = input("Email:")
        aprobado = False
        suspendido = False
        nuevo_alumno = {
            "NIF": nif,
            "Nombre": nombre,
            "Apellidos": apellidos,
            "Teléfono": telefono,
            "Email": email,
            "Aprobado": aprobado,
            "Suspendido": suspendido
        }
        alumnos.append(nuevo_alumno)
        
        print("Alumno agregado con éxito")




#Eliminar alumno seleccionado
def eliminar_alumno_por_nif(nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumnos.remove(alumno)
            print(f"Alumno con NIF {nif} eliminado.")
            return
        
    print(f"No se encontró un alumno!")




#Actualizar un alumno seleccionado
def actualizar_datos_alumno(nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            nombre = input("Nuevo nombre: ")
            apellidos = input("Nuevos apellidos: ")
            telefono = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            alumno["Nombre"] = nombre
            alumno["Apellidos"] = apellidos
            alumno["Teléfono"] = telefono
            alumno["Email"] = email
            print(f"Datos del alumno actualizados.")
            return
        
    print(f"No se encontró un alumno!")





#Mostrar alumno seleccionado mediante NIF
def mostrar_datos_alumno_por_nif(nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            print("NIF:", alumno["NIF"])
            print("Nombre:", alumno["Nombre"])
            print("Apellidos:", alumno["Apellidos"])
            print("Teléfono:", alumno["Teléfono"])
            print("Email:", alumno["Email"])
            print("Aprobado:", alumno["Aprobado"])
            print("Suspendido:", alumno["Suspendido"])
            return
        
    print(f"No se encontró un alumno!")




#Mostrar alumno seleccionado mediante email
def mostrar_datos_alumno_por_email(email):
    for alumno in alumnos:
        if alumno["Email"] == email:
            print("NIF:", alumno["NIF"])
            print("Nombre:", alumno["Nombre"])
            print("Apellidos:", alumno["Apellidos"])
            print("Teléfono:", alumno["Teléfono"])
            print("Email:", alumno["Email"])
            print("Aprobado:", alumno["Aprobado"])
            print("Suspendido:", alumno["Suspendido"])
            return
        
    print(f"No se encontró ese alumno con este email...")




#Mostrar todos los alumnos
def mostrar_todos_los_alumnos():
    for alumno in alumnos:
        print("NIF:", alumno["NIF"])
        print("Nombre:", alumno["Nombre"])
        print("Apellidos:", alumno["Apellidos"])
        print("Teléfono:", alumno["Teléfono"])
        print("Email:", alumno["Email"])
        print("Aprobado:", alumno["Aprobado"])
        print("Suspendido:", alumno["Suspendido"])
        print()



#Aprobar alumno
def aprobar_alumno(nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Aprobado"] = True
            print(f"NIF: {alumno['NIF']} - Nombre: {alumno['Nombre']} - Aprobado: {alumno['Aprobado']}")
            return
        
    print(f"No se encontró alumno!!!")





#Suspender alumno
def suspender_alumno(nif):
    for alumno in alumnos:
        if alumno["NIF"] == nif:
            alumno["Suspendido"] = True
            print(f"NIF: {alumno['NIF']} - Nombre: {alumno['Nombre']} - Suspendido: {alumno['Suspendido']}")
            return
        
    print(f"No se encontró un alumno!!!")





####Display en consola-----------------------------------------------------

while True:
    print("\nOpciones:")
    print("1 - Añadir un alumno")
    print("2 - Eliminar alumno por NIF")
    print("3 - Actualizar datos de un alumno por NIF")
    print("4 - Mostrar datos de un alumno por NIF")
    print("5 - Mostrar datos de un alumno por Email")
    print("6 - Listar todos los alumnos")
    print("7 - Aprobar alumno por NIF")
    print("8 - Suspender alumno por NIF")
    print("9 - Mostrar alumnos aprobados")
    print("10 - Mostrar alumnos suspendidos")
    print("(X) Finalizar Programa")

    opcion = input("Elija una opción: ")





##########Armado de logica

    if opcion == '1':
        agregar_alumno()
    elif opcion == '2':
        nif = input("NIF del alumno a eliminar: ")
        eliminar_alumno_por_nif(nif)
    elif opcion == '3':
        nif = input("NIF del alumno cuyos datos desea actualizar: ")
        actualizar_datos_alumno(nif)
    elif opcion == '4':
        nif = input("NIF del alumno cuyos datos desea mostrar: ")
        mostrar_datos_alumno_por_nif(nif)
    elif opcion == '5':
        email = input("email del alumno cuyos datos desea mostrar: ")
        mostrar_datos_alumno_por_email(email)
    elif opcion == '6':
        mostrar_todos_los_alumnos()
    elif opcion == '7':
        nif = input("NIF del alumno a aprobar: ")
        aprobar_alumno(nif)
    elif opcion == '8':
        nif = input("NIF del alumno a suspender: ")
        suspender_alumno(nif)
    
    #------------------------------------
    
    elif opcion == '9':
        for alumno in alumnos:
            if alumno["Aprobado"]==True:
                print(f"NIF: {alumno['NIF']} - Nombre: {alumno['Nombre']} - Aprobado: {alumno['Aprobado']}")
    
    elif opcion == '10':
        for alumno in alumnos:
            if alumno["Suspendido"] == True:
                print(f"NIF: {alumno['NIF']} - Nombre: {alumno['Nombre']} - Suspendido: {alumno['Suspendido']}")
    
    
    #----------------------------------------
    
    elif opcion.upper() == 'X':
        break
    else:
        print("Has roto el programa!")
