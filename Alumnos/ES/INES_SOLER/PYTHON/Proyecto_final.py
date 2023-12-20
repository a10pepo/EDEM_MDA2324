'''
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
(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X
'''

lista_alumnos = [{"NIF": "12345678A", "Nombre": "Juan", "Apellidos": "García Pérez", "Teléfono": "123-456-789", "Email": "juan@gmail.com", "Aprobado": True},
    {"NIF": "98765432B", "Nombre": "María", "Apellidos": "López Martínez", "Teléfono": "987-654-321", "Email": "maria@hotmail.com", "Aprobado": False},
    {"NIF": "56789012C", "Nombre": "Carlos", "Apellidos": "Fernández González", "Teléfono": "567-890-123", "Email": "carlos@yahoo.com", "Aprobado": True},
    {"NIF": "34567890D", "Nombre": "Laura", "Apellidos": "Rodríguez Sánchez", "Teléfono": "345-678-901", "Email": "laura@gmail.com", "Aprobado": False},
    {"NIF": "78901234E", "Nombre": "Pedro", "Apellidos": "Martín Jiménez", "Teléfono": "789-012-345", "Email": "pedro@hotmail.com", "Aprobado": True}
]


def actualizar2():
    opcion2 = input('''¿Desea actualizar otro campo? (SI/NO)
    ''')
    if (opcion2 == 'SI'):
        opcion
        return True
    else:
        return False

opcion_escogida = ''

print('¿Qué desea hacer?')
while opcion_escogida != 'X':
    opcion_escogida = input('''
    1. Añadir un alumno.
    2. Eliminar alumno por NIF.
    3. Actualizar datos de un alumno por NIF.
    4. Mostrar los datos de un alumno por NIF.
    5. Mostrar los datos de un alumno por Email.
    6. Listar TODOS los alumnos.
    7. Aprobar Alumno por NIF.
    8. Suspender Alumno por NIF.
    9. Mostrar alumnos aprobados.
    10. Mostrar alumnos suspensos.
    X. Finalizar programa.                       
    ''')

    if opcion_escogida == '1':
        Nif_in = input('''Indique el NIF del alumno:
        ''')
        Nombre_in = input('''Indique el nombre del alumno:
        ''')
        Apellidos_in = input('''Indique los apellidos del alumno:
        ''')
        Telefono_in = input('''Indique el número de teléfono del alumno:
        ''')
        Email_in = input('''Indique la dirección de email del alumno:
        ''')
        Aprobado_in = input('''¿Está aprobado el alumno? (SI/NO)
        ''')
        if Aprobado_in == 'SI':
            Aprobado = True
        else:
            Aprobado = False

        Alumno = {
            "NIF": str(Nif_in),
            "Nombre": str(Nombre_in),
            "Apellidos": str(Apellidos_in),
            "Telefono": str(Telefono_in),
            "Email": str(Email_in),
            "Aprobado": bool(Aprobado)
        }
        lista_alumnos.append(Alumno)

        print(lista_alumnos)
    
    elif opcion_escogida == '2':
        Nif_eliminar = input('''Indique el NIF del alumno que desea eliminar:
        ''')
        for alumno in lista_alumnos:
            if Nif_eliminar.lower() == alumno["NIF"].lower():
                lista_alumnos.remove(alumno)
                break
    
    elif opcion_escogida == '3':
        Nif_alumno = input('''Indique el NIF del alumno que desea actualizar:
        ''')
        for alumno in lista_alumnos:
            if Nif_alumno.lower() == alumno["NIF"].lower():
                while True:
                    print('¿Qué campo desea actualizar?')
                    opcion = input('''
                    1. NIF
                    2. Nombre
                    3. Apellidos
                    4. Telefono
                    5. Email
                    6. Aprobado
                    ''')
                    if opcion == '1':
                        Nif_actualizar = input('''Indique el nuevo NIF:
                        ''')
                        alumno["NIF"] = Nif_actualizar
                        
                    elif opcion == '2':
                        Nombre_actualizar = input('''Indique el nuevo nombre:
                        ''')
                        alumno["Nombre"] = Nombre_actualizar
                
                    elif opcion == '3':
                        Apellidos_actualizar = input('''Indique los nuevos apellidos:
                        ''')
                        alumno["Apellidos"] = Apellidos_actualizar
                
                    elif opcion == '4':
                        Telefono_actualizar = input('''Indique el nuevo teléfono:
                        ''')
                        alumno["Teléfono"] = Telefono_actualizar
                
                    elif opcion == '5':
                        Email_actualizar = input('''Indique el nuevo email:
                        ''')
                        alumno["Email"] = Email_actualizar
                
                    elif opcion == '6':
                        Aprobado_actualizar = input('''Indique si el alumno está aprobado o no (SI/NO):
                    ''')
                        if Aprobado_actualizar == 'SI':
                            alumno["Aprobado"] = True
                        else:
                            alumno["Aprobado"] = False
                    
                    if not actualizar2():
                        break 
    
    elif opcion_escogida == '4':
        Nif_mostrar = input('''Indique el NIF del alumno que quiere consultar:
        ''')
        for alumno in lista_alumnos:
            if Nif_mostrar == alumno["NIF"]:
                print(f'''Los datos del alumno con NIF {alumno["NIF"]} son:
                Nombre: {alumno["Nombre"]}
                Apellidos: {alumno["Apellidos"]}
                Teléfono: {alumno["Teléfono"]}
                Email: {alumno["Email"]}
                Aprobado: {alumno["Aprobado"]}
                ''')
    
    elif opcion_escogida == '5':
        Email_mostrar = input('''Indique el email del alumno que quiere consultar:
        ''')
        for alumno in lista_alumnos:
            if Email_mostrar == alumno["Email"]:
                print(f'''Los datos del alumno con Email {alumno["Email"]} son:
                NIF: {alumno["NIF"]}
                Nombre: {alumno["Nombre"]}
                Apellidos: {alumno["Apellidos"]}
                Teléfono: {alumno["Teléfono"]}
                Aprobado: {alumno["Aprobado"]}
                ''')

    elif opcion_escogida == '6':
        print('LISTADO DE TODOS LOS ALUMNOS:')
        for i, alumno in enumerate(lista_alumnos, start=1):
            print(f'''El alumno {i} es {alumno["Nombre"]} {alumno["Apellidos"]} y sus datos son:
            NIF: {alumno["NIF"]}
            Teléfono: {alumno["Teléfono"]}
            Email: {alumno["Email"]}
            Aprobado: {alumno["Aprobado"]}
            ''')

    elif opcion_escogida == '7':
        nif_aprobar = input('''Indique el NIF del alumno al que quiere aprobar:
        ''')
        for alumno in lista_alumnos:
            if nif_aprobar == alumno["NIF"]:
                alumno["Aprobado"] = True
    
    elif opcion_escogida == '8':
        nif_suspender = input('''Indique el NIF del alumno al que quiere suspender:
        ''')
        for alumno in lista_alumnos:
            if nif_suspender == alumno["NIF"]:
                alumno["Aprobado"] = False
    
    elif opcion_escogida == '9':
        print('LISTA ALUMNOS APROBADOS: ')
        contador_aprobados = 0
        for alumno in lista_alumnos:
            if alumno["Aprobado"] == True:
                contador_aprobados += 1
                print(f'{contador_aprobados}. {alumno["Nombre"]} {alumno["Apellidos"]}')

    elif opcion_escogida == '10':
        print('LISTA ALUMNOS SUSPENDIDOS: ')
        contador_suspendidos = 0
        for alumno in lista_alumnos:
            if alumno["Aprobado"] == False:
                contador_suspendidos += 1
                print(f'{contador_suspendidos}. {alumno["Nombre"]} {alumno["Apellidos"]}')

    elif opcion_escogida == 'X':
        exit()

