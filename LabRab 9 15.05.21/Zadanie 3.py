nums = list(map(int, input().split()))

N = nums[0] #кол-во строк rows
M = nums[1] #кол-во столбцов cols

tab = [[0] * M for _ in range(N)]
index = 0
for col in range(M):
	if col % 2 == 0: 
		for row in range(0, N):
			index += 1
			tab[row][col] = index
	else:
		for row in range(N-1, -1, -1):
			index += 1
			tab[row][col] = index

for row in tab:
	print(' '.join(map(str, row)))
