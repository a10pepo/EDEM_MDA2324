FROM python:latest

WORKDIR /app

COPY ahorcado.py .
COPY requirements.txt .
COPY palabras.csv .

RUN pip install pandas
RUN pip install -r requirements.txt

CMD [ "python", "ahorcado.py"]
