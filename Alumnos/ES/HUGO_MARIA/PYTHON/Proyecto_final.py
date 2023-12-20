alumnos= [{"NIF":"63141686A","Nombre":"Myrtia","Apellidos":"Wattam","Telefono":"2","Email":"mwattam0@gmail.com","Aprobado":False},
{"NIF":"33884858B","Nombre":"Sarah","Apellidos":"Woodthorpe","Telefono":"3","Email":"swoodthorpe1@gmail.com","Aprobado":False},
{"NIF":"72999272C","Nombre":"Walther","Apellidos":"Lorentz","Telefono": "1","Email":"wlorentz2@gmail.com","Aprobado":True},
{"NIF":"37038610D","Nombre":"Lynn","Apellidos":"Dilland","Telefono":"4","Email":"ldilland3@gmail.com","Aprobado":False},
{"NIF":"11867436E","Nombre":"Jackqueline","Apellidos":"Hammer","Telefono":"5","Email":"jhammer4@gmail.com","Aprobado":True},
{"NIF":"24828223F","Nombre":"Sofie","Apellidos":"Ivanisov","Telefono":"6","Email":"sivanisov5@gmail.com","Aprobado":True},
{"NIF":"70019655G","Nombre":"Saxe","Apellidos":"Wint","Telefono":"7","Email":"swint6@gmail.com","Aprobado":False},]

# 1. Creando Funcion para la creacion de alumnos

def agregar_alumnno():
    nif= str(input('Introduce el NIF del alumno: '))
    nombre= str(input('Introduce el nombre del alumno: '))
    apellido= str(input('Introduce el apellido del alumno: '))
    telefono= str(input('Introduce el telefono del alumno: '))
    email= str(input('Introduce el email del alumno: '))
    aprobado= bool(input('El alumnno ha aprobado? [S/N]').upper() == 'S')
    
    # Agregando el alumno a la lista de alumnos

    alumnos.append(
    {
        "NIF": nif,
        "Nombre": nombre,
        "Apellidos": apellido,
        "Telefono": telefono,
        "Email": email,
        "Aprobado": aprobado
    }
    )

# 2. Creando Funcion para la eliminacion del alumno por NIF

def eliminar_alumno():
    nif= input('Ingrese el NIF del alumno que desea eliminar: ')

    for alumno in alumnos:
        if alumno['NIF'] == nif:
            alumnos.remove(alumno)
            print('El alumno ha sido eliminado correctamente')
            return
        
    print('El alumno no existe')

# 3. Creando Funcion que actualice datos del alumno por NIF

def actualizar_alumno():
    nif= input('Ingrese el NIF del alumno que desea actualizar: ')

    for alumno in alumnos:
        if alumno['NIF'] == nif:
            print('Que dato deseas actualizar?:')
            print('1. NIF')
            print('2. Nombre')
            print('3. Apellidos')
            print('4. Telefono')
            print('5. Email')
            print('6. Aprobado? [S/N]')
            print('7. Actualizar todos los campos')

            opcion= input('Introduce una opcion: ')

            if opcion == '1':
                nuevo_nif = str(input('Introduce el nuevo NIF: '))
                alumno['NIF'] = nuevo_nif
            elif opcion == '2':
                nuevo_nombre= str(input('Introduce el nuevo nombre: '))
                alumno['Nombre']= nuevo_nombre
            elif opcion == '3':
                nuevo_apellido= str(input('Introduce el nuevo apellido'))
                alumno['Apellidos']= nuevo_apellido
            elif opcion == '4':
                nuevo_telefono= str(input('Introduce el nuevo telefono: '))
                alumno['Telefono']= nuevo_telefono
            elif opcion == '5':
                nuevo_email= str(input('Introduce el nuevo email: '))
                alumno['Email']= nuevo_email
            elif opcion == '6':
                nuevo_aprobado= bool(input('El alumnno ha aprobado? [S/N]').upper() == 'S')
                alumno['Aprobado']= nuevo_aprobado
            elif opcion == '7':
                nuevo_nif = str(input('Introduce el nuevo NIF: '))
                alumno['NIF'] = nuevo_nif
                nuevo_nombre= str(input('Introduce el nuevo nombre: '))
                alumno['Nombre']= nuevo_nombre
                nuevo_apellido= str(input('Introduce el nuevo apellido'))
                alumno['Apellidos']= nuevo_apellido
                nuevo_telefono= str(input('Introduce el nuevo telefono: '))
                alumno['Telefono']= nuevo_telefono
                nuevo_email= str(input('Introduce el nuevo email: '))
                alumno['Email']= nuevo_email
                nuevo_aprobado= bool(input('El alumnno ha aprobado? [S/N]').upper() == 'S')
                alumno['Aprobado']= nuevo_aprobado
            
            print('El alumno ha sido actualizado correctamente.')
            return
    print('El alumno no ha sido encontrado')
                
# 4. Funcion para mostrar los datos del alumno por NIF

def listar_nif_alumnos():
    nif= input('Ingrese el NIF del cual desea ver sus datos: ')

    for alumno in alumnos:
        if alumno['NIF'] == nif:
            print('Los datos del alumno mencionado son: ')
            print('NIF: ', alumno['NIF'])
            print('Nombre: ', alumno['Nombre'])
            print('Apellidos: ', alumno['Apellidos'])
            print('Telefono: ', alumno['Telefono'])
            print('Email: ', alumno['Email'])
            print('Aprobado: ', alumno['Aprobado'])
            return
        
    print('El alumno no existe')

# 5. Funcion para mostrar los datos de un alumno por Email

def listar_email_alumnos():
    email= input('Ingrese el email del alumno del cual desea ver sus datos: ')

    for alumno in alumnos:
        if alumno['Email'] == email:
            print('NIF: ', alumno['NIF'])
            print('Nombre: ', alumno['Nombre'])
            print('Apellidos: ', alumno['Apellidos'])
            print('Telefono: ', alumno['Telefono'])
            print('Email: ', alumno['Email'])
            print('Aprobado: ', alumno['Aprobado'])
            return
        
    print('El alumno no existe')

# 6. Funcion para listar a todos los Alumnos

def listar_todos_alumnos():
    if not alumnos:
        print('No hay ningun alumno en la base de datos')
        return
    
    for alumno in alumnos:        
        print('NIF: ', alumno['NIF'])
        print('Nombre: ', alumno['Nombre'])
        print('Apellidos: ', alumno['Apellidos'])
        print('Telefono: ', alumno['Telefono'])
        print('Email: ', alumno['Email'])
        print('Aprobado: ', alumno['Aprobado'])

# 7. Funcion para aprobar alumno por NIF

def aprobar_alumno_por_nif():
    nif = input('Ingrese el NIF del alumno que desea aprobar: ')

    for alumno in alumnos:
        if alumno['NIF'] == nif:
            alumno['Aprobado']= True
            print('El alumno ha sido aprobado')
            return 
    print('No existe ningun alumno con ese NIF')

# 8. Funcion para reprobar alumno por NIF

def reprobar_alumno_por_nif():
    nif = input('Ingrese el NIF del alumno que desea aprobar: ')

    for alumno in alumnos:
        if alumno['NIF'] == nif:
            alumno['Aprobado']= False
            print('El alumno ha sido reprobado')
            return 
    print('No existe ningun alumno con ese NIF')

# 9. Funcion para mostrar todos los alumnos aprobados

def mostrar_alumnos_aprobados():
    
    for alumno in alumnos:
        if alumno['Aprobado']== True:
            print('NIF: ', alumno['NIF'])
            print('Nombre: ', alumno['Nombre'])
            print('Apellidos: ', alumno['Apellidos'])
            print('--------------------')

# 10. Funcion para mostrar todos los alumnos reprobados

def mostrar_alumnos_reprobados():
    
    for alumno in alumnos:
        if not alumno['Aprobado']== False:
            print('NIF: ', alumno['NIF'])
            print('Nombre: ', alumno['Nombre'])
            print('Apellidos: ', alumno['Apellidos'])
            print('--------------------')

# 11. Generando el programa 

while True:
    print('1. Añadir Alumno')
    print('2. Eliminar alumno por NIF')
    print('3. Actualice datos del alumno por NIF')
    print('4. Mostrar los datos del alumno por NIF')
    print('5. Mostrar datos del alumno pior Email')
    print('6. Listar todos los alumnos')
    print('7. Aprobar alumno por NIF')
    print('8. Suspender alumno por NIF')
    print('9. Mostrar alumnos aprobados')
    print('10. Mostrar alumnos reprobados')
    print('X. Finalizar el programa')

    opcion = input('Introduce una de las opciones: ')

    if opcion == '1':
        agregar_alumnno()
    elif opcion == '2':
        eliminar_alumno()
    elif opcion == '3':
        actualizar_alumno()
    elif opcion == '4':
        listar_nif_alumnos()
    elif opcion == '5':
        listar_email_alumnos()
    elif opcion == '6':
        listar_todos_alumnos()
    elif opcion == '7':
        aprobar_alumno_por_nif()
    elif opcion == '8':
        reprobar_alumno_por_nif()
    elif opcion == '9':
        mostrar_alumnos_aprobados()
    elif opcion == '10':
        mostrar_alumnos_reprobados()
    elif opcion.upper() == 'X':
        break
    else:
        print('Opcion no valida, por favor elija una de las opciones validas')














            


        

