
import math
import numpy
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

if_name__='__main__'
arguments = numpy.arange(1, 300)
mpp.plot(
        arguments,
        [math.cos(a**3) * 2*math.tan(a/2) for a in arguments]
    )
mpp.show()
    
