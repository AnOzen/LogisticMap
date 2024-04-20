import numpy
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider

init_pop = 0.5
rate = 2.1

steps = 100


def logyb(n, initp, ra):
    p = initp
    for j in range(n):
        p = ra * p * (1 - p)
    return p


x = numpy.linspace(0, steps, steps)
y = numpy.zeros(len(x))

for i in range(len(x)):
    y[i] = logyb(i, init_pop, rate)

fig, ax = plt.subplots()
ax.set_xlabel("Iteration")
ax.set_ylabel("Population (%)")
fig.subplots_adjust(bottom=0.2)
plt.ylim(0, 1)
line, = ax.plot(x, y)

axis_rate = fig.add_axes([0.2, 0.05, 0.65, 0.03])
r_slider = Slider(
    ax=axis_rate,
    label="Rate",
    valmin=0,
    valmax=4,
    valinit=rate
)


def update(_val):
    ys = numpy.zeros(len(x))
    for itr in range(len(x)):
        ys[itr] = logyb(itr, init_pop, r_slider.val)
    line.set_ydata(ys)
    fig.canvas.draw_idle()


r_slider.on_changed(update)

ax.set_title("Logistic Iterations")
plt.show()
