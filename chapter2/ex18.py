import sys

if len(sys.argv) == 1:
	print('please provide a input txt file')
	exit(0)

file_name = sys.argv[1]

mp = {}
with open(file_name, 'r') as f:
	
	for l in f.readlines():
		l = l[0]
		if l not in mp:
			mp[l] = 1
		else: mp[l] += 1
	
answer = []
[answer.append((data, key)) for key, data in mp.items()]

answer.sort()
answer.reverse()

for frequency, char in answer:
	print(f'Letter {char} appears {frequency} times')
