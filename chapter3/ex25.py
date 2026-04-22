import json

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
	
	all = f.readlines()

	content = ""
	for line in all:
		data = json.loads(line)
		if data['title'] == 'イギリス':
			content = data['text']	

	content = content.split('\n')

	flag = False
	for line in content:
		if line.startswith('{{基礎情報'):
			flag = True
		
		
		if flag:
			print(line)
		

		if line.startswith('}}'): flag = False
