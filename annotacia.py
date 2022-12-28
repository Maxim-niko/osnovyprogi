import random
import math


print('Найдём НОД двух чисел')
a = 210
b = random.randrange(-100000, 100000)



def Algoritm_Evklida(b:int) ->int:
    flag=True
    if b>=0:
        while b != a:
            if b > a:
                b = b - a
            else:
                a = a - b
        print(b)
        if b > 1:
            print: ("НОД")
        else:
            print: ("Взаимно простые")
    else:
        flag= False
    return(flag)

    
print('Алгоритм Евклида:', b, Algoritm_Evklida(b))  


try:
     print(Algoritm_Evklida(0 , 9))
     print('Алгоритм Евклида:', b, Algoritm_Evklida(b))
except:
    print("Нецелое число")

try:
    print(Algoritm_Evklida(-88))
    print('Алгоритм Евклида:', b, Algoritm_Evklida(b))
except:
    print("отрицательное число")

    

     

