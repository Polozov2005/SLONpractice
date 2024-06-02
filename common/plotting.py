import numpy as np
import matplotlib.pyplot as plt
from matplotlib import figure
import locale

def plotting(function, a, b):
    fig = figure.Figure()
    ax = fig.add_subplot()
    locale.setlocale(locale.LC_NUMERIC, "de_RU")
    font = {'family': 'Segoe Ui',
            'size': 10}
    plt.rc('font', **font)
    ax.ticklabel_format(useLocale=True)
    ax.grid(linewidth = 0.5, color='#7b7b7b')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()
    ax.plot(0, 0)

    ax_color = '#ffffff'
    ax.set_facecolor('#333333')
    fig.set_facecolor('#333333')
    ax.spines['bottom'].set_color(ax_color)
    ax.spines['left'].set_color(ax_color) 
    ax.tick_params(axis='x', colors=ax_color)
    ax.tick_params(axis='y', colors=ax_color)

    x = np.linspace(a, b, 1000)
    y = function(x)
    ax.plot(x, y, color='#007fff')

    fig.set_size_inches(7.2, 7.2)

    return fig