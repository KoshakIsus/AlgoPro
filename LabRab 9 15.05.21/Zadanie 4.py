size = int(input())

tab = [[0] * size for _ in range(size)]
tab[0] = [(col+1) for col in range(size)]

index = size
y = 0; x = size - 1; r = size

while index < size * size:
	for _ in range(size):
		r -= 1
		for _ in range(r):  #вертикаль
			y += 1
			index += 1; tab[y][x] = index
		for _ in range(r):  #горизонталь
			x -= 1
			index += 1; tab[y][x] = index
		r -= 1
		if index >= size * size:
			break
		for _ in range(r): #верт
			y -= 1
			index += 1; tab[y][x] = index
		for _ in range(r): #горизонт
			x += 1
			index += 1; tab[y][x] = index

for line in tab:
	print(' '.join(map(str, line)))
