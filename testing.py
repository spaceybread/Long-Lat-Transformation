import os
from EarthToLine import earthToImage
from LineToEarth import imageToEarth
from math import fabs
from random import randint

os.system('clear')
print("================================================================")
for _ in range(8):
    x, y = randint(1, 100000), randint(1, 100000)

    a, b = imageToEarth(x, y)
    c, d = earthToImage(a, b)

    print(x, y)
    print(a, b)
    print(c, d)
    print(c / x, d / y, fabs(c / x - d / y))
    print(x / c, y / d, fabs(x / c - y / d))
    print(x / c * c, x / c * d)
    print(y / d * c, y / d * d)
    print("================================================================")
