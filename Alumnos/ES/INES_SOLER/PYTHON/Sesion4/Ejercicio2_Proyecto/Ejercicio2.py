'''
Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt 
y un .venv que pueda ser ejecutado desde Visual Studio Code
'''

'''
COMANDOS EN LA TERMINAL
> python3 -m venv .venv
        –> se crea la carpeta .venv

> python 3 --version
3.12.0

> pip3 --version
23.3.1

Cerrar terminal y abrir una nueva. La ruta ahora está dentro de (.venv)

Crear archivo 'requierements.txt' y ejecutar comando:
> pip install -r requirements.txt

Se instalan las dependencias y comprobar que tengo acceso desde el código:
'''
import requests
import pandas

'''
El acceso funciona correctamente.
'''