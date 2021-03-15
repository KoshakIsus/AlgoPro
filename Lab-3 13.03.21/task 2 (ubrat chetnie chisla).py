line = input()
line = line.split()
#line = map(int, line)
for i in line:
	if int(line[i]) % 2 == 0:
		line.pop([i])
print(*line, sep=' ')