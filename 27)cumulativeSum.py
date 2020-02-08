list1 = [1, 2, 3, 4]

def cumulative_sum(list):
	y = 0
	a = 0
	b = []
	for x in list:
		y += list[a]
		b.append(y)
		a += 1
	print(b)

cumulative_sum(list1)