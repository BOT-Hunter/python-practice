#This function will reverse the lines of a text file

import sys

a = open(sys.argv[1])

def reverse(x):
	y = x.read().split("\n")
	y = y[::-1]
	for i in y:
		print(str(i) + "\n")

reverse(a)