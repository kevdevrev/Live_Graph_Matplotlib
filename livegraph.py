import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

os.getcwd()


def animate(i):
    filedir = "C:/Users/galea/OneDrive/Documents/#Summer 2020/please64/"
    graph_data = open(filedir + 'samplefile.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    # redraw data
    ax1.clear()
    ax1.plot(xs, ys)


# in ms intervals
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
