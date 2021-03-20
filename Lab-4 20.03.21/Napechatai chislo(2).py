line = list(input())  #введи последовательность чисел
#1 строка
for i in line:
	if i == '1' or i == '6':
		print('.#', end='')
	else:
		print('##', end='')

print()
# 2 строка
for i in line:
	if i == '8':
		print('..', end='')
	if i == '0' or i == '1' or i == '4' or i == '9':
		print('##', end='')
	if i == '2' or i == '3' or i == '7':
		print('.#', end='')
	if i == '5' or i == '6':
		print('#.', end='')

print()
#3 строка
for i in line:
	if i == '0' or i == '6' or i == '8':
		print('##', end='')
	if i == '1' or i == '3' or i == '4' or i == '5' or i == '9':
		print('.#', end='')
	if i == '2' or i == '7':
		print('#.', end='')

print()
#4 строка
for i in line:
	if  i == '2' or i == '3' or i == '5' or i == '6' or i == '8' or i == '0':
		print('##', end='')
	if i == '1' or i == '4':
		print('.#', end='')
	if i == '7' or i == '9':
		print('#.', end ='')