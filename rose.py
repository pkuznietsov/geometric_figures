import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define data set

DATA = np.random.uniform(1, 10, 300).reshape(-1, 3)
X_VALUES = np.arange(3)

# Initial plot

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)
ax.plot(X_VALUES, DATA[0], '-o')

# Update function


def update_wave(val):
    idx = int(sliderwave.val)
    ax.cla()
    ax.plot(X_VALUES, DATA[idx], '-o')
    fig.canvas.draw_idle()


# Sliders

axwave = plt.axes([0.25, 0.05, 0.5, 0.03])

sliderwave = Slider(axwave, 'Event No.', 0, 100, valinit=0, valfmt='%d')
sliderwave.on_changed(update_wave)

plt.show()
'''

def update_rose(val):
    idx = int(sliderwave.val)
    plt.cla()
    plt.polar(theta, r, 'r')
    ax.plot(X_VALUES, DATA[idx], '-o')
    fig.canvas.draw_idle()



import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

theta = np.linspace(0, 2*np.pi, 1000)
alpha, betha = 1, 1
r = alpha * np.sin(betha * theta)

plt.polar(theta, r, 'r')

plt.show()
'''