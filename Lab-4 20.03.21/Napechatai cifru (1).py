num = int(input()) #введи 0-9, напечатается в виде символов.and
s_1 = '##' #s = symbol
s_2 = '.#'
s_3 = '#.'
s_4 = '..'

def print_num():
	if num == 0:
		print(('\n' + s_1)*4)
	if num == 1:
		print('\n' + s_2 + '\n' + s_1 + ('\n'+s_2)*2)
	if num == 2:
		print('\n' + s_1 + '\n' + s_2 + '\n' + s_3 + '\n' + s_1)
	if num == 3:
		print('\n' + s_1 + ('\n' + s_2)*2 + '\n' + s_1)
	if num == 4:
		print(('\n' + s_1)*2 + ('\n' + s_2)*2)
	if num == 5:
		print('\n' + s_1 + '\n' + s_3 + '\n' + s_2 + '\n' + s_1)
	if num == 6:
		print('\n' + s_2 + '\n' + s_3 + ('\n' + s_1)*2)
	if num == 7:
		print('\n' +s_1 + '\n' + s_2 + '\n' + s_3 + '\n' + s_3)
	if num == 8:
		print('\n' + s_1 + '\n' + s_4 + ('\n' + s_1)*2)
	if num == 9:
		print(('\n' + s_1)*2 + '\n' + s_2 + '\n' + s_3)

print_num()