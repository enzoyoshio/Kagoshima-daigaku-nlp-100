import sys

if len(sys.argv) == 1:
	print('please provide a input txt file')
	exit(0)

file_name = sys.argv[1]

s = set()
with open(file_name, 'r') as f:
	[s.add(l[0]) for l in f.readlines()]

s = list(s)
s.sort()
print('\n'.join(s))
