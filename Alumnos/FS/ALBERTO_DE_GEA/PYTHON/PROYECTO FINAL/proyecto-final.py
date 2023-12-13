class Alumno:
  def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
      self.nif = nif
      self.nombre = nombre
      self.apellidos = apellidos
      self.telefono = telefono
      self.email = email
      self.aprobado = aprobado

class GestorAlumnos:
  def __init__(self):
      self.alumnos = []

  def añadir_alumno(self):
      nif = input("NIF: ")
      nombre = input("Nombre: ")
      apellidos = input("Apellidos: ")
      telefono = input("Teléfono: ")
      email = input("Email: ")
      nuevo_alumno = Alumno(nif, nombre, apellidos, telefono, email)
      self.alumnos.append(nuevo_alumno)
      
      
  def eliminar_alumno(self, nif):
    alumno = self.buscar_alumno_por_nif(nif)

    if alumno:
        self.alumnos.remove(alumno)
        print(f"Alumno con NIF {nif} eliminado.")
    else:
        print(f"Alumno con NIF {nif} no encontrado.")

  def actualizar_datos(self, nif):
      alumno = self.buscar_alumno_por_nif(nif)
      if alumno:
          alumno.nombre = input("Nuevo nombre: ")
          alumno.apellidos = input("Nuevos apellidos: ")
          alumno.telefono = input("Nuevo teléfono: ")
          alumno.email = input("Nuevo email: ")

  def mostrar_por_nif(self, nif):
      alumno = self.buscar_alumno_por_nif(nif)
      if alumno:
          print(f"NIF: {alumno.nif}")
          print(f"Nombre: {alumno.nombre}")
          print(f"Apellidos: {alumno.apellidos}")
          print(f"Teléfono: {alumno.telefono}")
          print(f"Email: {alumno.email}")
          print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
      else:
          print("Alumno no encontrado.")

  def mostrar_por_email(self, email):
      alumno = next((alumno for alumno in self.alumnos if alumno.email == email), None)
      if alumno:
          self.mostrar_por_nif(alumno.nif)
      else:
          print("Alumno no encontrado.")

  def listar_alumnos(self):
      for alumno in self.alumnos:
          print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}")

  def aprobar_alumno(self, nif):
      alumno = self.buscar_alumno_por_nif(nif)
      if alumno:
          alumno.aprobado = True

  def suspender_alumno(self, nif):
      alumno = self.buscar_alumno_por_nif(nif)
      if alumno:
          alumno.aprobado = False

  def mostrar_aprobados(self):
      aprobados = [alumno for alumno in self.alumnos if alumno.aprobado]
      if aprobados:
          self.listar_alumnos(aprobados)
      else:
          print("No hay alumnos aprobados.")

  def mostrar_suspendidos(self):
      suspendidos = [alumno for alumno in self.alumnos if not alumno.aprobado]
      if suspendidos:
          self.listar_alumnos(suspendidos)
      else:
          print("No hay alumnos suspendidos.")

  def buscar_alumno_por_nif(self, nif):
      return next((alumno for alumno in self.alumnos if alumno.nif == nif), None)


def main():
  gestor_alumnos = GestorAlumnos()

  while True:
      print("\nMenú:")
      print("(1) Añadir un alumno")
      print("(2) Eliminar alumno por NIF")
      print("(3) Actualizar datos de un alumno por NIF")
      print("(4) Mostrar datos de un alumno por NIF")
      print("(5) Mostrar datos de un alumno por Email")
      print("(6) Listar TODOS los alumnos")
      print("(7) Aprobar Alumno por NIF")
      print("(8) Suspender Alumno por NIF")
      print("(9) Mostrar alumnos aprobados")
      print("(10) Mostrar alumnos suspendidos")
      print("(X) Finalizar Programa")

      opcion = input("Seleccione una opción: ").upper()

      if opcion == "1":
          gestor_alumnos.añadir_alumno()
      elif opcion == "2":
          nif = input("Introduce el NIF del alumno a eliminar: ")
          gestor_alumnos.eliminar_alumno(nif)
          print("Lista de alumnos después de eliminar:")
          gestor_alumnos.listar_alumnos()
      elif opcion == "3":
          nif = input("Introduce el NIF del alumno a actualizar: ")
          gestor_alumnos.actualizar_datos(nif)
          print("Lista de alumnos después de actualizar:")
          gestor_alumnos.listar_alumnos()
      elif opcion == "4":
          nif = input("Introduce el NIF del alumno a mostrar: ")
          gestor_alumnos.mostrar_por_nif(nif)
      elif opcion == "5":
          email = input("Introduce el Email del alumno a mostrar: ")
          gestor_alumnos.mostrar_por_email(email)
      elif opcion == "6":
          gestor_alumnos.listar_alumnos()
      elif opcion == "7":
          nif = input("Introduce el NIF del alumno a aprobar: ")
          gestor_alumnos.aprobar_alumno(nif)
          gestor_alumnos.aprobar_alumno(nif)
          print("Lista de alumnos después de aprobar:")
      elif opcion == "8":
          nif = input("Introduce el NIF del alumno a suspender: ")
          gestor_alumnos.suspender_alumno(nif)
          print("Lista de alumnos después de suspender:")
          gestor_alumnos.listar_alumnos()
      elif opcion == "9":
          gestor_alumnos.mostrar_aprobados()
      elif opcion == "10":
          gestor_alumnos.mostrar_suspendidos()
      elif opcion == "X":
          break
      else:
          print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
  main()