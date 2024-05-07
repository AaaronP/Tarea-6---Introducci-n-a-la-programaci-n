def ceros(coeficientes):
    invC = coeficientes[::-1]
    pos_ceros = []
    for x in range(-1000, 1001):
        val = 0
        for i, coeficiente in enumerate(invC):
            val += coeficiente * (x**i)

        if val == 0:
            pos_ceros.append(x)
    return pos_ceros


print(ceros([3, 5, -2, 1, -7]))
