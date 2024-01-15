FROM python:3.11.5

COPY ahorcado.py ./
COPY palabras.txt ./
COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD ["python3", "ahorcado.py"]

