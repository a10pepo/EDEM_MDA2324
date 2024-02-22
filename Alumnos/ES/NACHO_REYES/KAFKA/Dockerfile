FROM python:3.8-slim

WORKDIR /app

COPY producer.py requirements.txt dakar.json ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "producer.py"]