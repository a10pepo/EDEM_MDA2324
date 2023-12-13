FROM python:3.11.6

WORKDIR /app

COPY main.py /app
COPY requirements.txt /app
COPY palabras.csv /app
COPY 0_palabras_todas_no_conjugaciones.txt /app


RUN pip install -r requirements.txt 

CMD ["python", "main.py"]
