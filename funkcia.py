import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(0, 10)
y = 2*np.sin(2*x) + 3*np.cos(3*x) + 5

ax.plot(x, y)

plt.show()
