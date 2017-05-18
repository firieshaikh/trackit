from pykafka import KafkaClient,rdkafka
from random import randint
import json, time

client = KafkaClient(hosts="192.168.2.11:9092,192.168.2.12:9092")

topic = client.topics[b'firsttopic']

with topic.get_producer(delivery_reports=True) as producer:
    count = 0
    while True:
        count += 1
        count_byte = bytes(count)
        producer.produce('test msg'.encode(), partition_key='{}'.format(count_byte).encode())
        if (count%10)**5 == 0:  # adjust this or bring lots of RAM ;)
            while True:
                try:
                    msg, exc = producer.get_delivery_report(block=True,timeout=60)
                    if exc is not None:
                        print('Failed to deliver msg {}: {}'.format(msg.partition_key, repr(exc)))
                    else:
                        print('Successfully delivered msg {}'.format(msg))
                except(queue.Empty):
                    break
