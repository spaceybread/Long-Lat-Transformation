from EarthToLine import earthToImage
from LineToEarth import imageToEarth
from math import fabs
from random import randint

for _ in range(5):
    x, y = randint(1, 2000), randint(1, 2000)

    a, b = imageToEarth(x, y)
    c, d = earthToImage(a, b)

    print(x, y)
    print(a, b)
    print(c, d)
    print(c / x, d / y, fabs(c / x - d / y))
    print("==================")
