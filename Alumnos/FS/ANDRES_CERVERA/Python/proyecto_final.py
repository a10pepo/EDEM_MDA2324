alumnos = []

#llamado de funciones desde main
def main():
    print(f'¿Qué quieres hacer?\n'
          f'1 --> Añadir alumno\n'
          f'2 --> Eliminar alumno por NIF\n'
          f'3 --> Actualizar datos de alumno por NIF\n'
          f'4 --> Mostrar datos de un alumno por NIF\n'
          f'5 --> Mostrar datos de un alumno por Email\n'
          f'6 --> Listar todos los alumnos\n'
          f'7 --> Aprobar alumno por NIF\n'
          f'8 --> Suspender alumno por NIF\n'
          f'9 --> Mostrar alumnos aprobados\n'
          f'10 --> Mostrar alumnos suspendidos\n'
          f'X --> Salir')

    numero = input('')

    if (numero == '1'):
        añadir_alumno()
    
    elif (numero == '2'): 
        eliminar_alumno()   
    
    elif (numero == '3'):  
        actualizar_datos()
           
    elif (numero == '4'):
        mostrar_por_nif()
    
    elif (numero == '5'):
        mostrar_por_email()
    
    elif (numero == '6'):
       listar_todos()
    
    elif (numero == '7'):
       aprobar_alumno()
       
    elif (numero == '8'):
        suspender_alumno()
        
    elif (numero == '9'):
        mostrar_aprobados()
        
    elif (numero == '10'):
        mostrar_suspendidos()
    
    elif (numero.upper() == 'X'):
        salir()
            
    else:
        print(f'Caracter no válido. Proporciona otro.')
        main()

#funcion añadir alumno
def añadir_alumno():
    print(f'Rellene los siguientes datos:\n')
    NIF = input('NIF: ')
    Nombre = input('Nombre: ')
    Apellidos = input('Apellidos: ')
    Telefono = input('Telefono: ')
    Email = input('Email: ')
    Calificacion = 'NC'
    
    nuevo_alumno = {
            "NIF": NIF,
            "Nombre": Nombre,
            "Apellidos": Apellidos,
            "Telefono": Telefono,
            "Email": Email,
            "Calificacion": Calificacion
        }
    
    alumnos.append(nuevo_alumno)
    print(f'Alumno añadido correctamente.')
    otra_operacion()

#funcion eliminar alumno
def eliminar_alumno():
    print(f'Escriba el NIF del alumno a eliminar:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(NIF == alumno['NIF']):
            alumnos.remove(alumno) 
            print(f'Alumno eliminado correctamente')
            otra_operacion()
            return
    print(f'No se ha encontrado ningún alumno con ese NIF')
    otra_operacion()

#funcion actualizar datos por NIF   
def actualizar_datos():
    print(f'Escriba el NIF del alumno a actualizar:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(alumno['NIF'] == NIF):
            print(f'Rellene los datos para actualizar el alumno:\n')
            NIF_actualizado = input('NIF: ')
            Nombre_actualizado = input('Nombre: ')
            Apellidos_actualizado = input('Apellidos: ')
            Telefono_actualizado = input('Telefono: ')
            Email_actualizado = input('Email: ')
            Calificacion_actualizado = 'NC'
            
            alumno['NIF'] = NIF_actualizado
            alumno['Nombre'] = Nombre_actualizado
            alumno['Apellidos'] = Apellidos_actualizado
            alumno['Telefono'] = Telefono_actualizado
            alumno['Email'] = Email_actualizado
            alumno['Calificacion'] = Calificacion_actualizado
            
            print(f'Alumno actualizado correctamente:\n')
            otra_operacion()
            return
    print(f'No se ha encontrado ningún alumno con ese NIF')       
    otra_operacion()
          
#funcion mostrar datos por NIF                       
def mostrar_por_nif():
    print(f'Escriba el NIF del alumno a mostrar:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(alumno['NIF'] == NIF):
            print('Datos del alumno:')
            print(f'NIF: {alumno["NIF"]}')
            print(f'Nombre: {alumno["Nombre"]}')
            print(f'Apellidos: {alumno["Apellidos"]}')
            print(f'Teléfono: {alumno["Telefono"]}')
            print(f'Email: {alumno["Email"]}')
            print(f'Calificación: {alumno["Calificacion"]}')
            otra_operacion()
            return
    print(f'No se ha encontrado ningún alumno con ese NIF')   
    otra_operacion()

#funcion mostrar datos por email            
def mostrar_por_email():
    print(f'Escriba el Email del alumno a mostrar:\n')
    email = input('Email: ')
    for alumno in alumnos:
        if(alumno['Email'] == email):
            print('Datos del alumno:')
            print(f'NIF: {alumno["NIF"]}')
            print(f'Nombre: {alumno["Nombre"]}')
            print(f'Apellidos: {alumno["Apellidos"]}')
            print(f'Teléfono: {alumno["Telefono"]}')
            print(f'Email: {alumno["Email"]}')
            print(f'Calificación: {alumno["Calificacion"]}')
            otra_operacion()
            return
    print(f'No se ha encontrado ningún alumno con ese Email')
    otra_operacion()

#funcion aprobar alumno por NIF            
def aprobar_alumno():
    print(f'Escriba el NIF del alumno a aprobar:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(NIF == alumno['NIF']):
            alumno['Calificacion'] = 'Aprobado'   
            print(f'Alumno aprobado')
            otra_operacion()
            return
    print(f'No se ha encontrado ningún alumno con ese NIF')
    otra_operacion()

#funcion suspender alumno por NIF
def suspender_alumno():
    print(f'Escriba el NIF del alumno a suspender:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(NIF == alumno['NIF']):
            alumno['Calificacion'] = 'Suspendido'   
            print(f'Alumno suspendido')
            otra_operacion()
            return
    print(f'No se ha encontrado ningún alumno con ese NIF')
    otra_operacion()

#funcion mostrar aprobados
def mostrar_aprobados():
    for alumno in alumnos:
        if(alumno['Calificacion'] == 'Aprobado'):
            print(f'{alumno}\n')
            otra_operacion()
            return
    print(f'No hay ningún alumno aprobado')
    otra_operacion()

#funcion mostrar suspendidos
def mostrar_suspendidos():
    for alumno in alumnos:
        if(alumno['Calificacion'] == 'Suspendido'):
            print(f'{alumno}\n')
            otra_operacion()
            return
    print(f'No hay ningún alumno suspendido')
    otra_operacion()
                   
#funcion listar alumno
def listar_todos():
    for alumno in alumnos:
        print(f'Alumno {alumno}: {alumnos}\n')
        otra_operacion()
        return
    print(f'No hay alumnos registrados')
    otra_operacion()

#funcion para poder solicitar mas operaciones al acabar una
def otra_operacion():
    print(f'¿Desea realizar otra operación?\n'
          f'1 --> Sí\n'
          f'X -- Salir')
    numero = input('')
    if (numero == '1'):
        main()
    elif (numero.upper() == 'X'):
        salir()
    else:
        print(f'Caracter no válido')
        otra_operacion()

#funcion para abandonar el programa
def salir():
    print(f'¡Nos vemos!')
    exit()

 #llamada al programa 
main()