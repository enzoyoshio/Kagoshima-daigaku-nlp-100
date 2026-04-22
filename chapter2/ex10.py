import sys

if len(sys.argv) == 1:
	print('please provide a input txt file')
	exit(0)

file_name = sys.argv[1]

with open(file_name, 'r') as f:
	print(f'File {file_name} has {len(f.readlines())} lines.')
