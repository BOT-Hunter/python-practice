#sorting a list of strings based on the length of strings

list1 = ['apple', 'banana', 'cat', 'zebronic', 'cattle', 'hurdang']

def lensort(list):
	list.sort(key = lambda x: len(x))
	print(list)

lensort(list1)