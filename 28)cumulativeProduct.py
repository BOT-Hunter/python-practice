#cumulative_product

list1 = [1, 2, 3, 4]
list2 = list1[::-1]

def cumulative_product(list):
	a = 0
	y = 1
	b = []
	for x in list:
		y *= list[a]
		b.append(y)
		a += 1
	print(b)

cumulative_product(list2)