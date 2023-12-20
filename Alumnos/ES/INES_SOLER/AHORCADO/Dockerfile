FROM python:3.12

RUN apt-get update

COPY  requirements.txt /
COPY Palabras.csv /
COPY Ejercicio_Ahorcado.py /

RUN chmod +x /Ejercicio_Ahorcado.py
RUN pip install -r requirements.txt

CMD python Ejercicio_Ahorcado.py