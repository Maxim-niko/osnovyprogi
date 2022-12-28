
import itertools
import math
from numbers import Number

class matrix:

    print("Перемножим две матрицы")
print("Введите элементы первой матрицы")



a11 = input("a11 ")
try:
    a11=int(a11)
except:
    pass
a12 = input("a12 ")
try:
   a12= int(a12)
except:
    pass
a21 = input("a21 ")
try:
   a21= int(a21)
except:
    pass
a22 = input("a22 ")
try:
   a22= int(a22)
except:
    pass
print("Введите элементы второй матрицы")
b11 = input("b11 ")
try:
    b11=int(b11)
except:
    pass
b12 = input("b12 ")
try:
   b12= int(b12)
except:
    pass
b21 = input("b21 ")
try:
   b21= int(b21)
except:
    pass
b22 = input("b22 ")
try:
   b22= int(b22)
except:
    pass

print("Новая матрица")
print("c11")
print(a11 * b11 + a12 * b21)
print("c12")
print(a11 * b12 + a12 * b22)
print("c21")
print(a21 * b11 + a22 * b21)
print("c22")
print(a21 * b12 + a22 * b22)
