from EarthToLine import earthToImage
from LineToEarth import imageToEarth

x, y = 3, 5

a, b = imageToEarth(x, y)
c, d = earthToImage(a, b)

print(x, y)
print(a, b)
print(c, d)
print(c / x, d / y)

