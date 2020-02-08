
list1 = [1, 2, 3, 4, "apple", "banana", ["a", "b"]]

def reverse(list):
	a = 1
	b = []
	for x in list:
		b.append(list[-a])
		a += 1
	print(b)

reverse(list1)

#!!!  NOTE !!!
#By the method of Slicing,
#It is as simple as 

list2 = list1[::-1]
print(list2)