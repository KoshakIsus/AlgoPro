line = input()
line = line.split()

result = []
for item in line: #т.к. нужен элемент, а не индекс из списка!!!
	if int(item) % 2 != 0: #проверка элемента
		result.append(item) #если нечётный, то добавляем в новый список
print(*result)


#Неверный метод:
#т.к. здесь брали по индексам, а не по элементам списка!!!

# line = input()
# line = line.split()
# #line = map(int, line)

# for i in line:
# 	if int(line[i]) % 2 == 0:
# 		line.pop([i])
# print(*line, sep=' ')