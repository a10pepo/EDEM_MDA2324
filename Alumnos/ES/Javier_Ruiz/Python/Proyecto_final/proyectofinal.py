# la clase alumno define los campos que tiene cada alumno
class Alumno:         
  def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
      self.nif = nif
      self.nombre = nombre
      self.apellidos = apellidos
      self.telefono = telefono
      self.email = email
      self.aprobado = aprobado

# la clase modificaciones, que incluye la gestion y actualización de los campos de los alumnos , además he añadido una opción para volver al menú principal en caso de elegir equivocadamente una de las acciones

class Modificaciones:
  def __init__(self):
      self.alumnos = []  # lista de alumnos

  def agregar_alumno(self):  # 1
      while True:
          nif = input("Ingrese el NIF del alumno (o 'X' para volver al menú principal): ")
          if nif.upper() == 'X':
              print("Acción cancelada.\n")
              return
          nombre = input("Ingrese el nombre del alumno: ")
          apellidos = input("Ingrese los apellidos del alumno: ")
          telefono = input("Ingrese el teléfono del alumno: ")
          email = input("Ingrese el email del alumno: ")

          nuevo_alumno = Alumno(nif, nombre, apellidos, telefono, email)
          self.alumnos.append(nuevo_alumno)
          print("Alumno añadido correctamente.\n")
          break

  def eliminar_alumno(self, nif):  # 2
      while True:
          if nif.upper() == 'X':
              print("Acción cancelada.\n")
              return

          for alumno in self.alumnos:
              if alumno.nif == nif:
                  self.alumnos.remove(alumno)
                  print("Alumno eliminado correctamente.\n")
                  return
          print("Alumno no encontrado. Intente de nuevo (o 'X' para volver al menú principal): ")
          nif = input("Ingrese el NIF del alumno: ")

  def actualizar_datos(self, nif):  # 3
      while True:
          if nif.upper() == 'X':
              print("Acción cancelada.\n")
              return

          for alumno in self.alumnos:
              if alumno.nif == nif:
                  alumno.nombre = input("Nuevo nombre: ")
                  alumno.apellidos = input("Nuevos apellidos: ")
                  alumno.telefono = input("Nuevo teléfono: ")
                  alumno.email = input("Nuevo email: ")
                  print("Datos actualizados correctamente.\n")
                  return
          print("Alumno no encontrado. Intente de nuevo (o 'X' para volver al menú principal): ")
          nif = input("Ingrese el NIF del alumno: ")

  def mostrar_por_nif(self, nif):  # 4
      while True:
          if nif.upper() == 'X':
              print("Acción cancelada.\n")
              return

          for alumno in self.alumnos:
              if alumno.nif == nif:
                  print("NIF:", alumno.nif)
                  print("Nombre:", alumno.nombre)
                  print("Apellidos:", alumno.apellidos)
                  print("Teléfono:", alumno.telefono)
                  print("Email:", alumno.email)
                  print("Aprobado:", alumno.aprobado)
                  print("---------------------------")
                  return
          print("Alumno no encontrado. Intente de nuevo (o 'X' para volver al menú principal): ")
          nif = input("Ingrese el NIF del alumno: ")

  def mostrar_por_email(self, email):  # 5
      while True:
          if email.upper() == 'X':
              print("Acción cancelada.\n")
              return

          for alumno in self.alumnos:
              if alumno.email == email:
                  print("NIF:", alumno.nif)
                  print("Nombre:", alumno.nombre)
                  print("Apellidos:", alumno.apellidos)
                  print("Teléfono:", alumno.telefono)
                  print("Email:", alumno.email)
                  print("Aprobado:", alumno.aprobado)
                  print("---------------------------")
                  return
          print("Alumno no encontrado. Intente de nuevo (o 'X' para volver al menú principal): ")
          email = input("Ingrese el Email del alumno: ")

  def listar_todos(self):  # 6
      if not self.alumnos:
          print("No hay alumnos registrados.\n")
          return
      for alumno in self.alumnos:
          print("NIF:", alumno.nif)
          print("Nombre:", alumno.nombre)
          print("Apellidos:", alumno.apellidos)
          print("---------------------------")
      print()

  def aprobar_alumno(self, nif):  # 7
      while True:
          if nif.upper() == 'X':
              print("Acción cancelada.\n")
              return

          for alumno in self.alumnos:
              if alumno.nif == nif:
                  alumno.aprobado = True
                  print("Alumno aprobado correctamente.\n")
                  return
          print("Alumno no encontrado. Intente de nuevo (o 'X' para volver al menú principal): ")
          nif = input("Ingrese el NIF del alumno: ")

  def suspender_alumno(self, nif):  # 8
      while True:
          if nif.upper() == 'X':
              print("Acción cancelada.\n")
              return

          for alumno in self.alumnos:
              if alumno.nif == nif:
                  alumno.aprobado = False
                  print("Alumno suspendido correctamente.\n")
                  return
          print("Alumno no encontrado. Intente de nuevo (o 'X' para volver al menú principal): ")
          nif = input("Ingrese el NIF del alumno: ")

  def mostrar_aprobados(self):  # 9
      aprobados = [alumno for alumno in self.alumnos if alumno.aprobado]
      if not aprobados:
          print("Nadie ha aprobado.\n")
          return
      for alumno in aprobados:
          print("NIF:", alumno.nif)
          print("Nombre:", alumno.nombre)
          print("Apellidos:", alumno.apellidos)
          print("---------------------------")
      print()

  def mostrar_suspensos(self):  # 10
      suspendidos = [alumno for alumno in self.alumnos if not alumno.aprobado]
      if not suspendidos:
          print("Nadie ha suspendido.\n")
          return
      for alumno in suspendidos:
          print("NIF:", alumno.nif)
          print("Nombre:", alumno.nombre)
          print("Apellidos:", alumno.apellidos)
          print("---------------------------")
      print()

# interfaz
def main():        
  gestion_alumnos = Modificaciones()

  while True:
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

      opcion = input("Seleccione una opción: ")

      if opcion == "1":
          gestion_alumnos.agregar_alumno()
      elif opcion == "2":
          nif_eliminar = input("Ingrese el NIF del alumno a eliminar: ")
          gestion_alumnos.eliminar_alumno(nif_eliminar)
      elif opcion == "3":
          nif_actualizar = input("Ingrese el NIF del alumno a actualizar: ")
          gestion_alumnos.actualizar_datos(nif_actualizar)
      elif opcion == "4":
          nif_mostrar = input("Ingrese el NIF del alumno a mostrar: ")
          gestion_alumnos.mostrar_por_nif(nif_mostrar)
      elif opcion == "5":
          email_mostrar = input("Ingrese el Email del alumno a mostrar: ")
          gestion_alumnos.mostrar_por_email(email_mostrar)
      elif opcion == "6":
          gestion_alumnos.listar_todos()
      elif opcion == "7":
          nif_aprobar = input("Ingrese el NIF del alumno a aprobar: ")
          gestion_alumnos.aprobar_alumno(nif_aprobar)
      elif opcion == "8":
          nif_suspender = input("Ingrese el NIF del alumno a suspender: ")
          gestion_alumnos.suspender_alumno(nif_suspender)
      elif opcion == "9":
          gestion_alumnos.mostrar_aprobados()
      elif opcion == "10":
          gestion_alumnos.mostrar_suspensos()
      elif opcion == "X":
          break
        
      else:
          print("Opción inválida. Intente de nuevo.")

main()