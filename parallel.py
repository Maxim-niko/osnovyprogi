import multiprocessing
from math import sqrt
import time
start  = time.time()
def f(n):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
        return True
def a(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
        return True
if __name__ == '__main__':
    n = 123456789098765432123456789098765432123456789098765432123456789098765432123456789098765432234567890987654321234567890987654321234567890987654321234567890987891
    x = 987654321234567890987654321123456789098765432123456789098765432123456789098765432123456789098765432123456789098765432123456789098765432123456789098765432123457
    print(f(n))
    print(a(x))
    timer = time.time()
    p1 = multiprocessing.Process(target=f, args=(n, ))
    p1.start()
    p2 = multiprocessing.Process(target=a, args=(x, ))
    p2.start()
    p1.join()
    p2.join()
    print('elapsed %.6f seconds' % (time.time() - timer))
