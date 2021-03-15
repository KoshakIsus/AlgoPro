import random

line = input()
list_substrings = line.split()

symb = 1

while symb == 1:
	symb = random.choice(list_substrings)
	symb = int(symb)
	if symb % 2 == 0:
		print(symb)
	else:
		symb = 1