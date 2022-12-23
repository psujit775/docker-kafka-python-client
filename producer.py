from kafka import KafkaProducer
from time import sleep
from json import dumps

# Create a producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: dumps(x).encode('utf-8'))

# Send a message to the "my-topic" topic
for i in range(100):
    producer.send("my-topic", i)
    print("Sending data : {}".format(i))
    sleep(5)
