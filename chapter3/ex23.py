import json

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
	
	all = f.readlines()

	content = ""
	for line in all:
		data = json.loads(line)
		if data['title'] == 'イギリス':
			content = data['text']	

	content = content.split('\n')

	titles = []
	for line in content:
		if '==' in line.lower():
			titles.append((line.count("=")//2 - 1, line))

	titles.sort()
	for (level, line) in titles:
		print(f'=> this title is level {level} ::: ' + line)
