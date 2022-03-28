import numpy as np
import matplotlib.pyplot as plt


x_values = np.linspace(-1, 1, 100)

x_squr = x_values**2
x_cube = x_values**3

fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(x_values, x_values, color="black", label="Linear")
ax.plot(x_values, x_squr, label="Quadratic")
ax.plot(x_values, x_cube, label="Cubic")
ax.legend(frameon=False)
plt.savefig("functions.png")


