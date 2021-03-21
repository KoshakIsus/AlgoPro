nums = list(map(int, input().split()))
nums = set(nums)
#  Вводим числа от 1 до 100 с пробелами включительно.
#  Одно число потерялось - вывести его.
setA = set(range(1, 101))
setA -= nums
print(*setA)