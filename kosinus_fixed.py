import math
import matplotlib.pyplot as plt
import numpy as np


ITERATIONS = 13


def my_cos(x):
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow *= x ** 2
        multiplier *= -1 / (2 * n) / (2 * n - 1)
        partial_sum += x_pow * multiplier

    return partial_sum


if __name__=='__main__':
    print(my_cos(0.5))
    print(math.cos(0.5))
    vs = np.vectorize(my_cos)
    print(my_cos, vs)
    arguments = np.arange(1, 10, 0.01)
    plt.plot(arguments, np.cos(arguments), linewidth=4.0, color='red', label='косинус')
    plt.plot(arguments, vs(arguments), linewidth=1.0, color='orange', label='ряд Тейлора')
    plt.legend()
    plt.show()
