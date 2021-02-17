import matplotlib.pyplot as plt
import numpy as np
def my_func(x, a, b, c, d):

    return (a * x ** 3 + b * x ** 2 + c * x) / (x + d)
styles = plt.style.available
plt.style.use(styles[2])

a = 4; b = -3; c = -4; d = -5
legend = '{} * x ** 3 + {} * x ** 2 + {} * x'.format(a, b, c)

left = -100; right = 4.5; step = 0.5
data_x = np.arange(left, right, step)
data_y = [my_func(x, a, b, c, d) for x in data_x]
plt.plot(data_x, data_y, linewidth = 2, color='#00ff00')


left = 4.5; right = 5.5; step = 0.5
data_x = np.arange(left, right, step)
data_y = [my_func(x, a, b, c, d) for x in data_x]
plt.plot(data_x, data_y, linewidth = 2, color='#e6e600')

left = 5.5; right = 100; step = 0.5
data_x = np.arange(left, right, step)
data_y = [my_func(x, a, b, c, d) for x in data_x]
plt.plot(data_x, data_y, linewidth = 2, color='#9933ff')

data_x = []; data_y = []
pos_x = 0
while pos_x <= right:
    try:
        pos_y = my_func(pos_x, a, b, c, d)
        data_x.append(pos_x)
        data_y.append(pos_y)
    except:
        pass
    pos_x += step

plt.title('График. Вот он.')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend([legend])
plt.grid(True)
plt.axhline(linewidth = 2, color = '#ff0000')
plt.axvline(linewidth = 2, color = '#ff0000')
plt.show()
