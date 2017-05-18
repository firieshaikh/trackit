from random import randint
import json, time
d = {}

with open('sample_file') as f:
	for line in f:
		list = line.split()
		#print(list)
		for l in list:
			key, val = l.split(':')
			d[key] = val
		#print("Dictionary:", d)
		print("JSON:", json.dumps(d))
		time.sleep(randint(0,5))
