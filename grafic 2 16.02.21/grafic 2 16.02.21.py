import matplotlib.pyplot as plt
import numpy as np

def my_func(x, a, b, c):
    '''
    y = a * x ** 2 + b * x + c
    '''
    return (a * x ** 2 + b * x + c)

plt.xkcd() #пьяный инжинер (внешний вид)

styles = plt.style.available

plt.style.use(styles[3])

a = 2; b = -3; c = 0
legend = '{} * x ** 2 + {} * x + {}'.format(a, b, c)
left = -8; right = 8; step = .1


data_x = np.arange(left, right, step)
data_y = [my_func(x, a, b, c) for x in data_x]
plt.plot(data_x, data_y, linewidth = 1, color= '#3333ff')


plt.title('График. Вот он.')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend([legend])
plt.grid(True)
plt.axhline(linewidth = 2, color = '#ff0000')
plt.axvline(linewidth = 2, color = '#ff0000')
plt.show()
