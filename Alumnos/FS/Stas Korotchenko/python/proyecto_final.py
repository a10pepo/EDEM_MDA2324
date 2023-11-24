# Enunciado Proyecto FInal

# Una empresa de formación quiere gestionar su cartera de alumnos.

# Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

#     NIF (string)
#     Nombre (string)
#     Apellidos (string)
#     Teléfono (string)
#     Email (string)
#     Aprobado (boolean)

# El programa debe mostrar las siguientes opciones por consola para que escoja el usuario:

# (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
# (2) Eliminar alumno por NIF
# (3) Actualizar datos de un alumno por NIF
# (4) Mostrar datos de un alumno por NIF
# (5) Mostrar datos de un alumno por Email
# (6) Listar TODOS os alumnos
# (7) Aprobar Alumno por NIF
# (8) Suspender Alumno por NIF
# (9) Mostrar alumnos aprobados
# (10) Mostrar alumnos suspensos
# (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X


import pandas as pd


df = pd.DataFrame({'NIF': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
                'Nombre': ['Alma', 'Astra', 'Ben', 'Bred', 'Carla', 'Cristy'],
                'Apellidos': ['Martinez', 'Nupa', 'Aflek', 'Pitt', 'Madison', 'Misty'],
                'Teléfono': ['123', '345', '678', '987', '654', '321'],
                'Email': ['alma@gmail.com', 'astra@gmail.com', 'ben@gmail.com', 'bred@gmail.com', 'carla@gmail.com', 'cristy@gmail.com'],
                'Aprobado': ['SI', 'NO', 'NO', 'NO', 'NO', 'SI']})






# (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
def añadir_alumno():
    nif: str = input('Añade NIF: ')
    nombre: str = input('Añade nombre: ')
    appellido: str = input('Añade appellido: ')
    telefono: str = input('Añade teléfono: ')
    email: str = input('Añade email: ')
    aprobado: str = input('Añade aprobado o no, introduce SI o NO: ')
    df.loc[ len(df.index)] = [nif, nombre, appellido,telefono, email, aprobado]
    print(df)
    

# (2) Eliminar alumno por NIF
def Eliminar_por_NIF(df):
    nif_para_eliminar = input('Ingresa NIF: ')
    df = df.loc[df['NIF'] != nif_para_eliminar]
    print(df)
    
# (3) Actualizar datos de un alumno por NIF
def Actualizar_por_NIF():
    actualizar_por_nif = input('Ingresa NIF: ')
    que = input('Que quiere actualizar:\
                \n(1) Nombre\
                \n(2) Apellido\
                \n(3) Teléfono\
                \n(4) Email\
                \nIngresa número: ')
    if que == '1':
        nuevo_nombre = input('Nuevo nombre: ')
        df['Nombre'].where(~(actualizar_por_nif == df.NIF),
                           other=nuevo_nombre, inplace=True)
    elif que == '2':
        nuevo_apellido = input('Nuevo apellido: ')
        df['Apellidos'].where(~(actualizar_por_nif == df.NIF),
                              other=nuevo_apellido, inplace=True)
    elif que == '3':
        nuevo_teléfono = input('Nuevo teléfono: ')
        df['Teléfono'].where(~(actualizar_por_nif == df.NIF),
                             other=nuevo_teléfono, inplace=True)
    elif que == '4':
        nuevo_email = input('Nuevo email: ')
        df['Email'].where(~(actualizar_por_nif == df.NIF),
                          other=nuevo_email, inplace=True)
    print(df)


#(4) Mostrar datos de un alumno por NIF
def Mostrar_datos_por_NIF():
    mostrar_por_nif = input('Ingresa NIF: ')
    print(df.loc[df['NIF'] == mostrar_por_nif])

# (5) Mostrar datos de un alumno por Email
def Mostrar_datos_por_Email():
    mostrar_por_email = input('Ingresa Email: ')
    print(df.loc[df['Email'] == mostrar_por_email])

# (6) Listar TODOS os alumnos
def Listar_TODOS_los_alumnos():
    print(df)

# (7) Aprobar Alumno por NIF
def Aprobar_Alumno_por_NIF():
    aprobar_por_nif = input('Ingresa NIF: ')
    df['Aprobado'].where(~(aprobar_por_nif == df.NIF), other=True, inplace=True)
    print(df)

# 8) Suspender Alumno por NIF
def Suspender_Alumno_por_NIF():
    suspender_por_nif = input('Ingresa NIF: ')
    df['Aprobado'].where(~(suspender_por_nif == df.NIF), other=False, inplace=True)
    print(df)

# (9) Mostrar alumnos aprobados  
def Mostrar_alumnos_aprobados():
    print(df.loc[df['Aprobado']== 'SI'])

# (10) Mostrar alumnos suspensos  
def Mostrar_alumnos_suspensos():
    print(df.loc[df['Aprobado'] == 'NO'])


while True:
    escoja_opcion = input('Escoja_opcion:\
                        \n(1) Añadir un alumno\
                        \n(2) Eliminar alumno por NIF\
                        \n(3) Actualizar datos de un alumno por NIF\
                        \n(4) Mostrar datos de un alumno por NIF\
                        \n(5) Mostrar datos de un alumno por Email\
                        \n(6) Listar TODOS os alumnos\
                        \n(7) Aprobar Alumno por NIF\
                        \n(8) Suspender Alumno por NIF\
                        \n(9) Mostrar alumnos aprobados\
                        \n(10) Mostrar alumnos suspensos\
                        \n(X) Finalizar Programa\
                        \nEntre numero: ')



    if escoja_opcion == 'x':
            break
    elif int(escoja_opcion) == 1:
            añadir_alumno()
    elif int(escoja_opcion) == 2:
            Eliminar_por_NIF(df)
    elif int(escoja_opcion) == 3:
            Actualizar_por_NIF()
    elif int(escoja_opcion) == 4:
            Mostrar_datos_por_NIF()
    elif int(escoja_opcion) == 5:
            Mostrar_datos_por_Email()
    elif int(escoja_opcion) == 6:
            Listar_TODOS_los_alumnos()
    elif int(escoja_opcion) == 7:
            Aprobar_Alumno_por_NIF()    
    elif int(escoja_opcion) == 8:
            Suspender_Alumno_por_NIF()
    elif int(escoja_opcion) == 9:
            Mostrar_alumnos_aprobados()
    elif int(escoja_opcion) == 10:
            Mostrar_alumnos_suspensos()


    

    
           