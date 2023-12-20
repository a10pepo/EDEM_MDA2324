


alumnos = {}


##funcion añadir alumno 1
def anadir_alumno(alumnos):
   NIF_alumno = str(input('ingrese NIF : '))
   nombre_alumno = str(input('ingrese nombre : '))
   apellidos_alumno = str(input('ingrese apellidos : '))
   telefono_alumno = str(input('ingrese telefono : '))
   email_alumno = str(input('ingrese mail : '))
   aprobado_alumno = bool(input( '¿ está aprobado ? (S/N) ').lower()=='s')

   alumnos[NIF_alumno] = {
        "NIF": NIF_alumno,
        "Nombre": nombre_alumno,
        "Apellidos": apellidos_alumno,
        "Telefono": telefono_alumno,
        "Email": email_alumno,
        "Aprobado": aprobado_alumno
    }
   print('el alumno ha sido añadido correctamente')



##funcion eliminar alumno por nif 2

def eliminar_alumno(alumnos):
    NIF_alumno = input(str('ingrese nif del alumno que quiera eliminar : '))
    if NIF_alumno in alumnos:
     del alumnos[NIF_alumno]
     print('alumno eliminado correctamente')
    else:
       print('no se ha encontrado el NIF')

## actualizar alumnos por NIF 3

def actualizar_alumnos(alumnos):
    NIF_alumno = str(input('Ingrese NIF del alumno que desea actualizar: '))
    if NIF_alumno in alumnos:
            alumno = alumnos[NIF_alumno]
            alumno['nombre'] = input(f"Nuevo nombre para {alumno['Nombre']}: ")
            alumno['apellidos'] = input(f"Nuevos apellidos para {alumno['Apellidos']}: ")
            alumno['telefono'] = input(f"Nuevo teléfono para {alumno['Telefono']}: ")
            alumno['email'] = input(f"Nuevo email para {alumno['Email']}: ")
            print("Los datos han sido actualizados correctamente")
    else:
            print("Alumno no encontrado.")

          


#MOSTRAR DATOS DE UN ALUMNO POR NIF 4

def mostrar_datos(alumnos):
   NIF_alumno = str(input('Ingrese NIF del alumno que quiera ver: '))
   if NIF_alumno in alumnos:
      alumno = alumnos[NIF_alumno]
      print(f'''los datos del alumno con el NIF{NIF_alumno} son :
            
            Nombre : {alumno['Nombre']}
            Apellidos: {alumno['Apellidos']}
            Telefono: {alumno['Telefono']}
            Email: {alumno['Email']}
            Aprobado: {alumno['Aprobado']}''')

            

#mostrar datos alumnos por mail 5



def mostrar_datos_mail(alumnos):
    
    email_alumno = str(input('Ingrese email del alumno que desea mostrar: '))
    for alumno in alumnos.values():
        if alumno['Email'] == email_alumno:
            print(f"NIF: {alumno['NIF']}")
            print(f"Nombre: {alumno['Nombre']}")
            print(f"Apellidos: {alumno['Apellidos']}")
            print(f"Telefono: {alumno['Telefono']}")
            print(f"Email: {alumno['Email']}")
            print(f"Aprobado: {'Sí' if alumno['Aprobado'] else 'No'}")
            
    
##Listar TODOS os alumnos mirar si va 6

def mostrar_alumnos(alumnos):
    print('listado con los datos de los alumnos')
    for clave, alumno in alumnos.items():
        print(f'{clave}: {alumno}')

   


       
##Aprobar Alumno por NIF 7

def aprobar_por_NIF(alumnos):
    NIF_alumno = str(input('Ingrese NIF del alumno que desea actualizar: '))
    if NIF_alumno in alumnos:
       alumnos[NIF_alumno]['aprobado'] = True
       print('alumno aprobado')
    else :
       print('alumno suspendido')
   
   



##Suspender Alumno por NIF 8

def suspender_por_NIF(alumnos):
    NIF_alumno = str(input('Ingrese NIF del alumno que desea actualizar: '))
    if NIF_alumno in alumnos:
       alumnos[NIF_alumno]['aprobado'] = False
       print('alumno suspendido')
    else :
       print('alumno aprobado')




##Mostrar alumnos aprobados 9

def alumnos_aprobados(alumnos):
    print('el listado de los alumnos aprobados es : ')
    for clave, alumno in alumnos.items():
        if alumno['Aprobado'] == True:
            print(f"{clave}: {alumno}")


## Mostrar alumnos suspensos 10


def alumnos_suspendidos(alumnos):
   print('el listado de los alumnos suspendidos es : ')
   for clave, alumno in alumnos.items():
      if alumno['Aprobado'] == False:
         print(f"{clave}: {alumno}")



## Funcion final para llamar al resto de las funciones segun la opcion que queramos 


def pulsar_tecla(alumnos):
    while True:
        print('''PULSE LA TECLA QUE DESEA
            
             1. Añadir un alumno 
             2. Eliminar alumno por NIF 
             3. Actualizar datos de un alumno por NIF 
             4. Mostrar datos de un alumno por NIF 
             5. Mostrar datos de un alumno por Email 
             6. Listar TODOS los alumnos 
             7. Aprobar Alumno por NIF 
             8. Suspender Alumno por NIF 
             9. Mostrar alumnos aprobados 
             10. Mostrar alumnos suspensos 
             X. Finalizar Programa''')
            
        tecla = input('Ingrese la opción que desea: ')

        if tecla == '1':
            anadir_alumno(alumnos)
        elif tecla == '2':
            eliminar_alumno(alumnos)
        elif tecla == '3':
            actualizar_alumnos(alumnos)
        elif tecla == '4':
            mostrar_datos(alumnos)
        elif tecla == '5':
            mostrar_datos_mail(alumnos)
        elif tecla == '6':
            mostrar_alumnos(alumnos)
        elif tecla == '7':
            aprobar_por_NIF(alumnos)
        elif tecla == '8':
            suspender_por_NIF(alumnos)
        elif tecla == '9':
            alumnos_aprobados(alumnos)
        elif tecla == '10':
            alumnos_suspendidos(alumnos)
        elif tecla.lower() == 'x':
            break
               

pulsar_tecla(alumnos)