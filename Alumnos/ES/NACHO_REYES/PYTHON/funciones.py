import json
alumnos = {}

def alumnos_pred():
    global alumnos
    with open('alumnos_pred.json', 'r') as file:
        alumnos = json.load(file)
    return alumnos

def guardar_alumno():
    with open('alumnos_pred.json', 'w') as file:
        json.dump(alumnos, file, indent=2)

def añadir_alumno():
  NIF = str(input('Introduce el NIF del alumno'))
  nombre = str(input('Introduce el nombre del alumno'))
  apellidos = str(input('Introduce los apellidos del alumno'))
  teléfono = str(input('Introduce el teléfono del alumno'))
  email = str(input('Introduce el email del alumno'))
  aprobado = bool(input('Introduce si el alumno está o no aprobado, (true/false)'))

  alumnos[NIF] = {
      'NIF': NIF,
      'Nombre': nombre,
      'Apellidos': apellidos,
      'Telefono': teléfono,
      'Emeail': email,
      'Aprobado': aprobado

  }

def eliminar_alumno(valor):
  NIF = str(valor)
  del(alumnos[NIF])
  print(alumnos)
  print(f'El alumno eliminado era el que poseía este NIF: {NIF}')


def actualizar_alumno(valor):
  NIF = str(valor)
  nombre = str(input('Introduce el nuevo nombre del alumno'))
  apellidos = str(input('Introduce los nuevos apellidos del alumno'))
  teléfono = str(input('Introduce el nuevo teléfono del alumno'))
  email = str(input('Introduce el nuevo email del alumno'))
  aprobado = bool(input('Introduce si el alumno está o no aprobado, (true/false)'))

  alumnos[NIF] = {
      'NIF': NIF,
      'Nombre': nombre,
      'Apellidos': apellidos,
      'Telefono': teléfono,
      'Email': email,
      'Aprobado': aprobado

  }


def mostrar_alumno_nif(valor):
  NIF = str(valor)
  print(f"El alumno seleccionado es el que posee este NIF: {NIF}")
  print(f"El nombre del alumno seleccionado es: {alumnos[NIF]['Nombre']}")
  print(f"Los apellidos del alumno seleccionado son: {alumnos[NIF]['Apellidos']}")
  print(f"El telefono del alumno seleccionado es: {alumnos[NIF]['Telefono']}")
  print(f"El email del alumno seleccionado es: {alumnos[NIF]['Email']}")
  print(f"¿El alumno esta aprobado?: {alumnos[NIF]['Aprobado']}")

def mostrar_alumno_email(valor):
  email = str(valor)
  for alumno in alumnos.values():
    if alumno['Email'] == email:
      print(f"El alumno seleccionado es el que posee este NIF: {alumno['NIF']}")
      print(f"El nombre del alumno seleccionado es: {alumno['Nombre']}")
      print(f"Los apellidos del alumno seleccionado son: {alumno['Apellidos']}")
      print(f"El telefono del alumno seleccionado es: {alumno['Telefono']}")
      print(f"El email del alumno seleccionado es: {email}")
      print(f"¿El alumno esta aprobado?: {alumno['Aprobado']}")
      break

def listar_alumnos():
  for i in alumnos.values():
    for x, y in i.items():
      print(f"{x}: {y}")
    print("////////")

def aprobar_alumno(valor):
  NIF = str(valor)
  if alumnos[NIF]['Aprobado'] == True:
    print('El alumno ya estaba aprobado')
  else:
    ap = str(input(f'¿Quieres aprobar al alumno con el siguiente NIF (si/no): {alumnos[NIF]["NIF"]}'))
    if ap == 'si':
      alumnos[NIF]['Aprobado'] = True
      print('El alumno ha sido aprobado con exito')
      print(f"¿El alumno esta aprobado?: {alumnos[NIF]['Aprobado']}")
    else:
      print('El alumno no ha sido aprobado')

def suspender_alumno(valor):
  NIF = str(valor)
  if alumnos[NIF]['Aprobado'] == False:
    print('El alumno ya estaba suspendido')
  else:
    ap = str(input(f'¿Quieres suspender al alumno con el siguiente NIF (si/no): {alumnos[NIF]["NIF"]}'))
    if ap == 'si':
      alumnos[NIF]['Aprobado'] = False
      print('El alumno ha sido supendido con exito')
      print(f"¿El alumno esta aprobado?: {alumnos[NIF]['Aprobado']}")
    else:
      print('El alumno no ha sido supendido')

def mostrar_aprobados():
  for i in alumnos.values():
    if i['Aprobado'] == True:
      for x, y in i.items():
        print(f"{x}: {y}")
      print("////////")

def mostrar_suspendidos():
  for i in alumnos.values():
    if i['Aprobado'] == False:
      for x, y in i.items():
        print(f"{x}: {y}")
      print("////////")
