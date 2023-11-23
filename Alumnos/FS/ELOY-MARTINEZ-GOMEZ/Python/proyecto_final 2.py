# ------------------ CLASE ALUMNO -----------------------------------------
class Alumno(): # Clase Alumno donde inicializamos todos los campos descritos en el enunciado.
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado):
        self.nif: str = nif
        self.nombre: str = nombre
        self.apellidos: str = apellidos
        self.telefono: str = telefono
        self.email: str = email
        self.aprobado: bool = aprobado
        print(f"\nEl alumno: {self.nombre} se ha creado correctamente.")
    
    def __str__(self):
        resultado = "Aprobado" if self.aprobado else "Suspendido"
        return f"- Nombre: {self.nombre} {self.apellidos} ({self.nif}) \n- Telefono de contacto: {self.telefono}\n- E-mail: {self.email}\n- {resultado} "
# -------------------------------------------------------------------------

# ------ LISTADO POR DEFECTO PARA COMPROBAR FUNCIONALIDAD ------------------
# alumno_defecto_1 = Alumno(nif="1234A", nombre="A", apellidos="1", telefono="1234", email="gmail", aprobado=True)
# alumno_defecto_2 = Alumno(nif="1234B", nombre="B", apellidos="2", telefono="5678", email="yahoo", aprobado=True)
# alumno_defecto_3 = Alumno(nif="1234C", nombre="C", apellidos="3", telefono="4321", email="private", aprobado=False)
# alumno_defecto_4 = Alumno(nif="1234D", nombre="D", apellidos="4", telefono="8765", email="hotmail", aprobado=True)
# lista_alumnos = [alumno_defecto_1, alumno_defecto_2, alumno_defecto_3, alumno_defecto_4]
# --------------------------------------------------------------------------

lista_alumnos = [] # Lista de alumnos donde los almacenaremos durante el funcionamiento del script

# ------------------ FUNCIONALIDAD -----------------------------------------
def crear_alumno():
    """ Función para añadir los datos del alumno y añadirlo a la lista.
        En caso de que uno de los campos este mal, te redirige al menú. """
    nif: str = input("Introduce el nif: ")
    nombre: str = input("Introduce el nombre: ")
    apellidos: str = input("Introduce el apellido: ")
    telefono: str = input("Introduce el teléfono: ")
    email: str = input("Introduce el email: ")
    aprobado: str = input("Esta aprobado? [y/n] ")
    
    if aprobado == "y" or aprobado == "Y":
        aprobado = True
    elif aprobado == "n" or aprobado == "N":
        aprobado = False
    else:
        print("El dato introducido es erróneo... Vuelve a intentarlo de nuevo.")
        return None
    alumno = Alumno(nif=nif, nombre=nombre, apellidos=apellidos, telefono=telefono,
                    email=email, aprobado=aprobado)
    lista_alumnos.append(alumno)

def eliminar_alumno(nif):
    """ Función que recibe por parametro del nif del alumno, lo busca en la lista y lo elimina.
        En caso de que no encuentre el alumno o el nif no sea válido, te redirige al menú. """
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            lista_alumnos.remove(alumno)
            print(f"El alumno {alumno.nombre} {alumno.apellidos} ({alumno.nif}) ha sido eliminado de la lista con éxito.")   
            return True
    return False

def actualizar_datos(nif):
    """ Función que recibe por parametro del nif del alumno, lo busca en la lista y lo actualiza.
        Si pulsas el intro y el campo está vacío, pasa al siguiente campo, si está vacío no lo actualiza.
        En caso de que no encuentre el alumno o el nif no sea válido, te redirige al menú. """
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            print("Si presionas enter, se usará el valor ya guardado.")
            nif: str = input("Introduce el nuevo nif: ")
            if nif != "":
                alumno.nif = nif
            else:
                pass
            nombre: str = input("Introduce el nuevo nombre: ")
            if nombre != "":
                alumno.nombre = nombre
            else:
                pass
            apellidos: str = input("Introduce el nuevo apellido: ")
            if apellidos != "":
                alumno.apellidos = apellidos
            else:
                pass
            telefono: str = input("Introduce el nuevo teléfono: ")
            if telefono != "":
                alumno.telefono = telefono
            else:
                pass
            email: str = input("Introduce el nuevo email: ")
            if email != "":
                alumno.email = email
            else:
                pass
            aprobado: str = input("Sigue aprobado? [y/n] ")
            if aprobado != "":
                alumno.aprobado = aprobado
            else:
                pass
            print("\nDatos actualizados:\n")
            print("-----ALUMNO------")
            print(alumno)
            print("-----------------")
            return True
    return False 

def mostrar_alumno_por_nif(nif):
    """ Función que recibe por parametro del nif del alumno, lo busca en la lista y lo muestra por pantalla.
        En caso de que no encuentre el alumno o el nif no sea válido, te redirige al menú. """
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            print("-----ALUMNO------")
            print(alumno)
            print("-----------------")
            return True
    return False

def mostrar_alumno_por_mail(email):
    """ Función que recibe por parametro del email del alumno, lo busca en la lista y lo muestra por pantalla.
        En caso de que no encuentre el alumno o el nif no sea válido, te redirige al menú. """
    for alumno in lista_alumnos:
        if alumno.email == email:
            print("-----ALUMNO------")
            print(alumno)
            print("-----------------")
            return True
    return False

def mostrar_alumnos():
    """ Función que muestra por pantalla todos los alumnos de la lista."""
    for alumno in lista_alumnos:
        print("-----ALUMNO------")
        print(alumno)
        print("-----------------")

def nota_alumno(nif, aprobado: bool):
    """ Función que recibe por parametro del nif del alumno y si debe aprobarlo (aprobado=True),
        o suspenderlo (aprobado=False).
        En caso de que no encuentre el alumno o el nif no sea válido, te redirige al menú. """
    for alumno in lista_alumnos:
        if alumno.nif == nif:
            resultado = "aprobado" if aprobado else "suspendido"
            if alumno.aprobado != aprobado:
                alumno.aprobado = aprobado
                print(f"El alumno {alumno.nombre} {alumno.apellidos} ({alumno.nif}) ha sido {resultado}.")
                return True
            else:
                print(f"El alumno {alumno.nombre} {alumno.apellidos} ({alumno.nif}) ya estaba {resultado}.")
                return True
    return False

def mostrar_alumno_por_nota(aprobado: bool):
    """ Función que recibe por parametro si buscamos los alumnos aprobados (aprobado=True),
        o suspendidos (aprobado=False) y los muestra por pantalla. """
    alumnos_aprobado = [alumno.aprobado for alumno in lista_alumnos if alumno.aprobado == aprobado] # Creamos una lista que nos permita saber si hay o no alumnos
    if len(alumnos_aprobado) == 0:
        resultado = "aprobados" if aprobado else "suspendidos"
        print(f"No hay alumnos {resultado}.")
    for alumno in lista_alumnos:
        if alumno.aprobado == aprobado:
            print("-----ALUMNO------")
            print(alumno)
            print("-----------------")
    return True
# --------------------------------------------------------------------------

opciones_menu = """\nSELECCIONA UNA OPCIÓN:\n
(1) Añadir un alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS los alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa\n"""

# ------------------------ BUCLE WHILE -------------------------------
menu = True
while menu:
    print(opciones_menu)
    
    # Creamos la opción de interrumpir por teclado.
    try:
        opcion_elegida = input("Opción Elegida: ")
    except KeyboardInterrupt:
        print("\nCierre forzado.")
        break
    if len(lista_alumnos) > 0: # Opción solo disponible si ya existe algún alumno
        # Creamos un "switch" con lógica if-elif-else
        if opcion_elegida == "X" or opcion_elegida == "x": # (X) Finalizar Programa
            print("Programa finalizado con éxito.")
            menu = False
        elif opcion_elegida == "1": # (1) Añadir un alumno
            print("(1) Añadir un alumno")
            crear_alumno()
        elif opcion_elegida == "2": # (2) Eliminar alumno por NIF
            nif = input("Introduce el nif del alumno que desea eliminar: ")
            output = eliminar_alumno(nif)
            if not output:
                print(f"El alumno con nif: [{nif}] no ha sido encontrado. Por favor, inténtelo de nuevo.")
        elif opcion_elegida == "3": # (3) Actualizar datos de un alumno por NIF
            nif = input("Introduce el nif del alumno que desea actualizar: ")
            output = actualizar_datos(nif)
            if not output:
                print(f"El alumno con nif: [{nif}] no ha sido encontrado. Por favor, inténtelo de nuevo.")
        elif opcion_elegida == "4": # (4) Mostrar datos de un alumno por NIF
            nif = input("Introduce el nif del alumno que quieres visualizar: ")
            output = mostrar_alumno_por_nif(nif)
            if not output:
                print(f"El alumno con nif: [{nif}] no ha sido encontrado. Por favor, inténtelo de nuevo.")
        elif opcion_elegida == "5": # (5) Mostrar datos de un alumno por Email
            email = input("Introduce el email del alumno que quieres visualizar: ")
            output = mostrar_alumno_por_mail(email)
            if not output:
                print(f"El alumno con nif: [{email}] no ha sido encontrado. Por favor, inténtelo de nuevo.")
        elif opcion_elegida == "6": # (6) Listar TODOS los alumnos
            mostrar_alumnos()
        elif opcion_elegida == "7": # (7) Aprobar Alumno por NIF
            nif = input("Introduce el nif del alumno que quieres aprobar: ")
            output = nota_alumno(nif, True)
            if not output:
                print(f"El alumno con nif: [{nif}] no ha sido encontrado. Por favor, inténtelo de nuevo.")
        elif opcion_elegida == "8": # (8) Suspender Alumno por NIF
            nif = input("Introduce el nif del alumno que quieres suspender: ")
            output = nota_alumno(nif, False)
            if not output:
                print(f"El alumno con nif: [{nif}] no ha sido encontrado. Por favor, inténtelo de nuevo.")
        elif opcion_elegida == "9": # (9) Mostrar alumnos aprobados
            mostrar_alumno_por_nota(True)
        elif opcion_elegida == "10": # (10) Mostrar alumnos suspensos
            mostrar_alumno_por_nota(False)
        else: # Dato introducido no válido
            print("La opción elegida no es válida, por favor, introduce de nuevo otra opción.")
    else: # Vetamos al usuario de que elija una opción distinta a crear un alumno si todavía no existe ninguno
        if opcion_elegida == "X" or opcion_elegida == "x": # (X) Finalizar Programa
            print("Programa finalizado con éxito.")
            menu = False
        elif opcion_elegida == "1": # (1) Añadir un alumno
            print("(1) Añadir un alumno")
            crear_alumno()
        elif opcion_elegida in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]: # (1) Añadir un alumno
            print("Antes de continuar, por favor, introduce algún alumno en la lista.")
        else: # Dato introducido no válido
            print("La opción elegida no es válida, por favor, introduce de nuevo otra opción.")
# --------------------------------------------------------------------