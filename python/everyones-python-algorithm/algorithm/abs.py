# abs.py

import math

def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a
    
def abs_square(a):
    b = a * a
    return math.sqrt(b)


print(abs_sign(7))
print(abs_sign(-7))
print(abs_sign(0))
print(abs_square(9))
print(abs_square(-9))
print(abs_square(0))