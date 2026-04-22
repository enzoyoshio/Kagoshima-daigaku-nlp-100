import json
import re

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
	
	all = f.readlines()

	content = ""
	for line in all:
		data = json.loads(line)
		if data['title'] == 'イギリス':
			content = data['text']	
#			print(data['text'])

	content = content.split('\n')

	for line in content:
		if 'category' in line.lower():
			match = re.search(r'category:([^\]|]+)', line.lower())		
			if match:
				print(match.group(1))
