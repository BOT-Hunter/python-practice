#duplicates in a list

list1 = [1, 2, 3, 2, 4, 3, 5, 4, 6, 'potato', 'banana', 'potato']

def dups(list):
	a = []
	b = []
	for x in list:
		if x in a:
			b.append(x)
		a.append(x)
		
	print(b)

dups(list1)