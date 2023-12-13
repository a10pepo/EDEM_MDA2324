#Entregable FINAL Python

#Definición de la clase de alumnos:
class Alumno():
    def __init__(self, dni, nombre, apellidos, telefono, mail, aprobado):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.mail = mail
        self.aprobado = aprobado

    def info_alumno(self):
        return(f" -Nombre: {self.nombre} {self.apellidos}\n -DNI: {self.dni}\n -Teléfono: {self.telefono}\n -Mail: {self.mail}\n -Aprobado: {self.aprobado}")

lista_alumnos = []

print("Bienvenido al Programa Alumno300, ¡dónde podrá gestionar todos sus alumnos de una manera fácil!")

#Definimos la applicación en un bucle While, que funciona y guarda los datos siempre que se está en la aplicación "corriendo"

salir_app = False
while not salir_app:
    print("Por favor elija qué quiere hacer:")
    eleccion = input("(1) Añadir un nuevo alumno\n"
                     "(2) Eliminar un alumno\n"
                     "(3) Actualizar un dato de un alumno\n"
                     "(4) Mostrar alumno por DNI/NIF\n"
                     "(5) Mostrar alumno por mail\n"
                     "(6) Mostrar todos los alumnos del Instituto\n"
                     "(7) Aprobar a un alumno\n"
                     "(8) Suspender a un alumno\n"
                     "(9) Mostrar todos los alumnos aprobados\n"
                     "(10) Mostrar todos los alumnos suspensos\n"
                     "(X) Finalizar Programa\n")

    if eleccion == "1":
        print("Introduzca los siguientes datos del Alumno a añadir")
        dni = input("Indique el DNI/NIF del Alumno ")
        nombre = input("Indique el Nombre del Alumno ")
        apellidos = input("Inique los Apellidos del Alumno ")
        telefono = input("Indique el Número de Teléfono del Alumno ")
        mail = input("Indique el Correo electrónico del Alumno ")
        aprobado = input("¿El Alumno está aprobado? [y/n] ")

        if aprobado.lower() == "y":
            aprobado = True
        else:
            aprobado = False
        
        lista_alumnos.append(Alumno(dni, nombre, apellidos, telefono, mail, aprobado))
        print("Alumno añadido con éxito.")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")

        
    elif eleccion == "2":
        dni = input("Indique el DNI/NIF del alumno a eliminar\n")
        for alumno in lista_alumnos:
            if alumno.dni == dni:
                lista_alumnos.remove(alumno)
                print("Alumno eliminado con éxito.")
                break
        else:
            print("No se encontró ningún alumno con ese DNI/NIF.")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion == "3":
        dni_cambio = input("Quiere modificar los datos de un Alumno de la Aplicación, por favor inique el DNI/NIF\n")
        opcion_cambio = input("¿Qué campo desea modificar?\n"
                              "[1] DNI\n"
                              "[2] Nombre\n"
                              "[3] Apellidos\n"
                              "[4] Telefono\n"
                              "[5] Mail\n")
        if opcion_cambio == "1":
            for alumno in lista_alumnos:
                if alumno.dni == dni_cambio:
                    nuevo_dni = (input("Inique por favor el nuevo DNI del Alumno: "))
                    alumno.dni == nuevo_dni     
        elif opcion_cambio == "2":
            for alumno in lista_alumnos:
                if alumno.dni == dni_cambio:
                    nuevo_nombre = (input("Indique por favor el nuevo Nombre del Alumno: "))
                    alumno.nombre = nuevo_nombre
        elif opcion_cambio == "3":
            for alumno in lista_alumnos:
                if alumno.dni == dni_cambio:
                    nuevo_Apellidos = (input("Indique por favor los nuevos Apellidos del Alumno: "))
                    alumno.apellidos = nuevo_Apellidos
        elif opcion_cambio == "4":
            for alumno in lista_alumnos:
                if alumno.dni == dni_cambio:
                    nuevo_telefono = (input("Indique por favor el nuevo Teléfono del Alumno: "))
                    alumno.telefono = nuevo_telefono
        elif opcion_cambio == "5":
            for alumno in lista_alumnos:
                if alumno.dni == dni_cambio:
                    nuevo_mail = (input("Indique por favor el nuevo Mail del Alumno: "))
                    alumno.mail = nuevo_mail
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion == "4":
        nif_alumno = input("Quiere visualizar a un Alumno concreto"
                           "Indique el DNI/NIF del Alumno: ")
        for alumno in lista_alumnos:
            if alumno.dni == nif_alumno:
                print(f"-Nombre: {alumno.nombre} {alumno.apellidos}\n -DNI: {alumno.dni}\n -Mail: {alumno.mail}\n -Telefono: {alumno.telefono}\n -Aprobado: {alumno.aprobado}")
            else:
                print("Ese DNI no corresponde a ningún Alumno en nuestra aplicación")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion == "5":
        mail_alumno = input("Quiere visualizar a un Alumno concreto"
                           "Indique el MAIL del Alumno: ")
        for alumno in lista_alumnos:
            if alumno.mail == mail_alumno:
                print(f"-Nombre: {alumno.nombre} {alumno.apellidos}\n -DNI: {alumno.dni}\n -Mail: {alumno.mail}\n -Telefono: {alumno.telefono}\n -Aprobado: {alumno.aprobado}")
            else:
                print("Ese MAIL no corresponde a ningún Alumno en nuestra aplicación")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion == "6":
        for alumno in lista_alumnos:
            print(f"Alumno:\n -Nombre: {alumno.nombre} {alumno.apellidos}\n -DNI: {alumno.dni}\n -Mail: {alumno.mail}\n -Telefono: {alumno.telefono}\n -Aprobado: {alumno.aprobado}")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion == "7":
        print("Quieres Aprobar a un Alumno")
        dni_aprobado = (input("Indica el DNI/NIF del Alumno que quieres Aprobar\n"))
        for alumno in lista_alumnos:
            if alumno.dni == dni_aprobado:
                alumno.aprobado = True
            else:
                print("Ese DNI/NIF no coincide con ningun alumno")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion == "8":
        print("Quieres Suspender a un Alumno")
        dni_suspendido = (input("Indica el DNI/NIF del Alumno que quieres Suspender\n"))
        for alumno in lista_alumnos:
            if alumno.dni == dni_suspendido:
                alumno.aprobado = False
            else:
                print("Ese DNI/NIF no coincide con ningun alumno")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion == "9":
        print("Quieres visualizar todos los Alumnos Aprobados")
        for alumno in lista_alumnos:
            if alumno.aprobado == True:
                print(f"Los Alumnos Aprobados son:\n -Nombre: {alumno.nombre} {alumno.apellidos}\n -DNI: {alumno.dni}\n -Mail: {alumno.mail}\n -Telefono: {alumno.telefono}\n")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion == "10":
        print("Quieres visualizar todos los Alumnos Suspendidos")
        for alumno in lista_alumnos:
            if alumno.aprobado == False:
                print(f"Los Alumnos Suspendidos son:\n -Nombre: {alumno.nombre} {alumno.apellidos}\n -DNI: {alumno.dni}\n -Mail: {alumno.mail}\n -Telefono: {alumno.telefono}\n")
        print("------------------------------------------------------------------------------------------------\n"
              "¿Que desea hacer ahora?\n"
              "------------------------------------------------------------------------------------------------\n")
        
    elif eleccion.lower() == "x":
        salir_app = True
        print("Saliendo del programa...")
    else:
        print("Por favor, elija una opción válida.")


