#Unique Elements of a List

list1 = [1, 2, 3, 2, 4, 3, 5, 4, 6, "potato", "banana", "potato", 'Apple', 'baNaNa', 'APPLE']

def unique(list, key):
	b = []
	for x in list:
		x = key(str(x))
		if not x in b:
			b.append(x)
	print(b)

unique(list1, key=lambda s: s.lower())