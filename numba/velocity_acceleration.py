import time
from numba import njit, prange

cur_time = time.time()

@njit(fastmath=True)
def simple_numbers(n):
    for l in prange(2, n+1):
        simple = True
        for i in prange(2, l):
            if l % i == 0:
                simple = False
                break
        if simple:
            number = l

simple_numbers(60000)
print(time.time() - cur_time)
