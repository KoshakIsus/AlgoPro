line = input()
line = map(int, line.split())
line_reverse = []
ma = 0

for i in line:
	ma = max(line) #maximum
	line_reverse.append(ma)
	line.pop(line.index(max(line)))
print(*line_reverse)