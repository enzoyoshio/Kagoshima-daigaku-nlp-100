import sys

if len(sys.argv) < 3:
	print('please provide a input txt file and a number to show first names')
	exit(0)

file_name = sys.argv[1]
n = int(sys.argv[2])

with open(file_name, 'r') as f:
	for i in range(n):
		print(f.readline().replace('\t',' '), end='')
