import json

alumnos  = {}

##FUNCIONES

def cargar_alumnos():
    try:
        with open('alumnos.json', 'r') as file:
            global alumnos
            alumnos = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        alumnos = {}

def guardar_alumnos():
    with open('alumnos.json', 'w') as file:
        json.dump(alumnos, file, indent=2)

def agregar_alumnos():
    nif = str(input('Inserte el NIF del alumno: '))
    nombre = str(input('Inserte el nombre del alumno: '))
    apellidos = str(input('Inserte los apellidos del alumno: '))
    telefono = str(input('Inserte el teléfono del alumno: '))
    mail = str(input('Inserte el email del alumno: '))
    aprobado = input('Inserte si el alumno ha aprobado (True/False): ').lower() == 'true'
    
    alumnos[nif] = {
        'NIF': nif,
        'Nombre': nombre,
        'Apellidos': apellidos,
        'Telefono': telefono,
        'Email': mail,
        'Aprobado': aprobado
    }

def eliminar_alumnos():
    nif = str(input('Ingrese NIF del alumno que desea eliminar: '))
    if nif in alumnos:
        del alumnos[nif]
        print('Alumno eliminado correctamente.')
    else:
        print('Alumno no encontrado.')
        
def actualizar_alumnos():
    nif = str(input('Ingrese NIF del alumno que desea actualizar: '))
    if nif in alumnos:
        print(f'Actualice los datos del alumno c{nif}')
        alumnos[nif]['Nombre'] = str(input('Inserte el nombre del alumno: '))
        alumnos[nif]['Apellidos'] = str(input('Inserte los apellidos del alumno: '))
        alumnos[nif]['Telefono'] = str(input('Inserte el teléfono del alumno: '))
        alumnos[nif]['Email'] = str(input('Inserte el email del alumno: '))
        alumnos[nif]['Aprobado'] = bool(input('Inserte si el alumno ha aprobado: '))
        print('Alumno actualizado correctamente.')
    else:
        print('Alumno no encontrado.')
        
def mostrar_alumnos_nif():
    nif = str(input('Ingrese NIF del alumno que desea mostrar: '))
    if nif in alumnos:
        print(f'''Los datos del alumno {nif} son:
              Nombre: {alumnos[nif]['Nombre']}
              Apellidos: {alumnos[nif]['Apellidos']}
              Teléfono: {alumnos[nif]['Telefono']}
              Email: {alumnos[nif]['Email']}
              Aprobado: {alumnos[nif]['Aprobado']}''')
    else:
        print('Alumno no encontrado')

def mostrar_alumnos_mail():
    mail = str(input('Ingrese el mail del alumno que desea mostrar: '))
    for alumno in alumnos.values():
        if alumno['Email'] == mail:
            print(f'''Los datos del alumno {mail} son:
                  Nombre: {alumno['Nombre']}
                  Apellidos: {alumno['Apellidos']}
                  Teléfono: {alumno['Telefono']}
                  NIF: {alumno['NIF']}
                  Aprobado: {alumno['Aprobado']}''')
            break
                
def listar_alumnos():
    print("Listado de todos los alumnos:")
    for alumno in alumnos.values():
        for key, value in alumno.items():
            print(f"{key}: {value}")
        print("-----------------------")
        
def aprobar_alumno():
    nif = str(input('Ingrese NIF del alumno que desea aprobar: '))
    if nif in alumnos:
        alumnos[nif]['Aprobado'] = True
        print('Alumno aprobado')
    else:
        print('Alumno no encontrado')

def suspender_alumno():
    nif = str(input('Ingrese NIF del alumno que desea suspender: '))
    if nif in alumnos:
        alumnos[nif]['Aprobado'] = False
        print('Alumno suspendido')
    else:
        print('Alumno no encontrado')
        
def listar_alumnos_aprobados():
    print("Listado de todos los alumnos aprobados:")
    for alumno in alumnos.values():
        if alumno['Aprobado'] == True:
            for key, value in alumno.items():
                print(f"{key}: {value}")
            print("-----------------------")
            
def listar_alumnos_suspendidos():
    print("Listado de todos los alumnos suspendidos:")
    for alumno in alumnos.values():
        if alumno['Aprobado'] == False:
            for key, value in alumno.items():
                print(f"{key}: {value}")
            print("-----------------------")
            
   
##PROGRAMA         
cargar_alumnos()            
while True:
    print('''EMPRESA FORMACIÓN S.A 
    -------------------------- 
    1. Añadir un alumno 
    2. Eliminar alumno por NIF 
    3. Actualizar datos de un alumno por NIF 
    4. Mostrar datos de un alumno por NIF 
    5. Mostrar datos de un alumno por Email 
    6. Listar TODOS os alumnos 
    7. Aprobar Alumno por NIF 
    8. Suspender Alumno por NIF 
    9. Mostrar alumnos aprobados 
    10. Mostrar alumnos suspensos 
    X. Finalizar Programa''')
    tecla = input('Introduce la opción deseada: ')
    
    if tecla == '1':
        agregar_alumnos()
    elif tecla == '2':
        eliminar_alumnos()
    elif tecla == '3':
        actualizar_alumnos()
    elif tecla == '4':
        mostrar_alumnos_nif()
    elif tecla == '5':
        mostrar_alumnos_mail()
    elif tecla == '6':
        listar_alumnos()
    elif tecla == '7':
        aprobar_alumno()
    elif tecla == '8':
        suspender_alumno()
    elif tecla == '9':
        listar_alumnos_aprobados()
    elif tecla == '10':
        listar_alumnos_suspendidos()
    elif tecla.upper() == 'X':
        guardar_alumnos()
        break
    else:
        print('Introduzca una opción correcta')