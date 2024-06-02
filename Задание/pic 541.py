import numpy as np
import matplotlib.pyplot as plt
import locale


fig, ax = plt.subplots()
locale.setlocale(locale.LC_NUMERIC, "de_RU")
font = {'family': 'Times New Roman',
        'size': 12}
plt.rc('font', **font)
ax.ticklabel_format(useLocale=True)
ax.grid(linewidth = 0.3)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()
ax.xaxis.set_major_locator(plt.MultipleLocator(0.05))
ax.plot(0, 0)

def y(n, x):
    f = 1
    return np.sin(n * 2*np.pi * f * x)

x = np.linspace(0, 0.5, 100)

ax.plot(x, y(1, x), 'black')
ax.plot(x, y(3, x), '#bbbbbb')

plt.show()