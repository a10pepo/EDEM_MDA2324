#CLASS CREATION:
class alumno:
    def __init__(self,NIF,Nombre,Apellidos,Telefono,Email,Aprobado):
        self.NIF:str = NIF
        self.Nombre:str = Nombre
        self.Apellidos:str = Apellidos
        self.Telefono:str = Telefono
        self.Email:str = Email
        self.Aprobado:bool = Aprobado   
#PREPARACIÓN LISTAS:
Lista_Alumnos = [
    alumno("123456789A", "Ana", "Martínez", "600-100-200", "ana.martinez@example.com", True),
    alumno("234567890B", "Luis", "Gómez", "600-200-300", "luis.gomez@example.com", False),
    alumno("345678901C", "Marta", "Rodríguez", "600-300-400", "marta.rodriguez@example.com", True),
    alumno("456789012D", "Pablo", "López", "600-400-500", "pablo.lopez@example.com", False),
    alumno("567890123E", "Laura", "García", "600-500-600", "laura.garcia@example.com", True),
    alumno("678901234F", "David", "Fernández", "600-600-700", "david.fernandez@example.com", False),
    alumno("789012345G", "Sara", "González", "600-700-800", "sara.gonzalez@example.com", True),
    alumno("890123456H", "Carlos", "Pérez", "600-800-900", "carlos.perez@example.com", False),
    alumno("901234567I", "Elena", "Sánchez", "600-900-100", "elena.sanchez@example.com", True),
    alumno("012345678J", "Jorge", "Díaz", "600-010-110", "jorge.diaz@example.com", False),
    alumno("135792468K", "Carmen", "Moreno", "600-020-120", "carmen.moreno@example.com", True),
    alumno("246813579L", "Antonio", "Jiménez", "600-030-130", "antonio.jimenez@example.com", False),
    alumno("369258147M", "Irene", "Ruiz", "600-040-140", "irene.ruiz@example.com", True),
    alumno("481369257N", "Mario", "Hernández", "600-050-150", "mario.hernandez@example.com", False),
    alumno("592481368O", "Clara", "Muñoz", "600-060-160", "clara.munoz@example.com", True),
    alumno("604813692P", "Álvaro", "Alonso", "600-070-170", "alvaro.alonso@example.com", False),
    alumno("715926483Q", "Patricia", "Gutiérrez", "600-080-180", "patricia.gutierrez@example.com", True),
    alumno("826349715R", "Ricardo", "Romero", "600-090-190", "ricardo.romero@example.com", False),
    alumno("937462859S", "Blanca", "Torres", "600-001-101", "blanca.torres@example.com", True),
    alumno("048573961T", "Víctor", "Ortiz", "600-002-102", "victor.ortiz@example.com", False)]

#DEFINICIÓN DE FUNCIONES

def nuevo_alumno ():
    print("\n ALTA NUEVO ALUMNO \n")
    NIF = input ("NIF (Sin espacios): ").lower().strip()
    Nombre = input ("Nombre: ").strip()
    Apellidos = input ("Apellidos: ").strip()
    Telefono = input ("Telefono: ").strip()
    Email = input ("Email: ").strip().lower()
    Aprobado = None
    while Aprobado is None:
        Aprobado_input:bool = input ("¿Alumno Aprobado? (S/N): ")
        if Aprobado_input =="S":
            Aprobado = True
        elif Aprobado_input == "N":
            Aprobado = False
        else :
            print ("Por favor, (S/N)")
    nuevo_alumno = alumno (NIF,Nombre,Apellidos,Telefono,Email,Aprobado)
    Lista_Alumnos.append(nuevo_alumno)
    print("\nALTA COMPLETADA\n")

def mostrar_total_alumnos ():
    if not Lista_Alumnos:
          print ("\nNO SE HAN REGISTRADO ALUMNOS TODAVÍA")
    else:
        print("\nALUMNOS:")
        print("-" * 140)
        print("{:<20} {:<20} {:<20} {:<20} {:<40} {:<20}".format("NIF","Nombre", "Apellidos", "Telefono", "Email","Aprobado"))
        print("-" * 140)
        for student in Lista_Alumnos:
            print("{:<20} {:<20} {:<20} {:<20} {:<40} {:<20}".format(student.NIF, student.Nombre, student.Apellidos, student.Telefono, student.Email, "Sí" if student.Aprobado else "No"))

def eliminar_alumno ():
    NIF_para_borrar = input("\n Por favor introduce el NIF para buscar y borrar registro: ").lower().strip()
    alumno_NIF = None
    for alumno in Lista_Alumnos:
        if alumno.NIF == NIF_para_borrar:
            alumno_NIF = alumno
            break
    if alumno_NIF:
        Lista_Alumnos.remove(alumno_NIF)
        print(f'\n EL ALUMNO CON NIF:{alumno_NIF.NIF} HA SIDO DADO DE BAJA')
    else:
        print(f'\n NO SE HA ENCONTRADO EL NIF')

def actualizar_alumno():
    NIF_busqueda = input("Ingrese el NIF del alumno a actualizar: ").strip()

    alumno_encontrado = None
    for alumno in Lista_Alumnos:
        if alumno.NIF == NIF_busqueda:
            alumno_encontrado = alumno
            break

    if alumno_encontrado:
        print(f"\nDatos actuales de {alumno_encontrado.Nombre} {alumno_encontrado.Apellidos}:")
        print(f"NIF: {alumno_encontrado.NIF}")
        print(f"Nombre: {alumno_encontrado.Nombre}")
        print(f"Apellidos: {alumno_encontrado.Apellidos}")
        print(f"Telefono: {alumno_encontrado.Telefono}")
        print(f"Email: {alumno_encontrado.Email}")
        print(f"Aprobado: {'Sí' if alumno_encontrado.Aprobado else 'No'}")

        nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ").strip()
        nuevos_apellidos = input("Ingrese los nuevos apellidos (deje en blanco para no cambiar): ").strip()
        nuevo_telefono = input("Ingrese el nuevo teléfono (deje en blanco para no cambiar): ").strip()
        nuevo_email = input("Ingrese el nuevo email (deje en blanco para no cambiar): ").strip()
        nuevo_aprobado_input = input("¿Está aprobado? (S/N, deje en blanco para no cambiar): ").strip().upper()

        if nuevo_nombre:
            alumno_encontrado.Nombre = nuevo_nombre
        if nuevos_apellidos:
            alumno_encontrado.Apellidos = nuevos_apellidos
        if nuevo_telefono:
            alumno_encontrado.Telefono = nuevo_telefono
        if nuevo_email:
            alumno_encontrado.Email = nuevo_email
        if nuevo_aprobado_input in ["S", "N"]:
            alumno_encontrado.Aprobado = True if nuevo_aprobado_input == "S" else False

        print("\nDatos actualizados con éxito.")
    else:
        print("No se encontró un alumno con ese NIF.")

def mostrar_datos_alumno_nif ():
    NIF_busqueda = input("Ingrese el NIF del alumno a buscar: ").strip()

    alumno_encontrado = None
    for alumno in Lista_Alumnos:
        if alumno.NIF == NIF_busqueda:
            alumno_encontrado = alumno
            break

    if alumno_encontrado:
        print(f"\nDatos actuales de {alumno_encontrado.Nombre} {alumno_encontrado.Apellidos}:")
        print(f"NIF: {alumno_encontrado.NIF}")
        print(f"Nombre: {alumno_encontrado.Nombre}")
        print(f"Apellidos: {alumno_encontrado.Apellidos}")
        print(f"Telefono: {alumno_encontrado.Telefono}")
        print(f"Email: {alumno_encontrado.Email}")
        print(f"Aprobado: {'Sí' if alumno_encontrado.Aprobado else 'No'}")

    else:
        print("No se encontró un alumno con ese NIF.")


def mostrar_datos_alumno_email ():
    Email_busqueda = input("Ingrese el Email del alumno a buscar: ").strip()

    alumno_encontrado = None
    for alumno in Lista_Alumnos:
        if alumno.Email == Email_busqueda:
            alumno_encontrado = alumno
            break

    if alumno_encontrado:
        print(f"\nDatos actuales de {alumno_encontrado.Nombre} {alumno_encontrado.Apellidos}:")
        print(f"NIF: {alumno_encontrado.NIF}")
        print(f"Nombre: {alumno_encontrado.Nombre}")
        print(f"Apellidos: {alumno_encontrado.Apellidos}")
        print(f"Telefono: {alumno_encontrado.Telefono}")
        print(f"Email: {alumno_encontrado.Email}")
        print(f"Aprobado: {'Sí' if alumno_encontrado.Aprobado else 'No'}")

    else:
        print("No se encontró un alumno con ese Email.")

def aprobar_alumno_por_nif():
    NIF_busqueda = input("Ingrese el NIF del alumno a aprobar: ").strip()
    alumno_encontrado = None
    for alumno in Lista_Alumnos:
        if alumno.NIF == NIF_busqueda:
            alumno_encontrado = alumno
            break

    if alumno_encontrado:
        if alumno_encontrado.Aprobado:
            print(f"El alumno con NIF {alumno_encontrado.NIF} ya está aprobado.")
        else:
            alumno_encontrado.Aprobado = True
            print(f"El alumno con NIF {alumno_encontrado.NIF} ha sido aprobado exitosamente.")
    else:
        print("No se encontró un alumno con ese NIF.")

def suspender_alumno_por_nif():
    NIF_busqueda = input("Ingrese el NIF del alumno a suspender: ").strip()
    alumno_encontrado = None
    for alumno in Lista_Alumnos:
        if alumno.NIF == NIF_busqueda:
            alumno_encontrado = alumno
            break

    if alumno_encontrado:
        if alumno_encontrado.Aprobado == False:
            print(f"El alumno con NIF {alumno_encontrado.NIF} ya está suspenso.")
        else:
            alumno_encontrado.Aprobado = False
            print(f"El alumno con NIF {alumno_encontrado.NIF} ha sido suspendido exitosamente.")
    else:
        print("No se encontró un alumno con ese NIF.")

def mostrar_alumnos_aprobados():
    if not Lista_Alumnos:
        print("\nNO SE HAN REGISTRADO ALUMNOS TODAVÍA")
    else:
        print("\nALUMNOS APROBADOS:")
        print("-" * 140)
        print("{:<20} {:<20} {:<20} {:<20} {:<40} {:<20}".format("NIF", "Nombre", "Apellidos", "Telefono", "Email", "Nota"))
        print("-" * 140)
        for student in Lista_Alumnos:
            if student.Aprobado:
                print("{:<20} {:<20} {:<20} {:<20} {:<40} {:<20}".format(student.NIF, student.Nombre, student.Apellidos, student.Telefono, student.Email, "Aprobado"))


def mostrar_alumnos_suspendidos():
    if not Lista_Alumnos:
        print("\nNO SE HAN REGISTRADO ALUMNOS TODAVÍA")
    else:
        print("\nALUMNOS SUSPENDIDOS:")
        print("-" * 140)
        print("{:<20} {:<20} {:<20} {:<20} {:<40} {:<20}".format("NIF", "Nombre", "Apellidos", "Telefono", "Email", "Nota"))
        print("-" * 140)
        for student in Lista_Alumnos:
            if student.Aprobado == False:
                print("{:<20} {:<20} {:<20} {:<20} {:<40} {:<20}".format(student.NIF, student.Nombre, student.Apellidos, student.Telefono, student.Email, "Suspendido"))
