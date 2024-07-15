#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	'''Print x elements of a list.
	my_list: List containing any type of elements.
	x: Number of elements to print.'''
	elements_printed = 0
	try:
		for i in range(x):
			print(my_list[i], end="")
			elements_printed += 1
	except IndexError:
		pass
	print("")
	return elements_printed
