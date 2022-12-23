from kafka import KafkaConsumer, TopicPartition

# Create a consumer
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                        enable_auto_commit=True,
                        group_id='my-group',
                        auto_offset_reset='earliest')

topic_partition = TopicPartition("my-topic", 0)
consumer.assign([topic_partition])

# Comment below line to read only new messages.
consumer.seek_to_beginning()

for message in consumer:
    print (message.value.decode('utf-8'))
