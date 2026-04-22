import json

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
	
	all = f.readlines()

	for line in all:
		data = json.loads(line)
		if data['title'] == 'イギリス':
			print(data['text'])

