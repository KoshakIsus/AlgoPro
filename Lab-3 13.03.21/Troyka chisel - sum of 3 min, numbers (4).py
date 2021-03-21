line = input().split()
line = list(map(int, line))
summa = 0
num = 3 #  цикл - 3 раза
while num > 0:
	summa += min(line)
	line.remove(min(line))
	num -= 1
print(summa)