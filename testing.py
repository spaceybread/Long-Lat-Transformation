import os
from EarthToLine import earthToImage
from LineToEarth import imageToEarth
from math import fabs
from random import randint

idx = 0
print("================================================================")
for _ in range(100000):
    os.system('clear')
    x, y = randint(1, 800), randint(1, 800)
    a, b = imageToEarth(x, y)
    c, d = earthToImage(a, b)
    
    e, f = randint(-89, 89), randint(-89, 89)
    g, h = earthToImage(e, f)
    i, j = imageToEarth(g, h)
    
    print("Test case:", _ + 1)
    print()
    print("Fuzz values:", x, y)
    print("Earth Coordinates:", a, b)
    print("Line:", c, d)
    print()
    print("Fuzz values:", e, f)
    print("Line:", g, h)
    print("Earth Coordinates:", i, j)
    print()
    try:
        flag = False
        mx = [c/x, d/y, i/e, j/f]
        print("Ratios:", mx)
        for m in mx:
            if fabs(1 - m) > 0.0000000000009:
                inp = input()
                if inp == "exit":
                    flag = True
                    break
        if flag:
            break
    except:
        print("Division by 0")
    #print(c / x, d / y, fabs(c / x - d / y))
    #print(x / c, y / d, fabs(x / c - y / d))
    #print(x / c * c, x / c * d)
    #print(y / d * c, y / d * d)
    #print(fabs(x / c * c - y / d * c), fabs(x / c * d - y / d * d))
    print("================================================================")
