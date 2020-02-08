#Unique Elements of a List

list1 = [1, 2, 3, 2, 4, 3, 5, 4, 6, "potato", "banana", "potato"]

def unique(list):
	list = set(list)
	print(list)

unique(list1)