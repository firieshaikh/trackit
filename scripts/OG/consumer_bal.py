from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.2.11:9092,192.168.2.12:9092")

topic = client.topics[b'firsttopic']

consumer = topic.get_simple_consumer()
balanced_consumer = topic.get_balanced_consumer(consumer_group=b'testgroup', auto_commit_enable=True, zookeeper_connect='192.168.2.11:2181,192.168.2.12:2181')	
for message in consumer:
	if message is not None:
		print(message.offset, message.value)
