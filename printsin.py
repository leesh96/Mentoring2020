from math import *

for i in range(0, 361, 360//40):
    num = int((sin(radians(i))+1)*40)
    print("#" * num)
