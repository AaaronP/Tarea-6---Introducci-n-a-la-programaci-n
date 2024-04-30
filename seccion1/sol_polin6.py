def encontrar_raices(coeficientes):
    grado = len(coeficientes) - 1
    raices = []

    # Iteramos sobre los posibles valores de x
    for x in range(-100, 101):
        resultado = 0

        # Calculamos el valor del polinomio para el valor de x actual
        for i in range(grado + 1):
            resultado += coeficientes[i] * (x ** (grado - i))

        # Si el resultado es cero, agregamos el valor de x a las raíces
        if resultado == 0:
            raices.append(x)

    return raices

print(encontrar_raices([6,12,-5]))