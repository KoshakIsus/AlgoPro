nums = list(map(int, input().split()))

rows = nums[0]  # кол-во строк (длина вертикали)
cols = nums[1]  # кол-во столбцов (длина горизонтали)

r_rows = rows  # это вместо r - шаг по вертикаль
c_cols = cols  # это вместо r - шаг по горизонтали
tab = [[0] * cols for _ in range(rows)]
tab[0] = [(col+1) for col in range(cols)]

y = 0  #это уровень вертикали (номер строки)
x = cols - 1 # уровень горизонтали (номер столбца)
index = cols  #индекс, т.е. последний номер строки + 1, т.к. дальше путь вниз

while index < rows * cols:
	for _ in range(cols):
		r_rows -= 1
		c_cols -= 1
		for _ in range(r_rows):  #вертикаль вниз
			y += 1  # увеличиваем номер строки - вниз сдвиг
			index += 1; tab[y][x] = index
		for _ in range(c_cols):  #горизонталь влево
			x -= 1  # уменьшаем номер строки - влево сдвиг
			index += 1; tab[y][x] = index

		r_rows -= 1
		c_cols -= 1

		if index >= rows * cols:
 			break

		for _ in range(r_rows):  # вертикаль вверх
			y -= 1  # уменьшаем номер строки - сдвиг вверх
			index += 1; tab[y][x] = index
		for _ in range(c_cols):  # горизонталь вправо
			x += 1  # увеличиваем номер столбца - сдвиг вправо
			index += 1; tab[y][x] = index

for line in tab:
	print(' '.join(map(str, line)))
