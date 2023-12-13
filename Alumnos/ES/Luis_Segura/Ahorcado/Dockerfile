FROM python:3.12.0

WORKDIR /app

COPY ahorcado.py .
COPY palabras.csv .
COPY requirements.txt .

RUN /bin/sh -c pip install -r requirements.txt

RUN pip install --upgrade pip setuptools

CMD [ "python", "ahorcado.py" ]