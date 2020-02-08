#copied and modified

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

def group(list, size):
	list2 = []
	x = 0 
	y = len(list)
	for i in range(x, y, size):
		x = i
		list2.append(list[x : x + size])
	print(list2)

group(list1, 5)