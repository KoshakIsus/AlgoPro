size = int(input())

tab = [[0] * size for _ in range(size)]

index = 0; x = -1; y = 1

while True:
	while y > 0 and x < size -1:
		y -= 1; x += 1
		index += 1; tab[y][x] = index
	if y == 0 and x < size - 1:
		x += 1  # вправо если дошли до верхней границы 
	else:
		if y == size - 1 and x == size - 1:
			break
		else:
			y += 1  #вниз если дошли до правой границы
	index += 1; tab[y][x] = index

	if x == size -1 and y == size -1:
		break

	while y < size - 1 and x > 0:
		y += 1; x -= 1
		index += 1; tab[y][x] = index
	if x == 0 and y < size - 1:
		y += 1
	else:
		if y == size - 1 and x == size - 1:
			break
		else:
			x += 1
	index += 1; tab[y][x] = index

for line in tab:
	print(' '.join(map(str, line)))
