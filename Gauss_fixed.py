import numpy
from numpy import array, zeros

a = array([[1, -2, 3, -4],
           [5, -6, 7, -8],
           [9, -10, -11, 12],
           [-13, 14, -15, -16]],float)
b = array([17, -18, 19, -20], float)
def method(a, b):
    n = len(b)
    x = zeros(n, float)
    for k in range(n-1):
        for i in range(k+1, n):
            fctr = a[i, k] / a[k, k]
            for j in range(k, n):
                a[i, j] = a[i, j] - fctr*a[k, j]
            b[i] = b[i] - fctr*b[k]
            
    x[n-1] = b[n-1] / a[n-1, n-1]
    for i in range(n-2, -1, -1):
        b_sum = b[i]
        for j in range(i+1, n):
            b_sum = b_sum - a[i, j]*x[j]
    x[i] = b_sum/a[i, i]
    return x

c = method(a, b)          
print('Решение системы:')
print(c)
