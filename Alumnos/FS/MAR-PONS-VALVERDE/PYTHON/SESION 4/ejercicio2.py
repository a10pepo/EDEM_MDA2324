#Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv 
#que pueda ser ejecutado desde Visual Studio Code

#para crear un entonorno virtual ultizamos la función python -m venv .venv
# para activar el entorno virtual utilizamos .\.venv\Scripts\Activate
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(debug=True)

