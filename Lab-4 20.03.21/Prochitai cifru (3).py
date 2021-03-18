str_1 = input()  # введи строки числа поочереди
str_2 = input()
str_3 = input()
str_4 = input()

def print_num():  # читаем 1 строку
	if str_1 == '##':
		read_str_2()  # 0, 2-5, 7-9
	if str_1 == '.#':
		read_str_2_16()  # 1/6

def read_str_2_16():  # читаем 2 строку и выводим число - 1/6
	if str_2 == '##':
		print('1')  # 1
	if str_2 == '#.':
		print('6')  # 6

def read_str_2():
	if str_2 == '..':
		print('8')  # 8
	if str_2 == '##':
		read_str_3_049()  # 0/4/9
	if str_2 == '#.':
		print('5')  # 5
	if str_2 == '.#':
		read_str_3_237()  # 2/3/7

def read_str_3_049():
	if str_3 == '##':
		print('0')  # 0
	if str_3 == '.#':
		read_str_4_49()  # 4/9

def read_str_3_237():
	if str_3 == '.#':
		print('3')  # 3
	if str_3 == '#.':
		read_str_4_27()  # 2/7

def read_str_4_27():
	if str_4 == '##':
		print('2')  # 2
	if str_4 == '#.':
		print('7')  # 7

def read_str_4_49():
	if str_4 == '.#':
		print('4')  # 4
	if str_4 == '#.':
		print('9')  # 9
	
print_num()