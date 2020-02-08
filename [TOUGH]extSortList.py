#[TOUGH]Sorting the list based on extension

list1 = ['a.b', 'b.c', 'c.d', 'd.a']

def extsort(list):
	print(list)
	x = 0
	for i in list:
		list[x] = i.split('.')
		x += 1
	print(list)

	list.sort(key = lambda x: x[1])
	print(list)

	x = 0
	for j in list:
		list[x] = '.'.join(j)
		x += 1
		
	print(list)

extsort(list1)