import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

x = np.linspace(-4, 4, 100)
y = x/2 + 2

fig, ax = plt.subplots()

ax.plot(x, y, color = 'blue', lw = 2)
ax.vlines(0, y.min(), y.max(), color = 'orange', lw = 1)
ax.hlines(0, x.min(), x.max(), color = 'orange', lw = 1)

fig.set_figwidth(5); fig.set_figheight(20)

plt.show()
