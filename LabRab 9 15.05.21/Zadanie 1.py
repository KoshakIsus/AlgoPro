nums = list(map(int, input().split()))

N = nums[0] #кол-во строк rows
M = nums[1] #кол-во столбцов cols

tab = [[0] * M for _ in range(N)]

for row in range(N):
	for col in range(M):
		tab[row][col] = row*col


for row in tab:
	print(' '.join(map(str, row)))
