import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mpl
import matplotlib.pyplot as plt
X, Y = np.meshgrid(
    np.linspace(-math.pi, math.pi, 50),
    np.linspace(-math.pi, math.pi, 50)
)

Z = np.sqrt(X + Y**3)

plt.gca().set_aspect('equal')
surf = plt.pcolor(
    X, Y, Z,
    cmap=cm.RdGy)  
plt.colorbar(surf, shrink=0.9, aspect=10)
plt.show();
