FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY AHORCADO.py .
COPY PALABRAS.csv .

RUN pip install -r requirements.txt

CMD ["python", "AHORCADO.py"]



