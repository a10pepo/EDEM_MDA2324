# RETO 11

clientes = {}

def clientes_pred():
    global clientes
    with open('clientes_pred.json', 'r') as file:
        clientes = json.load(file)
    return clientes

def añadir_cliente():
  NIF = str(input('Introduce el NIF del cliente'))
  nombre = str(input('Introduce el nombre del cliente'))
  apellidos = str(input('Introduce los apellidos del cliente'))
  teléfono = str(input('Introduce el teléfono del cliente'))
  email = str(input('Introduce el email del cliente'))
  preferente = bool(input('Introduce si el cliente es preferente o no, (true/false)'))

  clientes[NIF] = {
      'NIF': NIF,
      'Nombre': nombre,
      'Apellidos': apellidos,
      'Telefono': teléfono,
      'Emeail': email,
      'Preferente': preferente

  }

def eliminar_cliente(valor):
  NIF = str(valor)
  del(clientes[NIF])
  print(clientes)
  print(f'El cliente eliminado era el que poseía este NIF: {NIF}')


def mostrar_cliente_nif(valor):
  NIF = str(valor)
  print(f"El cliente seleccionado es el que posee este NIF: {NIF}")
  print(f"El nombre del cliente seleccionado es: {clientes[NIF]['Nombre']}")
  print(f"Los apellidos del cliente seleccionado son: {clientes[NIF]['Apellidos']}")
  print(f"El telefono del cliente seleccionado es: {clientes[NIF]['Telefono']}")
  print(f"El email del cliente seleccionado es: {clientes[NIF]['Email']}")
  print(f"¿El cliente es preferente?: {clientes[NIF]['Preferente']}")

def listar_clientes():
  for i in clientes.values():
    for x, y in i.items():
      print(f"{x}: {y}")
    print("////////")

def mostrar_preferentes():
  for i in clientes.values():
    if i['Preferente'] == True:
      for x, y in i.items():
        print(f"{x}: {y}")
      print("////////")

while True: 
  print(""" PROGRAMA CARGADO
////////////////////////
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar datos de un cliente por NIF
(4) Listar TODOS los clientes
(5) Mostrar clientes preferentes
(6) Finalizar Programa
////////////////////////
""")

  eleccion = input('Selecciona el número que desees')
  if eleccion == '1':
    añadir_cliente()
  elif eleccion == '2':
    valor = str(input('Selecciona el NIF del cliente que quieres eliminar'))
    eliminar_cliente(valor)
  elif eleccion == '3':
    valor = str(input('Selecciona el NIF del cliente que quieres mostrar'))
    mostrar_cliente_nif(valor)
  elif eleccion == '4':
    listar_clientes()
  elif eleccion == '5':
    mostrar_preferentes()
  elif eleccion == '6':
    break
  else:
    print('Introduzca una opción correcta')