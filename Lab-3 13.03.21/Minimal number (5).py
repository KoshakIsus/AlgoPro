N = int(input()) #  Введи кол-во чисел, которые хочешь ввести (до 999)
a = 0  #  Хотя бы дно число должно оканчиваться на "3"
line = [] #  Программа выведет минимальное число, оканчивающееся на 3
line_check = []
for a in range(N):
	a = int(input())
	line.append(a)
	a = 0
for item in line:
	if item % 10 == 3:
		line_check.append(item)
line_check = list(map(int, line_check))
print(min(line_check))