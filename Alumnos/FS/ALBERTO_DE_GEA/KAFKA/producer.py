import time
from json import dumps
from confluent_kafka import Producer
import re


config = {
    'bootstrap.servers': '127.0.0.1:9092',  
    'client.id': 'python-producer'
}


producer = Producer(config)


topic_kafka = 'ALQUIMISTA'

file1 = open('/Users/albertodegeapla/Documents/GitHub/EDEM_MDA2324/Alumnos/FS/ALBERTO_DE_GEA/KAFKA/el_alquimista_book.txt',encoding="utf8")
Lines = file1.readlines()
 
count = 0

for line in Lines:
    time.sleep(2)
    print( line.strip() + "\n")
    words = re.findall(r"[\w']+|[.,!?;]", line)
    for word in words:
        data_bytes = word  
        key = str(count)
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)  
        producer.flush()
      

if producer.flush() != 0:
    print("Some messages failed to be delivered")