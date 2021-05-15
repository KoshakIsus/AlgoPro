size = int(input())

tab = [[0] * size for _ in range(size)]

index = 1
y = size // 2; x = size // 2; r = 0

tab[y][x] = index

if size != 1:
	x += 1; index += 1
	tab[y][x] = index

while index < size * size:
	for _ in range(size):
		r += 1
		for _ in range(r):  #верт
			y += 1
			index += 1; tab[y][x] = index
		r += 1

		for _ in range(r):  #гориз
			x -= 1
			index += 1; tab[y][x] = index

		for _ in range(r): #горизонталь
			y -= 1
			index += 1; tab[y][x] = index
		for _ in range(r): #вертикаль
			x += 1
			index += 1; tab[y][x] = index

		if index >= size * size:
			break
		x += 1; index += 1; tab[y][x] = index #если не конец, то дополняем ещё ячейку и ещё круг

for line in tab:
	print(' '.join(map(str, line)))
