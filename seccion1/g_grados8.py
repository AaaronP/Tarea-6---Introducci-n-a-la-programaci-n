import math


def vector(v, g):
    x, y = v
    magnitud = math.sqrt(x * x + y * y)
    angulo = math.radians(g)

    i = magnitud * math.cos(angulo)
    j = magnitud * math.sin(angulo)
    w = (i, j)
    return w


print(vector((2, 3), 45))
