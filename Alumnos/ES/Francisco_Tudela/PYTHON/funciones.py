import json


def cargar_alumnos():
    try:
        with open('alumnos.json', 'r') as file:
            alumnos = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        alumnos = {}
    return alumnos


def guardar_alumnos(alumnos):
    with open('alumnos.json', 'w') as file:
        json.dump(alumnos, file, indent=2)


def add_alumni(alumnos):
    NIF = input('Indique el NIF del alumno con la letra al final:').upper()
    if not any(alumno['NIF'] == NIF for alumno in alumnos):
        nif = NIF
        nombre = str(input('Indica el nombre del Alumno:'))
        apellidos = str(input('Indica el apellido del Alumno:'))
        teléfono = int(input('Indica el teléfono del Alumno:'))
        email = str(input('Indica el email del Alumno:'))
        aprobado = bool(input('Indica si el Alumno esta aprobado o suspendido:'))
        
        alumno = {
            'NIF': NIF,
            'Nombre': nombre,
            'Apellidos': apellidos,
            'Telefono': teléfono,
            'Email': email,
            'Aprobado': aprobado
        }
        alumnos.append(alumno)
        print(f'Alumno con NIF {NIF} agregado correctamente.')
        print(alumnos)
    else:
        print('Este alumno ya se encuentra en la base de datos')


def remove_alumni(alumnos):
    NIF = input('Indique el NIF del alumno con la letra al final:').upper()
    for alumno in alumnos:
        if alumno['NIF'] == NIF:
            alumnos.remove(alumno)
            break
    return alumnos   


def actualizar_data(alumnos):
    NIF = input('Indique el NIF del alumno con la letra al final:').upper()
    alumno_encontrado = None
    for alumno in alumnos:
        if alumno.get('NIF', '') == NIF:
            alumno_encontrado = alumno
            break
    if alumno_encontrado:
        mod_nombre = input('Se modifica el nombre Y / N')
        if mod_nombre.upper() == 'Y':
            alumno_encontrado['Nombre'] = input('Indica el nombre del Alumno:')

        mod_apellido = input('Se modifica el apellido Y / N')
        if mod_apellido.upper() == 'Y':
            alumno_encontrado['Apellidos'] = input('Indica el apellido del Alumno:')

        mod_telefono = input('Se modifica el telefono Y / N')
        if mod_telefono.upper() == 'Y':
            alumno_encontrado['Telefono'] = input('Indica el teléfono del Alumno:')

        mod_email = input('Se modifica el mail Y / N')
        if mod_email.upper() == 'Y':
            alumno_encontrado['Email'] = input('Indica el email del Alumno:')

        mod_nota = input('Se modifica la nota Y / N')
        if mod_nota.upper() == 'Y':
            alumno_encontrado['Aprobado'] = bool(input('Indica si el Alumno esta aprobado o suspendido:'))

        print('Datos del alumno actualizados correctamente.')
    else:
        print(f'No se encontró ningún alumno con NIF {NIF}. No se pueden actualizar los datos.')


def mostrar_data_alumni(alumnos):
    NIF = input('Indique el NIF del alumno con la letra al final:').upper()
    alumno_encontrado = None
    for alumno in alumnos:
        if alumno.get('NIF', '')== NIF:
            alumno_encontrado = alumno
            break
    if alumno_encontrado:
        print(f"El alumno seleccionado es el que posee este NIF: {NIF}")
        print(f"El nombre del alumno seleccionado es: {alumno_encontrado.get('Nombre', '')}")
        print(f"Los apellidos del alumno seleccionado son: {alumno_encontrado.get('Apellidos', '')}")
        print(f"El telefono del alumno seleccionado es: {alumno_encontrado.get('Telefono', '')}")
        print(f"El email del alumno seleccionado es: {alumno_encontrado.get('Email', '')}")
        print(f"¿El alumno esta aprobado?: {alumno_encontrado.get('Aprobado', '')}")
    else:
        print(f"No se encontró ningún alumno con NIF {NIF}.") 

def mostrar_datos_por_mail(alumnos):
    mail = input('Indique el email del alumno:')
    alumno_encontrado = None
    for alumno in alumnos:
        if alumno.get('Email','')== mail:
           alumno_encontrado = alumno
           break
    if alumno_encontrado:
        print(f"El alumno seleccionado es el que posee este NIF: {mail}")
        print(f"El nombre del alumno seleccionado es: {alumno_encontrado.get('Nombre', '')}")
        print(f"Los apellidos del alumno seleccionado son: {alumno_encontrado.get('Apellidos', '')}")
        print(f"El telefono del alumno seleccionado es: {alumno_encontrado.get('Telefono', '')}")
        print(f"El email del alumno seleccionado es: {alumno_encontrado.get('Email', '')}")
        print(f"¿El alumno esta aprobado?: {alumno_encontrado.get('Aprobado', '')}")
    else:
        print(f"No se encontró ningún alumno con NIF {mail}.")   


def mostrar_total_alumnos(alumnos):
   for i, alumno in enumerate(alumnos, start = 1):
        nombre = alumno.get('Nombre', '')
        apellidos = alumno.get('Apellidos', '')
        print(f'Alumno {i}: Nombre = {nombre}, Apellido = {apellidos}')

def aprobar_alumno(alumnos):
    NIF = input('Indique el NIF del alumno con la letra al final:').upper()
    alumno_encontrado = None 
    for alumno in alumnos:
        if alumno.get('NIF', '')== NIF:
            alumno_encontrado = alumno
            break
    if alumno_encontrado:
        if alumno_encontrado['Aprobado']:
            print('El alumno ya estaba aprobado')
        else:
            ap = str(input(f'¿Quieres aprobar al alumno con el siguiente NIF (YES/NO): {alumno_encontrado["NIF"]}')).upper()
        if ap == 'YES':
            alumno_encontrado['Aprobado'] = True
            print('El alumno ha sido aprobado con exito')
            print(f"¿El alumno esta aprobado?: {alumno_encontrado['Aprobado']}")
        else:
            print('El alumno no ha sido aprobado')

def suspender_alumno(alumnos):
    NIF = input('Indique el NIF del alumno con la letra al final:').upper()
    alumno_encontrado = None
    for alumno in alumnos:
        if alumno.get('NIF', '')==NIF:
            alumno_encontrado = alumno
            break
    if alumno_encontrado:
        if alumno_encontrado['Aprobado']==False:
            print('El alumno ya estaba suspendido')
        else:
            ap = str(input(f'¿Quieres suspender al alumno con el siguiente NIF (YES/NO): {alumno_encontrado["NIF"]}')).upper()
        if ap == 'YES':
            alumno_encontrado['Aprobado'] = False
            print('El alumno ha sido suspendido con exito')
            print(f"¿El alumno esta aprobado?: {alumno_encontrado['Aprobado']}")
        else:
            print('El alumno no ha sido suspendido')

def mostrar_alumnos_aprobados(alumnos):
    print('Alumnos Aprobados:')
    for i, alumno in enumerate(alumnos, start = 1):
        nombre = alumno.get('Nombre', '')
        aprobado = alumno.get('Aprobado', '')
        if aprobado:
            print(f'Alumno {i}: Nombre = {nombre}, Aprobado = {aprobado}')
    

def mostrar_alumnos_suspendidos(alumnos):
    print('Alumnos Suspendidos:')
    for i, alumno in enumerate(alumnos, start = 1):
        nombre = alumno.get('Nombre', '')
        aprobado = alumno.get('Aprobado', '')
        if not aprobado:
            print(f'Alumno {i}: Nombre = {nombre}, Aprobado = {aprobado}')
