import os
from EarthToLine import earthToImage
from LineToEarth import imageToEarth
from math import fabs
from random import randint

os.system('clear')
print("================================================================")
for _ in range(12):
    x, y = randint(1, 100000), randint(1, 100000)

    a, b = imageToEarth(x, y)
    c, d = earthToImage(a, b)

    print(x, y)
    print(a, b)
    print(c, d)
    print(c / x, d / y, fabs(c / x - d / y))
    print("================================================================")
