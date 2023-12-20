from alumnos import alumnos
# alumnos=[]

def queOpcion():
        opcion=input("""
        BIENVENIDO A LA BASE DE DATOS DE ALUMNOS, QUE DESEA HACER, MARQUE LA OPCIÓN ELEGIDA:
        (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
        (2) Eliminar alumno por NIF
        (3) Actualizar datos de un alumno por NIF
        (4) Mostrar datos de un alumno por NIF
        (5) Mostrar datos de un alumno por Email
        (6) Listar TODOS os alumnos
        (7) Aprobar Alumno por NIF
        (8) Suspender Alumno por NIF
        (9) Mostrar alumnos aprobados
        (10) Mostrar alumnos suspensos
        (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X:  """
        )
        return opcion
#(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno

def anyadirAlumno():
    nuevoAlumno={}
    nuevoAlumnoNombre=input("Introduce el nombre del nuevo alumno: ")
    nuevoAlumnoApellido1=input("Introduce el primer apellido del alumno: ")
    nuevoAlumnoApellido2=input("Introduce el segundo apellido del alumno: ")
    nuevoAlumnoNIF=input("Introduce el NIF del alumno")
    nuevoAlumnoEmail=input("Introduce el email del alumno")

    nuevoAlumno.setdefault("Nombre"," ")
    nuevoAlumno.setdefault("Apellido1", " ")
    nuevoAlumno.setdefault("Apellido2"," ")
    nuevoAlumno.setdefault("NIF"," ")
    nuevoAlumno.setdefault("Email"," ")
    nuevoAlumno.setdefault("Calificacion"," ")

    nuevoAlumno["Nombre"]=nuevoAlumnoNombre
    nuevoAlumno["Apellido1"]=nuevoAlumnoApellido1    
    nuevoAlumno["Apellido2"]=nuevoAlumnoApellido2
    nuevoAlumno["NIF"]=nuevoAlumnoNIF
    nuevoAlumno["Email"]=nuevoAlumnoEmail
    alumnos.append(nuevoAlumno)
    return


# (2) Eliminar alumno por NIF        

def eliminarAlumno():
    queCampoImprimir(nif=True)
    nif=input("Introduce el NIF del alumno a elminar; ")
    for alumno in alumnos:
         if alumno["NIF"]==nif:
              alumnos.remove(alumno)


# (3) Actualizar datos de un alumno por NIF,
def actualizarDatosAlumnoPorNIF():
    queCampoImprimir(nif=True)
    nif=input("Introduce el NIF del alumno a actualizar; ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            alumno["Nombre"]=input("Introduce el nombre a actualizar: ")
            alumno["Apellido1"]=input("Introduce el primer apellido a actualizar: ")
            alumno["Apellido2"]=input("Introduce el  segundo apellido actualizar: ")
            alumno["Email"]=input("Introduce el email actualizar: ")
    return


# (4) Mostrar datos de un alumno por NIF
def mostrarDatosAlumnoPorNombre():
    queCampoImprimir(nif=True)
    niffuncion=input("Introduce el Nif del alumno a mostrar; ")
    for alumno in alumnos:
        nombreAlumno=alumno["Nombre"]
        apellido1Alumno=alumno["Apellido1"]
        apellido2Alumno=alumno["Apellido2"]
        nifAlumno=alumno["NIF"]
        emailAlumno=alumno["Email"]
        calificacionAlumno=alumno["Calificacion"]
        if nifAlumno==niffuncion:
            print(f"""
                        Estos son los datos del alumno seleccionado:
                        Nombre: {nombreAlumno},
                        Primer apellido: {apellido1Alumno}, 
                        Segundo apellido: {apellido2Alumno},
                        NIF: {nifAlumno},
                        Email: {emailAlumno} y
                        Calificacion: {calificacionAlumno}
                        """)
   
# (5) Mostrar datos de un alumno por Email

def mostrarDatosAlumnoPorEmail():
    queCampoImprimir(email=True)
    email=input("Introduce el email del alumno a mostrar: ")
    for alumno in alumnos:
        nombre=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if email==alumno["Email"]:
            print(f"""
                        Estos son los datos del alumno seleccionado:
                        Nombre: {nombre},
                        Primer apellido: {apellido1}, 
                        Segundo apellido: {apellido2},
                        NIF: {nif},
                        Email: {email} y
                        Calificacion: {calificacion}
                        """)
         
# (6) Listar TODOS los alumnos

def mostrarDatosTodosAlumnos():
    i=0
    for alumno in alumnos:
        i+=1
        nombreAlumno=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if calificacion==True or calificacion==False:

            print(f'''
{i} {nombreAlumno} {apellido1} {apellido2}, NIF {nif}, {email} y calificación {calificacion}''')
        else:
            print(f'''
{i} {nombreAlumno} {apellido1} {apellido2}, NIF {nif}, {email} y calificación (pendiente de calificar)''')
            


# (7) Aprobar Alumno por NIF

def aprobarAlumnoPorNif():
    queCampoImprimir(nif=True)
    nif=input("Introduce el NIF del alumno que deseas aprobar: ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            aprobado=input("Esta aprobado el alumno: (Si/No)")
            if aprobado=="Si":
                alumno["Calificacion"]=True
            else:
               alumno["Calificacion"]=False
        
# (8) Suspender Alumno por NIF

def suspenderAlumnoPorNif():
    queCampoImprimir(nif=True)
    nif=input("Introduce el NIF del alumno que deseas suspender: ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            suspenso=input("Esta suspenso el alumno: (Si/No) ")
            if suspenso=="No":
                alumno["Calificacion"]=False
            else:
               alumno["Calificacion"]=True
        
# (9) Mostrar alumnos aprobados

def mostrarAlumnosAprobados():

    i=0
    for alumno in alumnos:
        i+=1
        nombreAlumno=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if calificacion==True:

            print(f'''
{i} El alumno {nombreAlumno} {apellido1} {apellido2},con NIF {nif} y correo {email} esta aprobado''')
        
        
# (10) Mostrar alumnos suspensos
def mostrarAlumnosSuspensos():
    i=0
    for alumno in alumnos:
        i+=1
        nombreAlumno=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if calificacion==False:

            print(f'''
{i} El alumno {nombreAlumno} {apellido1} {apellido2},con NIF {nif} y correo {email} esta suspendido''')
        
# (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X """


# Defino esta función para que me muestre los campos que quiero según la funcionalidad.
 
def queCampoImprimir(nombre=False,Apellido1=False,Apellido2=False,email=False,nif=False,calficacion=False):
    for alumno in alumnos:
    
        alumnoNombre=alumno["Nombre"]
        alumnoApellido1=alumno["Apellido1"]
        alumnoApellido2=alumno["Apellido2"]
        alumnoEmail=alumno["Email"]
        alumnoNif=alumno["NIF"]
        alumnoCalificacion=alumno["Calificacion"]
    
        if nombre==True and Apellido1==True and Apellido2==True:

            print(f"{alumnoNombre} {alumnoApellido1} {alumnoApellido2}")

        elif email==True:             
            print(f" {alumnoEmail}")
        elif nif==True:               
            print(f"{alumnoNombre} {alumnoApellido1}, {alumnoNif}")
        elif calficacion==True:               
            print(f"{alumnoNombre} {alumnoApellido1} {alumnoApellido2}, {alumnoCalificacion}")
