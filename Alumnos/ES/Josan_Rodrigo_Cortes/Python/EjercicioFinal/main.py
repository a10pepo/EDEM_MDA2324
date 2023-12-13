""" (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS os alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X """

from alumnos import alumnos
from functions import *

# alumnos=[]
funcion=" "
while funcion != "X":
    
    funcion=(queOpcion())

    # (1) Añadir un alumno OK
    if funcion=="1":
        anyadirAlumno()
        mostrarDatosTodosAlumnos() #Revisar, parece que imprime por duplicado

        funcion=queOpcion()

    # (2) Eliminar alumno por NIF OK
    if funcion=="2":
        eliminarAlumno()
        funcion=queOpcion()

            
  # (3) Actualizar datos de un alumno por NIF
    if funcion=="3":
        actualizarDatosAlumnoPorNIF()
        funcion=queOpcion()
            
    # (4) Mostrar datos de un alumno por nombre
    if funcion=="4":
        mostrarDatosAlumnoPorNombre()
        funcion=queOpcion()
                
    # (5) Mostrar datos de un alumno por Email
    if funcion=="5":
        mostrarDatosAlumnoPorEmail()
        funcion=queOpcion()
            
    # (6) Listar TODOS los alumnos
    if funcion=="6":
        mostrarDatosTodosAlumnos()
        funcion=queOpcion()
            
    # (7) Aprobar Alumno por NIF
    if funcion=="7":
        aprobarAlumnoPorNif()
        funcion=queOpcion()
            
    # (8) Suspender Alumno por NIF
    if funcion=="8":
        suspenderAlumnoPorNif()
        funcion=queOpcion()
            
    # (9) Mostrar alumnos aprobados
    if funcion=="9":
        mostrarAlumnosAprobados()
        funcion=queOpcion()
            
    # (10) Mostrar alumnos suspensos
    if funcion=="10":
        mostrarAlumnosSuspensos()
        funcion=queOpcion()
            
    # (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X  """
