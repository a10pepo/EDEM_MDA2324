FROM python:3.11.5

WORKDIR /

COPY ahorcado.py .
COPY palabras.csv .
COPY requirements.txt .
 
RUN pip install -r requirements.txt


CMD ["python", "ahorcado.py"]
