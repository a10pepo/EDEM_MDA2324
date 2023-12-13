FROM python

WORKDIR /app

COPY ahorcado.py /app
COPY requirements.txt /app
COPY palabras.csv /app

RUN pip install -r requirements.txt

CMD ["python", "ahorcado.py"]




