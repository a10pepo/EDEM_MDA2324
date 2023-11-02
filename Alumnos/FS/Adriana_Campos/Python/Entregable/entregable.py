# Proyecto Final 
# Curso Python - EDEM_MDA2324
# Una empresa de formación quiere gestionar su cartera de alumnos.


alumnos = [
    { 'NIF':'113004000R', 'nombre': 'Gabriela', 'Apellidos': 'Campos Romero', 'Telefono': 69809977, 'Email':'gabriela@gmail.com','Aprobado':False},
    { 'NIF':'123004000R', 'nombre': 'Laura', 'Apellidos': 'Gonzalez Romero', 'Telefono': 69809977, 'Email':'laura@gmail.com','Aprobado':False},
    { 'NIF':'133004000R', 'nombre': 'Paula', 'Apellidos': 'Alonso Romero', 'Telefono': 69809977, 'Email':'paula@gmail.com','Aprobado':True},
    { 'NIF':'143004000R', 'nombre': 'Lucia', 'Apellidos': 'Vera Romero', 'Telefono': 69809977, 'Email':'lucia@gmail.com','Aprobado':False}
]

print (alumnos)


while True:

  print(' \n(1) Añadir un alumno \n(2) Eliminar alumno por NIF \n(3) Actualizar los datos de un alumno por NIF \n(4) Mostrar datos de un alumno por NIF \n(5) Mostrar datos de un alumno por email \n(6) Listar todos los alumnos \n(7) Aprobar a un alumno por NIF \n(8) Suspender a un alumno por NIF \n(9) Mostrar ÚNICAMENTE los clientes preferentes \n(10) Finalizar Programa \n')
  
  posicion = 0
  opcion = input("Seleccione una opción y si quiere finalizar pulse x: ")

  if opcion == '1':
    AddAlumno = { 'NIF':'113004000R', 'nombre': 'Adriana', 'Apellidos': 'Campos Romero', 'Telefono': 69809977, 'Email':'adriana@gmail.com','Preferente':False }
    alumnos.append(AddAlumno)

  elif opcion == '2':
    EliminarAlumno= input('Dime el NIF del alumno que quieres eliminar: ')
    for x in alumnos:
      posicion += posicion
      if(x['NIF'] == EliminarAlumno):
        alumnos.pop(posicion)

  elif opcion == '3':
    ActualizarAlumno= input('Dime el NIF del alumno que quieres actualizar: ')
    for x in alumnos:
      if(x['NIF'] == ActualizarAlumno):
        print(' ¿Que quiere actualizar de este alumno? \n(1) NIF \n(2) Nombre \n(3) Apellidos\n(4) Telefono \n(5) Email \n(6) Aprobado')
        opcionActualizar = input('Elija que quiere actualizar de este alumno:')
        if (opcionActualizar == '1'):
          email = input('Escriba el nuevo NIF:')
          x['NIF'] = email
        if (opcionActualizar == '2'):
          nombre = input('Escriba el nuevo nombre:')
          x['nombre'] = nombre
        if (opcionActualizar == '3'):
          apellidos = input('Escriba el nuevo apellidos:')
          x['Apellidos'] = apellidos
        if (opcionActualizar == '4'):
          telefono = input('Escriba el nuevo telefono:')
          x['Telefono'] = telefono
        if (opcionActualizar == '5'):
          email = input('Escriba el nuevo email:')
          x['Email'] = email
        if (opcionActualizar == '6'):
          aprobado = input('Escriba el nuevo aprobado:')
          x['Aprobado'] = aprobado

  elif  opcion == '4':
    MostrarAlumnoNIF= input('Dime el NIF del cliente que quieres mostrar: ')
    for x in alumnos:
      if(x['NIF'] == MostrarAlumnoNIF):
        print(x)

  elif  opcion == '5':
   MostrarClienteEmail= input('Dime el NIF del cliente que quieres mostrar: ')
   for x in alumnos:
      if(x['Email'] == MostrarClienteEmail):
       print(x)

  elif  opcion == '6':
   print(alumnos)

  elif  opcion == '7':
    AprobarAlumnoNif= input('Dime el NIF del cliente que quieres aprobar: ')
    for x in alumnos:
     if(x['NIF'] == AprobarAlumnoNif):
        x['Aprobado'] == True 

  elif  opcion == '8':
    SuspenderAlumnoNif= input('Dime el NIF del cliente que quieres suspender: ')
    for x in alumnos:
     if(x['NIF'] == SuspenderAlumnoNif):
        x['Aprobado'] == False 

  elif  opcion == '9':
    for n in alumnos:
     if(n['Aprobado']==True):
       print(f'Estos son los alumnos aprobados: \n{n}\n')

  elif  opcion == '10':
    for n in alumnos:
     if(n['Aprobado']==False):
        print(f'Estos son los alumnos suspendidos: \n{n}\n')

  elif  opcion == 'x' or opcion == 'X':
    print ('FIN')
    print (alumnos)
    break
  else:
    print('No ha elegido ninguna opción valida')








