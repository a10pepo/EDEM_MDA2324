lista_alumnos = [{"NIF": "76895432X", "nombre": "Sole", "apellidos": "Pérez Soler", "teléfono": "667123456", "email": "soleps@gmail.com", "aprobado": True},
    {"NIF": "43215432T", "nombre": "Lucas", "apellidos": "Francis Díaz", "teléfono": "678234123", "email": "lucasfd@gmail.com", "aprobado": False},
    {"NIF": "98712345S", "nombre": "Lucia", "apellidos": "Catalá Sala", "teléfono": "634589765", "email": "luciacs@gmail.com", "aprobado": True},
]

opcion_escogida = ' '

while(opcion_escogida!='X'):
    opcion_escogida=input('''
    Hola, escoger una opción:
    1. Añadir alumno
    2. Eliminar alumno por NIF
    3. Actualizar datos de un alumno por NIF
    4. Mostrar datos de un alumno por NIF
    5. Mostrar datos de un alumno por Email
    6. Listar TODOS los alumnos
    7. Aprobar Alumno por NIF
    8. Suspender Alumno por NIF 
    9. Mostrar alumnos aprobados     
    10. Mostrar alumnos suspensos        
    X. Finalizar Programa
    ''')

    #añadir un alumno
    if (opcion_escogida == '1'):
         
        nif:str=input('Indica el NIF del alumno: ')
        print(f"El nif del alumno es {nif}")
        
        nombre:str = input('Indica el nombre del alumno: ')
        print(f"El nombre del alumno es: {nombre}")
        
        apellidos:str= input('Indica el apellido del alumno: ')
        print(f"Los apellidos del alumno es {apellidos}")
        
        telefono:str = input('Indica el número de teléfono del alumno: ')
        print(f"El teléfono del alumno es {telefono}")
        
        email:str = input('Indica el email del alumno: ')
        print(f"El email del alumno es {email}")

        aprobado=input('Indica si el alumno está aprobado (En ese caso introduce True) o suspendido (En ese caso introduce False): ')
        if (aprobado == 'True'):
            aprobado_bool = True
        elif(aprobado == 'False'):
            aprobado_bool = False
        else: 
            print('valor incorrecto')

        alumno_nuevo={
        "NIF": nif,
        "nombre": nombre,
        "apellidos":apellidos,  
        "teléfono": telefono,
        "email":email,  
        "aprobado": aprobado_bool
        }

        lista_alumnos.append(alumno_nuevo)
        

    #eliminar un alumno
    elif (opcion_escogida == '2'):

        nif_eliminar:str=input('Indica el NIF del alumno a eliminar: ')

        for alumno in lista_alumnos:
            if (alumno['NIF'] == nif_eliminar):
                 lista_alumnos.remove(alumno)


    #Actualizar datos de un alumno por NIF
    elif(opcion_escogida == '3'):
        nif_actualizar:str=input('Indica el NIF del alumno a actualizar: ') 

        for alumno in lista_alumnos:
            if (alumno['NIF'] == nif_actualizar):
                print(alumno)

                nombre_act: str= input('¿Quieres actualizar el nombre del alumno? (Si/No) ')
                if (nombre_act == 'Si'):
                    alumno['nombre'] = input('Introduce el nombre del alumno: ')

                apellidos_act: str= input('¿Quieres actualizar los apellidos del alumno? (Si/No) ')
                if (apellidos_act == 'Si'):
                    alumno['apellidos'] = input('Introduce los apellidos del alumno: ')

                telefono_act: str= input('¿Quieres actualizar el número de teléfono del alumno? (Si/No) ')
                if (telefono_act == 'Si'):
                    alumno['teléfono'] = input('Introduce el número de teléfono del alumno: ')
                
                email_act: str= input('¿Quieres actualizar el email del alumno? (Si/No) ')
                if (email_act == 'Si'):
                    alumno['email'] = input('Introduce el email del alumno: ')
                
                aprobado_act: str= input('¿Quieres actualizar el estado de aprobado o suspendido del alumno? (Si/No) ')
                if (aprobado_act == 'Si'):
                    vble_aprobado= input('Introduce estado de aprobado o suspendido del alumno: ')
                    if (vble_aprobado== 'True'):
                        alumno['aprobado'] = True
                    elif(vble_aprobado== 'False'):
                         alumno['aprobado'] = False


    #Mostrar datos de un alumno por NIF
    elif(opcion_escogida == '4'):
        nif_listar:str=input('Indica el NIF del alumno a consultar: ') 

        for alumno in lista_alumnos:
            if (alumno['NIF'] == nif_listar):
                print(f'''Los datos del alumno son los siguientes:
                    nombre: {alumno["nombre"]}
                    apellidos: {alumno["apellidos"]}
                    teléfono: {alumno["teléfono"]}
                    email: {alumno["email"]}
                    aprobado: {alumno["aprobado"]} ''')
    
    #Mostrar datos de un alumno por Email
    elif(opcion_escogida == '5'):
        email_listar:str=input('Indica el email del alumno a consultar: ') 

        for alumno in lista_alumnos:
            if (alumno['email'] == email_listar):
                print(f'''Los datos del alumno son los siguientes:
                    nombre: {alumno["nombre"]}
                    apellidos: {alumno["apellidos"]}
                    teléfono: {alumno["teléfono"]}
                    email: {alumno["email"]}
                    aprobado: {alumno["aprobado"]} ''')

    # Listar TODOS los alumnos
    elif(opcion_escogida == '6'):
        print(f'Los datos de los alumnos son los siguientes: \n')
        for alumno in lista_alumnos:
            print(alumno)


    #Aprobar Alumno por NIF
    elif(opcion_escogida == '7'):

        aprobar_nif :str=input('Indica el NIF del alumno a aprobar: ')
        for alumno in lista_alumnos:
            if (alumno['NIF'] == aprobar_nif):
                alumno['aprobado']= True

    # Suspender Alumno por NIF
    elif(opcion_escogida == '8'):

        suspender_nif :str=input('Indica el NIF del alumno a suspender: ')
        for alumno in lista_alumnos:
            if (alumno['NIF'] == suspender_nif):
                alumno['aprobado']= False
    
    #Mostrar alumnos aprobados
    elif(opcion_escogida == '9'):
        for alumno in lista_alumnos:
            if (alumno['aprobado'] == True):
                print(alumno)

    #Mostrar alumnos suspendidos
    elif(opcion_escogida == '10'):
        for alumno in lista_alumnos:
            if (alumno['aprobado'] == False):
                print(alumno)