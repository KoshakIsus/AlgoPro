line_1 = list(input()) #  1 строка
line_2 = list(input()) #  2 строка
line_3 = list(input()) #  3
line_4 = list(input()) #  4
a = 0 #  ограничение в проверке. Нужно, т.к. все циклы читают строки с самого начала, из-за этого
#  комп принтит совершенно не нужные числа. Чтобы это ограничить, добавляе эту переменную
#  и ограничиваем работу цикла так, что должно быть i == a, а "a" увеличиваем
#  на 2 после каждого принта, чтобы первые 2 элемента каждой строки больше не проверялись!

# global a - чтобы эта переменная была "глобальная" а не "локальная" и могла изменяться.

#  Проверка 2 строку
def read_line_2_16(): #  Проверка на схожесть 1 или 6
	global a
	for i in range(0, len(line_2), 2):
		if i == a:
			if line_2[i] == '#' and line_2[i+1] == '#':
				print('1', end='')
			if line_2[i] == '#' and line_2[i+1] == '.':
				print('6', end='')

def read_line_2(): #  Проверка на схожесть 0 2-5 7-9
	global a
	for i in range(0, len(line_2), 2):
		if i == a:
			if line_2[i] == '#' and line_2[i+1] == '#':
				read_line_3_049()
			if line_2[i] == '.' and line_2[i+1] == '.':
				print('8', end='')
			if line_2[i] == '.' and line_2[i+1] == '#':
				read_line_3_237()
			if line_2[i] == '#' and line_2[i+1] == '.':
				print('5', end='')

#  Проверка 3 строки
def read_line_3_049():
	global a
	for i in range(0, len(line_3), 2):
		if i == a:
			if line_3[i] == '#' and line_3[i+1] == '#':
				print('0', end='')
			if line_3[i] == '.' and line_3[i+1] == '#':
				read_line_4_49()

def read_line_3_237():
	global a
	for i in range(0, len(line_3), 2):
		if i == a:
			if line_3[i] == '.' and line_3[i+1] == '#':
				print('3', end='')
			if line_3[i] == '#' and line_3[i+1] == '.':
				read_line_4_27()

#  Проверка 4 строки
def read_line_4_49():
	global a
	for i in range(0, len(line_4), 2):
		if i == a:
			if line_4[i] == '.' and line_4[i+1] == '#':
				print('4', end='')
			if line_4[i] == '#' and line_4[i+1] == '.':
				print('9', end='')

def read_line_4_27():
	global a
	for i in range(0, len(line_4), 2):
		if i == a:
			if line_4[i] == '#' and line_4[i+1] == '#':
				print('2', end='')
			if line_4[i] == '#' and line_4[i+1] == '.':
				print('7', end='')

#  Проверка 1 строки
for i in range(0, len(line_1), 2): #  Проверка всех пар символов (по 2, а не так, что проверится один и тот же символ в разных парах!)
#  if i == a:
	if line_1[i] == '#' and line_1[i+1] == '#':
		read_line_2() #  0 2-5 7-9
	if line_1[i] == '.' and line_1[i+1] == '#':
		read_line_2_16() #  либо 1, либо 6
	a += 2