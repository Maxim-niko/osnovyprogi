import math
import numpy as np
import random

n = 1000
k = 0
s0 = 100

for _ in range(n):
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)

    if 2*np.sin(2*x) + 3*np.cos(3*x) + 5 >= y:
        k += 1
    
print((k / n) * s0)
