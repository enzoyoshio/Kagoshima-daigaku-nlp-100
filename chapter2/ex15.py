import sys

if len(sys.argv) < 3:
	print('please provide a input txt file and a number to show first names')
	exit(0)

file_name = sys.argv[1]
n = int(sys.argv[2])

def save_new(cur, i):
	with open(f'file{i}.txt', 'w') as f:
		f.write(cur)

with open(file_name, 'r') as f:

	for i in range(n):
		cur = f.readline()
		
		save_new(cur, i)
