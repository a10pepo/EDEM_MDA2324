#Una empresa de formación quiere gestionar su cartera de alumnos.
#Escribe un programa que guarde una lista. Cada Alumno dispone de los siguientes campos:

lista_master=[]
opcion_escogida = ''
while(opcion_escogida != 'x'):
  opcion_escogida = input(
'''
Hola, selecciona que deseas realizar:

1. Añadir un alumno
2. Eliminar alumno 
3. Actualizar datos de un alumno por NIF
4. Mostrar datos de un alumno por NIF
5. Mostrar datos de un alumno por Email
6. Listar TODOS los alumnos
7. Aprobar alumno por NIF
8. Suspender alumno por NIF
9. Mostrar alumnos aprobados
10.Mostrar alumnos suspensos
x. Salir del programa

''')
  if (opcion_escogida) == '1':
      print("ingrese los siguientes campos del alumno a inscribir:")
      nif:str=input('ingresa NIF:  ')
      nombre:str=input("ingresa nombre:  ")
      apellido:str=input("ingresa apellido:  ")
      telefono:str=input("ingrese telefono:  ")
      email:str=input("ingrese correo electronico:  ")
      aprobacion:bool=input("el alumno aprobo SI/NO?:  ")
      if aprobacion.lower()== 'si':
        aprobacion == True
      elif aprobacion.lower() == 'no':
        aprobacion == False
      else:
        print('Error, por favor ingrese si/no.')
        continue
      
      alumno = {
    'nif': nif,
    'nombre': nombre,
    'apellido': apellido,
    'telefono': telefono,
    'email': email,
    'aprobado': aprobacion
      }
      
      lista_master.append(alumno)
      print(f"el alumno {nombre} se ha ingresado de manera satisfactoria")
      #print(*lista_master)
    
  elif(opcion_escogida) == '2':
    nombre_a_eliminar:str= input('\nIngrese el NIF del alumno a eliminar: ')
    encontrado = False
    for i in range (len(lista_master)):
      if lista_master[i]["nif"] == nombre_a_eliminar:
        del lista_master[i]
        encontrado = True
        print(f"Estudiante con NIF {nombre_a_eliminar} borrado correctamente.") 
        break
    if not encontrado:
      print(f"No se encontró ningún estudiante con NIF {nombre_a_eliminar}.")
        
    
  elif(opcion_escogida) == '3':
    nombre_buscar:str = input('\n Ingrese el NIF del alumno a actualizar:  ')
    encontrado= False
    for alumno in lista_master:
      if alumno['nif'] == nombre_buscar:
        encontrado=True
        print(f'n\Ingrese los datos del alumno a actualizar: ')
    #si encuentra alumno:   
        alumno['nombre']:str=input("ingresa nombre:  ")
        alumno['apellido']:str=input("ingresa apellido:  ")
        alumno['telefono']:str=input("ingrese telefono:  ")
        alumno['email']:str=input("ingrese correo electronico:  ")
        alumno['aprobado']:bool=input("el alumno aprobo, SI/NO?:  ").lower()
        print(f"Alumno con NIF: '{nombre_buscar}' actualizado correctamente.")
        break
      if not encontrado:
        print('\n Alumno no encontrado con Nif')
        
  elif(opcion_escogida) == '4':
    mostrar_alumno:str = input('\n Ingrese el NIF del alumno a buscar:  ')
    encontrado=False
    for alumno in lista_master:
      if alumno['nif'] == mostrar_alumno:
        encontrado=True
        print("\nDatos del alumno:")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Telefono: {alumno['telefono']}")
        print(f"Email: {alumno['email']}")
        print(f"Aprobado: {alumno['aprobado']}")
        break
      if not encontrado:
        print('\n Alumno no encontrado con Nif.')
    
  elif(opcion_escogida) == '5':
    mostrar_alumno:str = input('\n Ingrese el Email del alumno a buscar:  ')
    encontrado=False
    for alumno in lista_master:
      if alumno['email'] == mostrar_alumno:
        encontrado=True
        print("\nDatos del alumno:")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Telefono: {alumno['telefono']}")
        print(f"Email: {alumno['email']}")
        print(f"Aprobado: {alumno['aprobado']}")
        break
      if not encontrado:
        print('\n Alumno no encontrado con Nif.')
        
  elif(opcion_escogida) == '6':
    print('''
******************** Listado Estudiantes ************************''')
    print(f"{'NIF':<10}|{'Nombre':<15}| {'Apellido':<15}| {'Telefono':<13}| {'Email':<12}| {'Aprobado':<10}")
    for element in lista_master:
      nif_al = element['nif']
      nombre_al =  element['nombre']
      apellido_al = element['apellido']
      telefono_al = element['telefono']
      email_al = element['email']
      aprobacion_al = element['aprobado']
      print(
        f'{nif_al:<10}{nombre_al:<18}{apellido_al:<18}{telefono_al:<16}{email_al:<15}{aprobacion_al:<12}'
        )
      
  elif(opcion_escogida) == '7':
    nombre_buscar:str = input('\n Ingrese el NIF del alumno a aprobar:  ')
    encontrado= False
    for alumno in lista_master:
      if alumno['nif'] == nombre_buscar:
        encontrado=True
    #si encuentra alumno:   
        alumno['aprobado']:bool=input("el alumno aprobo, SI/NO?:  ")
        if aprobacion.lower()== 'si':
          aprobacion == True
        elif aprobacion.lower() == 'no':
          aprobacion == False
        else:
          print('Error, por favor ingrese si/no.')
          continue
        print(f"Alumno con NIF: '{nombre_buscar}' ha aprobado.")
        break
    if not encontrado:
      print('\n Alumno no encontrado con Nif')
        
  elif(opcion_escogida) == '8':
    nombre_buscar:str = input('\n Ingrese el NIF del alumno a suspender:  ')
    encontrado= False
    for alumno in lista_master:
      if alumno['nif'] == nombre_buscar:
        encontrado=True
        alumno['aprobado']:bool=input("el alumno aprobo, SI/NO?:  ").lower()
        print(f"Alumno con NIF: '{nombre_buscar}' suspendido.")
        break
      if not encontrado:
        print('\n Alumno no encontrado con Nif')
        
  elif(opcion_escogida) == '9':
     print('''
******************** Listado aprobados ************************''')
     print(f"{'NIF':<10}|{'Nombre':<12}| {'Apellido':<12}| {'Telefono':<12}| {'Email':<12}|")
     for element in lista_master:
      nif_al = element['nif']
      nombre_al =  element['nombre']
      apellido_al = element['apellido']
      telefono_al = element['telefono']
      email_al = element['email']
      aprobacion_al = element['aprobado']
      if aprobacion_al == 'si':
        print(
      f'{nif_al:<12}{nombre_al:<15}{apellido_al:<15}{telefono_al:<15}{email_al:<15}'
        )
  elif(opcion_escogida) == '10':
    print('''
******************** Listado suspensos ************************''')
    print(f"{'NIF':<10}|{'Nombre':<12}| {'Apellido':<12}| {'Telefono':<12}| {'Email':<12}|")
    for element in lista_master:
      nif_al = element['nif']
      nombre_al =  element['nombre']
      apellido_al = element['apellido']
      telefono_al = element['telefono']
      email_al = element['email']
      aprobacion_al = element['aprobado']
      if aprobacion_al == 'no':
        print(
        f'{nif_al:<12}{nombre_al:<15}{apellido_al:<15}{telefono_al:<15}{email_al:<15}{aprobacion_al:<15}'
        )
  else:
        print("Gracias por utilizar nuestro programa")
    
        
        
    
        
      
    
          
    

        
        
      
        
    
    
    
      
  
  
      
      
      
    
    