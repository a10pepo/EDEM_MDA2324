from funciones import *

alumnos = {}
alumnos_pred()

while True: 
  print(""" PROGRAMA CARGADO
////////////////////////
(1) Añadir un alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS os alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa
////////////////////////
""")

  eleccion = input('Selecciona el número que desees')
  if eleccion == '1':
    añadir_alumno()
  elif eleccion == '2':
    valor = str(input('Selecciona el NIF del alumno que quieres eliminar'))
    eliminar_alumno(valor)
  elif eleccion == '3':
    valor = str(input('Selecciona el NIF del alumno que quieres modificar los datos'))
    actualizar_alumno(valor)
  elif eleccion == '4':
    valor = str(input('Selecciona el NIF del alumno que quieres mostrar'))
    mostrar_alumno_nif(valor)
  elif eleccion == '5':
    valor = str(input('Selecciona el email del alumno que quieres mostrar'))
    mostrar_alumno_email(valor)
  elif eleccion == '6':
    listar_alumnos()
  elif eleccion == '7':
    valor = str(input('Selecciona el NIF del alumno que quieres aprobar'))
    aprobar_alumno(valor)
  elif eleccion == '8':
    valor = str(input('Selecciona el NIF del alumno que quieres suspender'))
    suspender_alumno(valor)
  elif eleccion == '9':
    mostrar_aprobados()
  elif eleccion == '10':
    mostrar_suspendidos()
  elif eleccion.lower() == 'x':
    guardar_alumno()
    break
  else:
    print('Introduzca una opción correcta')