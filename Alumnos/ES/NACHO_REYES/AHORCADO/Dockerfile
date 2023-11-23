FROM python:3.12

RUN python -m pip install --upgrade pip
RUN pip install pandas 

COPY ahorcado.py /app/ahorcado.py

WORKDIR /app

CMD ["python", "ahorcado.py"]