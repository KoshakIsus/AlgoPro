nums = list(map(int, input().split()))
y_size = nums[0]  # кол-во строк, т.е. длина вертикали
x_size = nums[1]  # кол-во столбцов, т.е. длина горизонтали
tab = [[0] * x_size for _ in range(y_size)]

index = 0; x = 1; y = -1

while True:
	while x > 0 and y < y_size -1:
		y += 1; x -= 1
		index += 1; tab[y][x] = index
	if x == 0 and y < y_size - 1:
		y += 1  # вправо если дошли до верхней границы 
	else:
		if y == y_size - 1 and x == x_size - 1:
			break
		else:
			x += 1  #вниз если дошли до правой границы
	index += 1; tab[y][x] = index

	if x == x_size -1 and y == y_size -1:
		break

	while y > 0 and x < x_size - 1:
		y -= 1; x += 1
		index += 1; tab[y][x] = index
	if y == 0 and x < x_size - 1:
		x += 1
	else:
		if y == y_size - 1 and x == x_size - 1:
			break
		else:
			y += 1
	index += 1; tab[y][x] = index

for line in tab:
	print(' '.join(map(str, line)))
