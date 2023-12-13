FROM python:3.12

RUN apt-get update

COPY Ejercicio_ahorcado.py /
COPY Palabras.csv /
COPY requirements.txt /

RUN pip install -r requirements.txt

CMD python /Ejercicio_ahorcado.py
