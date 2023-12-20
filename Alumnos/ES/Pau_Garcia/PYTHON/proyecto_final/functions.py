def addStudent(lista_alumno:list):
    nif:str = input('NIF del alumno: ')
    first:str = input('Nombre del alumno: ').capitalize()
    last:str = input('Apellidos del alumno: ').capitalize()
    phone:str = input('Número de teléfono del alumno: ')
    email:str = input('Email del alumno: ').lower()
    while True:
        mark_input = input('Aprobado (A) / Suspendido (B): ')
        if mark_input.lower() == 'aprobado' or mark_input.lower() == 'a':
            mark = True
            break
        elif mark_input.lower() == 'suspendido' or mark_input.lower() == 'b':
            mark = False
            break
        else:
            print("Entrada inválida. Debe ser 'Aprobado' (A) o 'Suspendido' (B). Inténtelo de nuevo.")

    datosAlumno = {"NIF":nif,
     "Nombre":first,
     "Apellidos":last,
     "Teléfono":phone,
     "Email":email,
     "Nota":mark}
    
    lista_alumno.append(datosAlumno)
    return lista_alumno

def findStudent(lista_alumnos:list, nif_num):
    x = None
    i = -1
    for alumno in lista_alumnos:
            i += 1
            if (alumno["NIF"]==nif_num):
                x = alumno
                break
            
    return x,i

def showEmail(lista_alumnos:list):
    email = input('Introduzca el email del alumno: ')
    x = None
    for alumno in lista_alumnos:
            if (alumno["Email"]==email.lower()):
                x = alumno
                for campo in alumno:
                    print(f'{campo}: {alumno[campo]}')
            
    if (x == None):
        print('No se pudo encontrar al alumno. Pruebe de nuevo.')
   
    


def rmStudent(lista_alumnos:list):

    nif_number = input('Indique el NIF del alumno a eliminar: ')
    alumn,i = findStudent(lista_alumnos,nif_number)

    if (alumn==None):
        print('No se han encontrado coincidencias por NIF. Pruebe de nuevo.')
    else:
        lista_alumnos.remove(alumn)
        print(f'Alumno con NIF {nif_number} eliminado correctamente.')
    return lista_alumnos

def updateStudent(lista_alumnos:list):
    nif_number = input('Indique el NIF del alumno para actualizar datos: ')
    alumn,i = findStudent(lista_alumnos,nif_number)
    campos = {
    1: 'Nombre',
    2: 'Apellidos',
    3: 'Teléfono',
    4: 'Email'
    }
    if (alumn==None):
        print('No se han encontrado coincidencias por NIF. Pruebe de nuevo.')
    else:
        choice = int(input('''¿Qué campo quiere actualizar? 
                       Nombre (1)
                       Apellidos (2)
                       Teléfono (3)
                       Email (4)
                       '''))
        if choice in campos:
            campo = campos[choice]
            new_value:str = input(f'Indique el nuevo valor para {campo}: ')
            print(f'Actualizando {campo} con el nuevo valor: {new_value}')
            lista_alumnos[i][f'{campo}']=new_value
        else:
            print('Opción no válida. Por favor, elija un número del 1 al 4.')
    return lista_alumnos
        
def showStudent(lista_alumnos):
    nif_number = input('Indique el NIF del alumno que quiere consultar: ')
    alumn,i = findStudent(lista_alumnos,nif_number)
    for campo in alumn:
        print(f'{campo}: {alumn[campo]}')

def listStudents(lista_alumnos):
    i = 1
    for alumno in lista_alumnos:
        print(f'{i}- {alumno["Nombre"]} {alumno["Apellidos"]}')
        i += 1

def passStudent(lista_alumnos):
    nif_number = input('Indique el NIF del alumno que quiere aprobar: ')
    alumn,i = findStudent(lista_alumnos,nif_number)
    if (alumn == None):
        print(f'No se ha encontrado alumno con NIF {nif_number}')
    else:
        print(f'Alumno con NIF {nif_number}, ha sido aprobado.')
        lista_alumnos[i]["Nota"]=True
    return lista_alumnos

def failStudent(lista_alumnos):
    nif_number = input('Indique el NIF del alumno que quiere suspender: ')
    alumn,i = findStudent(lista_alumnos,nif_number)
    if (alumn == None):
        print(f'No se ha encontrado alumno con NIF {nif_number}')
    else:
        print(f'Alumno con NIF {nif_number}, ha sido suspendido.')
        lista_alumnos[i]["Nota"]=False
    return lista_alumnos


def showPass(lista_alumnos:list):
    print('***** ALUMNOS APROBADOS *****')
    i = 1
    for alumno in lista_alumnos:
        if (alumno["Nota"]==True):
            print(f'{i}- {alumno["Nombre"]} {alumno["Apellidos"]}')
            i += 1

def showFail(lista_alumnos:list):
    print('***** ALUMNOS SUSPENDIDOS *****')
    i = 1
    for alumno in lista_alumnos:
        if (alumno["Nota"]==False):
            print(f'{i}- {alumno["Nombre"]} {alumno["Apellidos"]}')
            i += 1