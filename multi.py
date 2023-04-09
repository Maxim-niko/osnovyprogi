import multiprocessing
from math import sqrt
import time
start  = time.time()
def f(n):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
        return True
    
if __name__ == '__main__':
    n = 12345678909876543212345678909876543212345678909876543212345678909876543212345678909876543212345678909876543212345678909876543213456789098765432123456789887
    print(f(n))
    timer = time.time()
    p1 = multiprocessing.Process(target=f, args=(0, ))
    p1.start()
    p2 = multiprocessing.Process(target=f, args=(1, ))
    p2.start()
    p3 = multiprocessing.Process(target=f, args=(2, ))
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('elapsed %.6f seconds' % (time.time() - timer))

