import os



deliverables=["DOCKER","PYTHON","LINUX","NOTEBOOKS","AHORCADO","SQL"]



def check_class(folder_path):
    alumnos={}
    for alumno in os.listdir(folder_path):
        file_path = os.path.join(folder_path, alumno)
        if os.path.isdir(file_path):
            delivs={}
            alumnos[alumno]=delivs
            for element in deliverables:
                #print(file_path+"/"+element)
                if (os.path.exists(file_path+"/"+element) & os.path.isdir(file_path+"/"+element)) or (os.path.exists(file_path+"/"+element.capitalize()) & os.path.isdir(file_path+"/"+element.capitalize())):
                    alumnos[alumno][element]=True    
                else:
                    alumnos[alumno][element]=False
    return alumnos


def generate_table(clase,alumnos):
    
    try:
        table="<table>\n<tr><th>Alumno</th>"
        for element in deliverables:
            table+="\n<th>"+element+"</th>"
        table+="\n</tr>\n"  
        for alumno in sorted(alumnos):
            table+="<tr>\n<td><a href='https://github.com/a10pepo/EDEM_MDA2324/tree/main/Alumnos/"+clase+"/"+alumno+"'>"+str.capitalize(alumno)+"</a></td>"
            for element in deliverables:
                if alumnos[alumno][element]:
                    table+="\n<td>✅</td>"
                else:
                    table+="\n<td>❌</td>"
            table+="\n</tr>\n"
        table+="</table>\n"
    except:
        print("error")
    return table

def modify_readme():
    with open('README.md', 'r') as file:
        data = file.read()
        parts = data.split('### Estado de las entregas')

    with open('README.md', 'w') as file:
        try: 
            file.write(parts[0])
            file.write('### Estado de las entregas\n')
            file.write('Entregas Fin de Semana\n')
            file.write(generate_table("FS",check_class('Alumnos/FS')))
            file.write('\n')
            file.write('\n')
            file.write('Entregas Entre Semana\n')
            file.write(generate_table("ES",check_class('Alumnos/ES')))
            file.write('\n')
        except:
            file.close()
            with open('README.md', 'w') as file_recov:
                file_recov.write(data)
        



if __name__ == '__main__':  
    modify_readme()
    print("README.md updated")

