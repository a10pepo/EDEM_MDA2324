#REQUERIMIENTOS
from PF_preparation import nuevo_alumno
from PF_preparation import mostrar_total_alumnos
from PF_preparation import eliminar_alumno
from PF_preparation import actualizar_alumno
from PF_preparation import mostrar_datos_alumno_nif
from PF_preparation import mostrar_datos_alumno_email
from PF_preparation import aprobar_alumno_por_nif
from PF_preparation import suspender_alumno_por_nif
from PF_preparation import mostrar_alumnos_aprobados
from PF_preparation import mostrar_alumnos_suspendidos

#CÓDIGO MOSTRAR OPCIONES EN TEMRINAL
while True:
    opcion_consola=input("\n ¿Qué deseas hacer?""\n\n" "1 - Añadir un alumno""\n\n""2 - Eliminar alumno por NIF""\n\n" "3 - Actualizar datos alumno por NIF""\n\n" "4 - Mostrar Datos Alumno por NIF""\n\n" "5 - Mostrar datos de un alumno por Email""\n\n""6 - Listar TODOS los alumnos""\n\n""7 - Aprobar alumno por NIF""\n\n""8 - Suspender alumno por NIF""\n\n""9 - Mostrar alumnos aprobados""\n\n""10 - Mostrar alumnos suspendidos""\n\n" "X - Finalizar programa""\n\n" "Escribe aquí tu opción :")
    if opcion_consola == "1":
        nuevo_alumno()
    elif opcion_consola == "2":
        eliminar_alumno()
    elif opcion_consola == "3":
        actualizar_alumno()
    elif opcion_consola == "4":
        mostrar_datos_alumno_nif()
    elif opcion_consola == "5":
        mostrar_datos_alumno_email()
    elif opcion_consola == "6":
        mostrar_total_alumnos()
    elif opcion_consola == "7":
        aprobar_alumno_por_nif()
    elif opcion_consola == "8":
        suspender_alumno_por_nif()
    elif opcion_consola == "9":
        mostrar_alumnos_aprobados()
    elif opcion_consola == "10":
        mostrar_alumnos_suspendidos()
    elif opcion_consola == "X":
        print("\n\n" "Progama Cerrado\n")
        break