FROM python:3.11.6

WORKDIR /app

COPY ahorcado.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt
RUN pip install pandas 

CMD ["python","ahorcado.py"]


