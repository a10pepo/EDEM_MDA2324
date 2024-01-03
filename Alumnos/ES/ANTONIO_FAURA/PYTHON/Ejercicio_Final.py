class Alumno:
  def __init__(self, NIF: str, nombre: str, apellidos: str, telefono: str, email: str, aprobado: bool = False):
      self.nif = NIF
      self.nombre = nombre
      self.apellidos = apellidos
      self.telefono = telefono
      self.email = email
      self.aprobado = aprobado

class CambiosAlumnos:
  def __init__(self):
      self.alumnos = []

  def append_alumno(self, alumno):
      self.alumnos.append(alumno)

  def eliminar_alumno_por_nif(self, nif):
      for alumno in self.alumnos:
          if alumno.nif == nif:
              self.alumnos.remove(alumno)
              print(f'  ')
              print(f'  ')
              print(f"Alumno con NIF {nif} eliminado.")
              return
      print(f"No se encontró ningún alumno con NIF {nif}")

  def actualizar_datos_por_nif(self, nif):
      for alumno in self.alumnos:
          if alumno.nif == nif:
              nuevo_nombre = input("Nuevo nombre: ")
              nuevo_apellido = input("Nuevos apellidos: ")
              nuevo_telefono = input("Nuevo teléfono: ")
              nuevo_email = input("Nuevo email: ")
              alumno.nombre = nuevo_nombre
              alumno.apellidos = nuevo_apellido
              alumno.telefono = nuevo_telefono
              alumno.email = nuevo_email
              print(f'  ')
              print(f'  ')
              print("Datos actualizados correctamente.")
              return
      print(f"No se encontró ningún alumno con NIF {nif}")

  def mostrar_datos_por_nif(self, nif):
      for alumno in self.alumnos:
          if alumno.nif == nif:
              print(f'  ')
              print(f'  ')
              print(f"Datos del alumno con NIF {nif}:")
              print(f"Nombre: {alumno.nombre}")
              print(f"Apellidos: {alumno.apellidos}")
              print(f"Teléfono: {alumno.telefono}")
              print(f"Email: {alumno.email}")
              print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
              return
      print(f"No se encontró ningún alumno con NIF {nif}")

  def mostrar_datos_por_email(self, email):
      for alumno in self.alumnos:
          if alumno.email == email:
              print(f'  ')
              print(f'  ')
              print(f"Datos del alumno con Email {email}:")
              print(f"Nombre: {alumno.nombre}")
              print(f"Apellidos: {alumno.apellidos}")
              print(f"Teléfono: {alumno.telefono}")
              print(f"NIF: {alumno.nif}")
              print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
              return
      print(f"No se encontró ningún alumno con gmail {email}")

  def listar_alumnos(self):
      print(f'  ')
      print(f'  ')
      print("Lista de todos los alumnos:")
      for alumno in self.alumnos:
          print(f"{alumno.nombre} {alumno.apellidos} - NIF: {alumno.nif}")

  def aprobar_alumno_por_nif(self, nif):
      for alumno in self.alumnos:
          if alumno.nif == nif:
              alumno.aprobado = True
              print(f'  ')
              print(f'  ')
              print(f"Al alumno con NIF {nif} le ha salvado la evaluacion continua.")
              return
      print(f"No se encontró ningún alumno con NIF {nif}")

  def suspender_alumno_por_nif(self, nif):
      for alumno in self.alumnos:
          if alumno.nif == nif:
              alumno.aprobado = False
              print(f'  ')
              print(f'  ')
              print(f"El alumno con NIF {nif} a recus.")
              return
      print(f"No se encontró ningún alumno con NIF {nif}")

  def mostrar_alumnos_aprobados(self):
      print(f'  ')
      print(f'  ')
      print("Alumnos Aprobados:")
      for alumno in self.alumnos:
          if alumno.aprobado:
              print(f"NIF: {alumno.nif} - Nombre: {alumno.nombre} {alumno.apellidos}")

  def mostrar_alumnos_suspensos(self):
      print(f'  ')
      print(f'  ')
      print("Alumnos Suspendidos:")
      for alumno in self.alumnos:
          if not alumno.aprobado:
              print(f"NIF: {alumno.nif} - Nombre: {alumno.nombre} {alumno.apellidos}")


cambios_alumnos = CambiosAlumnos()

while True:
  print(f'  ')
  print(f'  ')
  print(f'  ')
  print(f'----------------------------------------------------------------------------')
  print(f'  ')
  print(f'  ')
  print("--> MENU PRINCIPAL:")
  print("(1) Añadir un alumno")
  print("(2) Eliminar alumno por NIF")
  print("(3) Actualizar datos de un alumno por NIF")
  print("(4) Mostrar datos de un alumno por NIF")
  print("(5) Mostrar datos de un alumno por Email")
  print("(6) Listar TODOS os alumnos")
  print("(7) Aprobar Alumno por NIF")
  print("(8) Suspender Alumno por NIF")
  print("(9) Mostrar alumnos aprobados")
  print("(10) Mostrar alumnos suspensos")
  print("(X) Finalizar Programa")

  opcion = input("Seleccione una opción: ").upper()

  if opcion == "1":  # Añadir un alumno
      nif_nuevo = input("Introduce el NIF del nuevo alumno: ")
      nombre_nuevo = input("Introduce el nombre del nuevo alumno: ")
      apellido_nuevo = input("Introduce el apellido del nuevo alumno: ")
      telefono_nuevo = input("Introduce el teléfono del nuevo alumno: ")
      email_nuevo = input("Introduce el email del nuevo alumno: ")

      nuevo_alumno = Alumno(nif_nuevo, nombre_nuevo, apellido_nuevo, telefono_nuevo, email_nuevo)
      cambios_alumnos.append_alumno(nuevo_alumno)

  elif opcion == "2":  # Eliminar alumno por NIF
      nif_eliminar = input("Introduce el NIF del alumno a eliminar: ")
      cambios_alumnos.eliminar_alumno_por_nif(nif_eliminar)

  elif opcion == "3":  # Actualizar datos de un alumno por NIF
      nif_actualizar = input("Introduce el NIF del alumno a actualizar: ")
      cambios_alumnos.actualizar_datos_por_nif(nif_actualizar)

  elif opcion == "4":  # Mostrar datos de un alumno por NIF
      nif_mostrar = input("Introduce el NIF del alumno a mostrar: ")
      cambios_alumnos.mostrar_datos_por_nif(nif_mostrar)

  elif opcion == "5":  # Mostrar datos de un alumno por Email
      email_mostrar = input("Introduce el Email del alumno a mostrar: ")
      cambios_alumnos.mostrar_datos_por_email(email_mostrar)

  elif opcion == "6":  # Listar los alumnos
      cambios_alumnos.listar_alumnos()

  elif opcion == "7":  # Aprobar Alumno por NIF
      nif_aprobar = input("Introduce el NIF del alumno a aprobar: ")
      cambios_alumnos.aprobar_alumno_por_nif(nif_aprobar)

  elif opcion == "8":  # Suspender Alumno por NIF
      nif_suspender = input("Introduce el NIF del alumno a suspender: ")
      cambios_alumnos.suspender_alumno_por_nif(nif_suspender)

  elif opcion == "9":  # Mostrar alumnos aprobados
      cambios_alumnos.mostrar_alumnos_aprobados()

  elif opcion == "10":  # Mostrar alumnos suspensos
      cambios_alumnos.mostrar_alumnos_suspensos()

  elif opcion == "X":  # Cerrar Programa
      break
  else:
      print("Opción no válida. Intente de nuevo.")

