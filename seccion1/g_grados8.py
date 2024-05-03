import math


def grados(g):
    x = 1.0
    theta = math.radians(g)

    y = x * math.tan(theta)

    w = (x, y)

    return w


v = (3, 10)
g = 35
w = grados(g)

print("Vector v:", v)
print("Ángulo entre v y w:", g, "grados")
print("Vector w:", w)
