a = input()
a = a.split()
ma = 0
b = []
a = list(map(int, a))
while len(a) > 0:
	ma = (max(a)) #  maximum
	b.append(ma)
	a.remove(max(a))
print(*b)