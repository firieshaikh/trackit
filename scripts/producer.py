from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.2.11:9092,192.168.2.12:9092")
topic = client.topics[b'firsttopic']

with topic.get_producer(use_rdkafka=True) as producer:
	for i in range(4):
		producer.produce(b'test message: bytes(i)')
