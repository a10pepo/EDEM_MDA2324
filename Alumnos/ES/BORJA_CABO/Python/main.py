"""
Una empresa de formación quiere gestionar su cartera de alumnos.

Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

NIF (string)
Nombre (string)
Apellidos (string)
Teléfono (string)
Email (string)
Aprobado (boolean)
El programa debe mostrar las siguientes opciones por consola para que escoja el usuario:

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
"""

lista_alumnos = {
    '20304050A': {
        'NIF' : '20304050A',
        'Nombre' : 'Borja',
        'Apellidos' : 'Cabo Huélamo',
        'Telefono' : 657657657,
        'Email' : 'bc@gmail.com',
        'Aprobado' : True
    },
    '10203040B' :{
        'NIF' : '10203040B',
        'Nombre' : 'Pablo',
        'Apellidos' : 'Tapia Tapia',
        'Telefono' : 654654654,
        'Email' : 'pt@gmail.com',
        'Aprobado' : False        
    }
}


        
def añadir_alumno():
    NIF = (input('Introduce el NIF del alumno: '))
    print(f'El NIF del alumno es: {NIF}')

    nombre = str(input('Introduce el nombre del alumno: '))
    while any(opcion.isdigit() for opcion in nombre):
        print('El nombre que has introducido no es valido, por favor no introduzcas ningún valor númerico')
        nombre = str(input('Introduce el nombre del alumno: '))
    print(f'El nombre del alumno es {nombre}')

    apellidos = str(input('Introduce los apellidos del alumno: '))
    while any(opcion.isdigit() for opcion in apellidos):
        print('Los apellidos que has introducido no son validos, por favor no introduzcas ningún valor númerico')
        apellidos = str(input('Introduce el nombre del alumno: '))
    print(f'Los apellidos de los alumnos son: {apellidos}')

    while True:
        try:
            telefono = int(input('Introduce el teléfono del alumno: '))
            break
        except ValueError:
            print('El teléfono que has introducido no es válido, por favor introduce un valor númerico entero') 
    print(f'El teléfono del alumno es: {telefono}')

    email = str(input('Introduce el email del alumno: '))
    print(f'El email del alumno es: {email}')

    
    aprobado = bool(input('Introduce si ha aprobado el alumno o no, (true/false): '))


    lista_alumnos[NIF] = {
        'NIF' : NIF,
        'Nombre' : nombre,
        'Apellidos' : apellidos,
        'Telefono' : telefono,
        'Email' : email,
        'Aprobado' : aprobado
    }

def eliminar_alumno(valor):
    NIF = str(valor)
    alumno_eliminado = lista_alumnos.pop(NIF)
    print('Alumno eliminado con exito')
    return alumno_eliminado

def actualizar_alumno(valor):
    nif_a_actualizar = valor
    if nif_a_actualizar in lista_alumnos:
        NIF = (input('Introduce el NIF del alumno: '))
        print(f'El NIF del alumno es: {NIF}')

        nombre = str(input('Introduce el nombre del alumno: '))
        while any(opcion.isdigit() for opcion in nombre):
            print('El nombre que has introducido no es valido, por favor no introduzcas ningún valor númerico')
            nombre = str(input('Introduce el nombre del alumno: '))
        print(f'El nombre del alumno es {nombre}')

        apellidos = str(input('Introduce los apellidos del alumno: '))
        while any(opcion.isdigit() for opcion in apellidos):
            print('Los apellidos que has introducido no son validos, por favor no introduzcas ningún valor númerico')
            apellidos = str(input('Introduce el nombre del alumno: '))
        print(f'Los apellidos de los alumnos son: {apellidos}')

        while True:
            try:
                telefono = int(input('Introduce el teléfono del alumno: '))
                break
            except ValueError:
                print('El teléfono que has introducido no es válido, por favor introduce un valor númerico entero') 
        print(f'El teléfono del alumno es: {telefono}')

        email = str(input('Introduce el email del alumno: '))
        print(f'El email del alumno es: {email}')

        aprobado = bool(input('Introduce si ha aprobado el alumno o no, (true/false): '))

        alumno_actualizado = {
            'NIF': NIF,
            'Nombre': nombre,
            'Apellidos': apellidos,
            'Telefono': telefono,
            'Email': email,
            'Aprobado': aprobado
        } 
        lista_alumnos[NIF] = alumno_actualizado
        print('Alumno actalizado correctamente')
    else:
        print('El NIF no es valido. ')

def mostrar_alumno_nif(valor):
  NIF = str(valor)
  print(f"El alumno seleccionado es el que posee este NIF: {NIF}")
  print(f"El nombre y apellidos del alumno seleccionado es: {lista_alumnos[NIF]['Nombre']} {lista_alumnos[NIF]['Apellidos']}")
  print(f"El telefono del alumno seleccionado es: {lista_alumnos[NIF]['Telefono']}")
  print(f"El email del alumno seleccionado es: {lista_alumnos[NIF]['Email']}")
  print(f"¿El alumno esta aprobado?: {lista_alumnos[NIF]['Aprobado']}")


def mostrar_alumno_email(valor):
  email = str(valor)
  for alumno in lista_alumnos.values():
    if alumno['Email'] == email:
      print(f"El alumno seleccionado es el que posee este NIF: {alumno['NIF']}")
      print(f"El nombre del alumno seleccionado es: {alumno['Nombre']}")
      print(f"Los apellidos del alumno seleccionado son: {alumno['Apellidos']}")
      print(f"El telefono del alumno seleccionado es: {alumno['Telefono']}")
      print(f"El email del alumno seleccionado es: {email}")
      print(f"¿El alumno esta aprobado?: {alumno['Aprobado']}")
      break

def mostrar_alumnos():
    for NIF, datos in lista_alumnos.items():
        for clave, valor in datos.items():
            print(f'{clave} : {valor}')
        print('--------------------')

def aprobar_alumno(valor):
    NIF = str(valor)
    if lista_alumnos[NIF]['Aprobado'] == True:
        print('El alumno ya está aprobado')
    else:
        respuesta = input(f'¿Quieres aprobar al alumno con NIF: {lista_alumnos[NIF]["NIF"]}? (Si/No): ').lower()
        if respuesta == 'si':
            lista_alumnos[NIF]['Aprobado'] = True
            print('El alumno ha sido aprobado')
        else:
            print('El alumno no ha sido aprobado')

def suspender_alumno(valor):
    NIF = str(valor)
    if lista_alumnos[NIF]['Aprobado'] == False:
        print('El alumno ya está suspendido')
    else:
        respuesta = input(f'¿Quieres suspender al alumno con NIF: {lista_alumnos[NIF]["NIF"]}? (Si/No): ').lower()
        if respuesta == 'si':
            lista_alumnos[NIF]['Aprobado'] = False
            print('El alumno ha sido suspendido')
        else:
            print('El alumno no ha sido suspendido')

def mostrar_aprobados():
    for NIF, datos in lista_alumnos.items():
        for clave, valor in datos.items():
            if lista_alumnos[NIF]['Aprobado'] == True:
                print(f'{clave} : {valor}')
        print('--------------------')

def mostrar_suspendidos():
    for NIF, datos in lista_alumnos.items():
        for clave, valor in datos.items():
            if lista_alumnos[NIF]['Aprobado'] == False:
                print(f'{clave} : {valor}')
        print('--------------------')




opcion_escogida = ''
while(opcion_escogida != 'X'):
    opcion_escogida = input('''Escoge una opción: 
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
(X) Salir del programa
''').upper()
    if opcion_escogida == '1':
        añadir_alumno()
    elif opcion_escogida == '2':
        valor = str(input('Selecciona el NIF del alumno que quieres eliminar: '))
        eliminar_alumno(valor)
    elif opcion_escogida == '3':
        valor = str(input('Selecciona el NIF del alumno que quieres actualizar: '))
        actualizar_alumno(valor)
    elif opcion_escogida == '4':
        valor = str(input('Selecciona el NIF del alumno que quieres mostrar: '))
        mostrar_alumno_nif(valor)
    elif opcion_escogida == '5':
       valor = str(input('Selecciona el email del alumno que quieres mostrar: '))
       mostrar_alumno_email(valor)
    elif opcion_escogida == '6':
        mostrar_alumnos()
    elif opcion_escogida == '7':
       valor = str(input('Selecciona el NIF del alumno que quieres aprobar: '))
       aprobar_alumno(valor)
    elif opcion_escogida == '8':
       valor = str(input('Selecciona el NIF del alumno que quieres suspender: '))
       suspender_alumno(valor)
    elif opcion_escogida == '9':
        mostrar_aprobados()
    elif opcion_escogida == '10':
        mostrar_suspendidos()
    elif opcion_escogida != 'X':
        print('Opción no valida, por favor escoge una de las opciones de arriba. ')

