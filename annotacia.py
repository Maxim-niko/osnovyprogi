import random
import math
from typeguard import typechecked

@typechecked
def algoritm_Evklida(a:int, b:int)->int:
    if b>=0:
        while b != a:
            if b > a:
                b = b - a
            else:
                a = a - b
        return b

print(algoritm_Evklida(100, 40))
print(algoritm_Evklida(100, 40.0)) # Eсли функции дать неправильные параметры, то она вылетит
