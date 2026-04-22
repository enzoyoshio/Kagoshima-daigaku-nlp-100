import json

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
	
	all = f.readlines()

	content = ""
	for line in all:
		data = json.loads(line)
		if data['title'] == 'イギリス':
			content = data['text']	

	content = content.split('\n')

	for line in content:
		if 'ファイル' in line.lower():
			print(line)
