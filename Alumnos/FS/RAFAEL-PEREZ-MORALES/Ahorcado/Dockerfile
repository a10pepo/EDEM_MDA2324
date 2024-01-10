FROM python:3.8

COPY ahorcado.py .
COPY archivo.csv .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "ahorcado.py" ]