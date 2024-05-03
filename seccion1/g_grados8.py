def grados(v, g):
    mag_v = (v[0] ** 2 + v[1] ** 2) ** 0.5

    theta = g * (3.141592653589793 / 180)

    x_w = mag_v * cos(theta)
    y_w = mag_v * sin(theta)

    w = (x_w, y_w)

    return w


def sin(theta):
    return theta - (theta**3) / 6 + (theta**5) / 120 - (theta**7) / 5040


def cos(theta):
    return 1 - (theta**2) / 2 + (theta**4) / 24 - (theta**6) / 720


v = (3, 4) 
g = 30
w = grados(v, g)

print("Vector v:", v)
print("Ángulo entre v y w:", g, "grados")
print("Vector w:", w)
