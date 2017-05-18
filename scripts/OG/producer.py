from pykafka import KafkaClient
from random import randint
import json, time

client = KafkaClient(hosts="192.168.2.11:9092,192.168.2.12:9092")

topic = client.topics[b'firsttopic']

with topic.get_sync_producer(use_rdkafka=True) as producer:
	d = {}
	for i in range(5):
		with open('sample_file') as f:
			for line in f:
				list = line.split()
				for l in list:
					key, val = l.split(':')
					d[key] = val
				mesg = json.dumps(d).encode()
				producer.produce(mesg)
				#time.sleep(randint(0,5))
