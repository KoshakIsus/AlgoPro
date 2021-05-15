nums = list(map(int, input().split()))

N = nums[0] #кол-во строк rows
M = nums[1] #кол-во столбцов cols

tab = [[0] * M for _ in range(N)]
index = 0
for row in range(N):
	if row % 2 == 0: 
		for col in range(0, M):
			index += 1
			tab[row][col] = index

	else:
		for col in range(M-1, -1, -1):
			index += 1
			tab[row][col] = index

for row in tab:
	print(' '.join(map(str, row)))
